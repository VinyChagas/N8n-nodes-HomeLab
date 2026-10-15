#!/usr/bin/env python3
"""Validação estrutural de templates n8n (não importa/executa)."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
checked = 0

for path in sorted(ROOT.glob("workflows/**/workflow.json")):
    checked += 1
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        errors.append(f"{path}: JSON inválido: {e}")
        continue
    for key in ("name", "nodes", "connections"):
        if key not in data:
            errors.append(f"{path}: falta campo '{key}'")
    nodes = data.get("nodes") or []
    names = [n.get("name") for n in nodes]
    if len(names) != len(set(names)):
        errors.append(f"{path}: nomes de nodes duplicados")
    ids = [n.get("id") for n in nodes if n.get("id")]
    if len(ids) != len(set(ids)):
        errors.append(f"{path}: IDs de nodes duplicados")
    node_names = set(names)
    for src, outs in (data.get("connections") or {}).items():
        if src not in node_names:
            errors.append(f"{path}: conexão de origem inexistente: {src}")
        for _, branches in (outs or {}).items():
            for branch in branches or []:
                for dest in branch or []:
                    if dest.get("node") not in node_names:
                        errors.append(f"{path}: destino inexistente: {dest.get('node')}")
    # crude secret heuristics on public templates
    raw = path.read_text()
    for pat, label in [
        (r"(?i)bearer\s+[a-z0-9\-._~+/]{20,}", "bearer"),
        (r"(?i)(sk-|ghp_|glpat-)[a-zA-Z0-9]{10,}", "token_prefix"),
    ]:
        import re
        if re.search(pat, raw):
            errors.append(f"{path}: possível segredo residual ({label})")

print(f"Checked {checked} workflow.json files")
if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("OK — Compatibilidade estrutural validada. Importação real não executada.")
