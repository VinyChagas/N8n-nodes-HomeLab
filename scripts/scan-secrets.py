#!/usr/bin/env python3
"""Scan de segredos nos arquivos do hub. Não imprime valores."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "__pycache__"}
PATTERNS = [
    ("api_key_assignment", re.compile(r'(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*["\'][^"\']{12,}["\']')),
    ("bearer_token", re.compile(r'(?i)bearer\s+[a-z0-9\-._~+/]{20,}')),
    ("private_ip", re.compile(r'\b(?:192\.168\.\d{1,3}\.\d{1,3}|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b')),
    ("connection_string", re.compile(r'(?i)(?:postgres|mysql|mongodb|redis)://[^\s"\']+')),
    ("aws_key", re.compile(r'AKIA[0-9A-Z]{16}')),
]

findings = []
for path in ROOT.rglob("*"):
    if any(p in SKIP for p in path.parts):
        continue
    if not path.is_file():
        continue
    if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml", ".env", ".txt", ".example"} and path.name not in {"env.example"}:
        if "sample-payloads" not in path.parts and path.suffix:
            continue
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for line_no, line in enumerate(text.splitlines(), 1):
        # allow placeholders and docs mentioning private IP as concept in SECURITY docs with example.invalid
        if "{{$env." in line or "change-me" in line or "REDACTED" in line or "CREDENTIAL_ID" in line or "<LAN_BIND_IP>" in line or "<DOCKER_NET>" in line or "<REDACTED_IP>" in line:
            continue
        if "192.168." in line and ("docs/" in str(path) or path.name in {"ARCHITECTURE.md", "README.md", "COMPATIBILITY.md"}):
            # architecture may mention bind address as inventory fact — flag as info
            findings.append({"severity": "info", "type": "private_ip_in_docs", "file": str(path.relative_to(ROOT)), "field": f"line {line_no}", "action": "Revisar se o IP de inventário deve permanecer apenas em docs de ambiente"})
            continue
        for label, pat in PATTERNS:
            if pat.search(line):
                sev = "high" if label in ("bearer_token", "api_key_assignment", "connection_string", "aws_key") else "medium"
                findings.append({
                    "severity": sev,
                    "type": label,
                    "file": str(path.relative_to(ROOT)),
                    "field": f"line {line_no}",
                    "action": "Remover ou substituir por placeholder antes de publicar",
                })

# dedupe
uniq = []
seen = set()
for f in findings:
    key = (f["type"], f["file"], f["field"])
    if key in seen:
        continue
    seen.add(key)
    uniq.append(f)

print(f"Scan complete. Findings: {len(uniq)}")
for f in uniq:
    print(f"[{f['severity']}] {f['type']} | {f['file']} | {f['field']} | {f['action']}")
sys.exit(1 if any(f["severity"] == "high" for f in uniq) else 0)
