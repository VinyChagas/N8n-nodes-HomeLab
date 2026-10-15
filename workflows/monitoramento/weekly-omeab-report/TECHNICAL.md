# Técnica — 07 - WEEKLY OMEAB REPORT

## Visão geral

- **Nodes:** 16
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, docker, hermes, omeab, postgres, postgresql, rag, restic, telegram
- **Webhooks:** []
- **Schedules:** `[{"node": "Weekly Schedule", "rule": {"interval": [{"field": "cronExpression", "expression": "15 8 * * 1"}]}}]`
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

### Weekly Schedule

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get System

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get Storage

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get Disk Capacity

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get Docker

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get Backups

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get Current Week Events

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get Previous Week Events

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Get Capacity History

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Build Weekly Snapshot

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Prepare Weekly Message

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Prepare Capacity Persist

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Store Capacity Snapshot

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Restore Snapshot Context

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Generate HMAC

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.
### Send Weekly Report to Hestia

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `07 - WEEKLY OMEAB REPORT`.


## Code nodes

### Code: Build Weekly Snapshot

- Linguagem: js
- Linhas: 855
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
    const body = j.data && typeof j.data === 'object' && !Array.isArray(j.data) && (j.statusCode || j.hea
```
### Code: Prepare Weekly Message

- Linguagem: js
- Linhas: 180
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const snap = $json.snapshot;
const icon = { healthy: '🟢', attention: '🟠', degraded: '🟡', critical: '🔴' };
const trendIcon = { improving: '📈', stable: '↔️', worsening: '⚠️', insufficient_data: '❔' };
const o = snap.overall_status || 'healthy';

function fmtDateSP(iso) {
  try {
    return new Intl.DateTimeFormat('pt-BR', {
      timeZone: 'America/Sao_Paulo',
      day: '2-digit',
      month: '2-digit',
    }).format(new Date(iso));
  } catch (e) {
    return String(iso || '').slice(0, 10);
  }

```
### Code: Prepare Capacity Persist

- Linguagem: js
- Linhas: 46
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const rows = $json.capacity_rows || [];
const snap = $json.snapshot;
const alert = $json.alert;

if (!rows.length) {
  return [{
    json: {
      snapshot: snap,
      alert,
      capacity_persist: { attempted: false, reason: 'no_rows' },
    },
  }];
}

function sqlLit(v) {
  if (v === null || v === undefined) return 'NULL';
  if (typeof v === 'number' && Number.isFinite(v)) return String(v);
  return "'" + String(v).replace(/'/g, "''") + "'";
}

const values = rows.map((r) => {
  const mount
```
### Code: Restore Snapshot Context

- Linguagem: js
- Linhas: 14
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
// Reattach snapshot/alert after Postgres node (which may replace json)
let snap = null;
let alert = null;
let persist = null;
try {
  const prep = $('Prepare Capacity Persist').first().json;
  snap = prep.snapshot;
  alert = prep.alert;
  persist = prep.capacity_persist;
} catch (e) {
  snap = $json.snapshot || null;
  alert = $json.alert || null;
}
return [{ json: { snapshot: snap, alert, capacity_persist: persist || { attempted: false } } }];

```
### Code: Generate HMAC

- Linguagem: js
- Linhas: 34
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

// Reutiliza rota hestia-alerts (deliver_only): texto formatado = mensagem Telegram.
const body = JSON.stringify({
  alert: {
    text: event.alert.text,
  },
});

const timestamp = String(Math.floor(Date.now() / 1000));
const canonicalPayload = `${timestamp}.${body}`;
const signature = crypto
  .
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
