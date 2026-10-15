# Técnica — 12 - IMMICH MONITOR

## Visão geral

- **Nodes:** 14
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, immich, postgres, postgresql, rag
- **Webhooks:** []
- **Schedules:** `[{"node": "Schedule Trigger", "rule": {"interval": [{"field": "minutes", "minutesInterval": 10}]}}]`
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

- `GET` `={{ $env.IMMICH_URL }}/api/jobs`
- `GET` `={{ $env.IMMICH_URL }}/api/server/statistics`
- `GET` `={{ $env.IMMICH_URL }}/api/assets/statistics`
- `GET` `={{ $env.IMMICH_URL }}/api/server/storage`
- `GET` `={{ $env.IMMICH_URL }}/api/server/about`
- `GET` `http://immich_machine_learning:3003/ping`
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Get Immich Jobs

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Get Immich Server Statistics

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Get Immich Asset Statistics

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Get Immich Storage

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Get Immich About

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Get Immich ML Ping

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Build Snapshot

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Get Previous State

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Evaluate Changes

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Persist Snapshot

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Expand Events

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `1`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.
### Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `12 - IMMICH MONITOR`.


## Code nodes

### Code: Build Snapshot

- Linguagem: js
- Linhas: 158
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript

const testMode = String($env.IMMICH_MONITOR_TEST_MODE || 'false').toLowerCase() === 'true';
const now = new Date().toISOString();

function safeJson(nodeName) {
  try {
    const n = $(nodeName).first().json;
    return n && typeof n === 'object' ? n : {};
  } catch (e) {
    return { _error: true, _message: String(e?.message || e) };
  }
}

function safeText(nodeName) {
  try {
    const item = $(nodeName).first();
    if (item.json && typeof item.json === 'object' && item.json.data !== undefi
```
### Code: Evaluate Changes

- Linguagem: js
- Linhas: 225
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript

const snapshotWrap = $('Build Snapshot').first().json || {};
const snapshot = snapshotWrap.snapshot || {};
let previous = null;
try {
  const rows = $('Get Previous State').all().map((i) => i.json).filter(Boolean);
  previous = rows.find((r) => r.overall_status != null) || null;
  // when no rows, postgres may return empty object
  if (previous && previous.overall_status === undefined && Object.keys(previous).length === 0) previous = null;
} catch (e) {
  previous = null;
}

const now = snapsho
```
### Code: Expand Events

- Linguagem: js
- Linhas: 8
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript

const data = $json;
const persist = data.persist;
const events = Array.isArray(data.events) ? data.events : [];
if (!events.length) {
  return [{ json: { should_emit: false, persist, skip_event: true } }];
}
return events.map((ev) => ({ json: { ...ev, persist, skip_event: false } }));

```


## Dependências

### Aplicações

- credential:postgres
- immich
- postgres
- postgresql
- rag

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
