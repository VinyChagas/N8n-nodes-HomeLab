# Técnica — 06 - DAILY OMEAB REPORT

## Visão geral

- **Nodes:** 11
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, docker, hermes, omeab, postgres, postgresql, rag, restic, telegram
- **Webhooks:** []
- **Schedules:** `[{"node": "Daily Schedule", "rule": {"interval": [{"field": "cronExpression", "expression": "0 8 * * *"}]}}]`
- **Error workflow dedicado:** não observado no grafo (falhas tipicamente via branches If/Filter)

## Fluxo lógico (reconstruído)

TRIGGER / ENTRADA
   |
   v
COLETA / NORMALIZAÇÃO
   |
   v
AVALIAÇÃO / DECISÃO
   |
   +-- (sem mudança) --> FIM
   |
   v
PERSISTÊNCIA (quando houver Postgres)
   |
   v
NOTIFICAÇÃO (Event Bus / Hermes)

Detalhe por conexão em [diagram.md](diagram.md).

## HTTP

- `GET` `{{$env.SERVICE_BASE_URL}}/v1/system` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/storage` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/disk-capacity` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/docker` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/backups` (URL privada original → placeholder)
- `POST` `{{$env.HERMES_URL}}`

## Nodes

### Daily Schedule

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Get System Health

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Get Storage Health

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Get Disk Capacity

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Get Docker Health

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Get Backup Health

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Get Last 24h Events

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Build Daily Snapshot

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Prepare Daily Message

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Generate HMAC

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.
### Send Daily Report to Hestia

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `06 - DAILY OMEAB REPORT`.


## Code nodes

### Code: Build Daily Snapshot

- Linguagem: js
- Linhas: 292
- Caminhos absolutos detectados: False
- URLs privadas no código: True
- Prévia sanitizada:

```javascript
function safeNode(name) {
  try {
    const item = $(name).first();
    if (!item) return { status: 'unavailable', reason: 'empty', data: null };
    const j = item.json ?? {};
    if (j.error || j.message === 'Error' || (typeof j.statusCode === 'number' && j.statusCode >= 400)) {
      return { status: 'unavailable', reason: j.error?.message || j.message || 'http_error', data: null };
    }
    // neverError may put body under data
    const body = j.data && typeof j.data === 'object' && !Array
```
### Code: Prepare Daily Message

- Linguagem: js
- Linhas: 130
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const snap = $json.snapshot;
const icon = { healthy: '🟢', degraded: '🟡', critical: '🔴' };
const o = snap.overall_status || 'healthy';

function lineOrWarn(ok, okText, warnText) {
  return ok ? okText : warnText;
}

const sys = snap.system;
const storage = snap.storage;
const disk = snap.disk_capacity;
const docker = snap.docker;
const backups = snap.backups;
const postgres = snap.postgres;
const events = snap.events;
const internet = snap.internet;

const lines = [];
lines.push('🏠 OMEAB — Resumo
```
### Code: Generate HMAC

- Linguagem: js
- Linhas: 35
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const crypto = require('crypto');

const event = $json;
const secret = $env.HESTIA_WEBHOOK_SECRET;

if (!secret) {
  throw new Error('HESTIA_WEBHOOK_SECRET não está disponível no ambiente do n8n.');
}

// Reutiliza rota hestia-alerts (deliver_only=true):
// o texto formatado É a mensagem Telegram. Snapshot estruturado fica no workflow.
const body = JSON.stringify({
  alert: {
    text: event.alert.text,
  },
});

const timestamp = String(Math.floor(Date.now() / 1000));
const canonicalPayload = `
```


## Dependências

### Aplicações

- credential:postgres
- docker
- hermes
- omeab
- postgres
- postgresql
- rag
- restic
- telegram

### Credenciais a recriar

- Tipo `postgres` — configurar no n8n local com permissões mínimas de leitura quando possível

### Variáveis de ambiente esperadas (placeholders)

- `SERVICE_BASE_URL`
- `OMEAB_SERVICE_URL`
- `HERMES_URL`
- `HESTIA_WEBHOOK_SECRET` / `HESTIA_ACTION_SECRET` (quando aplicável)
- `AUTH_TOKEN` / `SECRET` (genéricos após sanitização)

## Segurança do código

Não foram embutidos valores de segredos no template público. Secrets devem viver em `$env` ou credenciais n8n.
