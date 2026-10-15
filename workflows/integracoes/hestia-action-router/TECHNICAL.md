# Técnica — 13 - HESTIA ACTION ROUTER

## Visão geral

- **Nodes:** 32
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.postgres`, `n8n-nodes-base.respondToWebhook`, `n8n-nodes-base.switch`, `n8n-nodes-base.webhook`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** audiobook, credential:postgres, docker, immich, media-manager, omeab, postgres, postgresql, rag, restic
- **Webhooks:** [{"node": "Webhook", "path": "hestia-action", "httpMethod": "POST"}]
- **Schedules:** `[]`
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
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/backups` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/docker` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/disk-capacity` (URL privada original → placeholder)
- `GET` `{{$env.OMEAB_SERVICE_URL}}/stats` (URL privada original → placeholder)
- `GET` `http://audiobook-factory:8080/stats`
- `GET` `{{$env.OMEAB_SERVICE_URL}}/stats` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Webhook

- **Tipo:** `n8n-nodes-base.webhook`
- **Versão:** `2.1`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Rate Limit Check

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Auth Validate Policy

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Should Execute?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Audit Reject

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Respond Reject

- **Tipo:** `n8n-nodes-base.respondToWebhook`
- **Versão:** `1.1`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Security Dedup Check

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Reserve Request

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Replay Gate

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Not Replay?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Resolve Action

- **Tipo:** `n8n-nodes-base.switch`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec system.status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec storage.status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec backup.status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec docker.status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec disk.status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec rag.stats

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec audiobook.stats

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec media.stats

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec immich.status

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Exec Fallback

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Sanitize Result

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Audit Update

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Respond Success

- **Tipo:** `n8n-nodes-base.respondToWebhook`
- **Versão:** `1.1`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Respond Replay

- **Tipo:** `n8n-nodes-base.respondToWebhook`
- **Versão:** `1.1`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Prepare Security Event

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Should Emit Security?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Emit Security Event

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Replay Security Dedup

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Prepare Replay Security

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Emit Replay Security?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.
### Emit Replay Security Event

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `13 - HESTIA ACTION ROUTER`.


## Code nodes

### Code: Auth Validate Policy

- Linguagem: js
- Linhas: 350
- Caminhos absolutos detectados: False
- URLs privadas no código: True
- Prévia sanitizada:

```javascript
const crypto = require('crypto');

const REPLAY_WINDOW_SEC = 300;
const RATE_LIMIT_PER_MIN = 30;
const ALLOWED_RISKS = new Set(['READ']);

const REGISTRY = {
  'system.status': {
    description: 'Estado geral do OMEAB (CPU/RAM/uptime/load).',
    risk: 'READ',
    enabled: true,
    requires_confirmation: false,
    parameter_schema: { type: 'object', additionalProperties: false, properties: {} },
    executor: 'system.status',
    timeout_ms: 10000,
    audit: true,
  },
  'storage.status': {

```
### Code: Replay Gate

- Linguagem: js
- Linhas: 48
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const ctx = $('Auth Validate Policy').first().json;
const rows = $input.all().map((i) => i.json).filter(Boolean);
const inserted = rows.find((r) => r && (r.id != null || r.inserted === true || r.request_id));

const ok = !!(inserted && (inserted.id != null || inserted.inserted === true));

if (!ok) {
  const startedMs = Number(ctx.started_ms || Date.now());
  const response = {
    request_id: ctx.request_id,
    action: ctx.registry_action,
    status: 'rejected',
    executed: false,
    requi
```
### Code: Exec Fallback

- Linguagem: js
- Linhas: 1
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
return [{ json: { error: { message: 'unknown_action_executor' }, statusCode: 403 } }];
```
### Code: Sanitize Result

- Linguagem: js
- Linhas: 250
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const startedMs = Number($('Auth Validate Policy').first().json.started_ms || Date.now());
const ctx = $('Auth Validate Policy').first().json;
const action = ctx.registry_action;
const requestId = ctx.request_id;
const executorItem = $input.first().json || {};

function fail(errorCode, message, partialData = {}) {
  const finished = new Date().toISOString();
  const response = {
    request_id: requestId,
    action,
    status: 'failed',
    executed: false,
    requires_confirmation: false,
  
```
### Code: Prepare Security Event

- Linguagem: js
- Linhas: 31
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const auth = $('Auth Validate Policy').first().json;
const name = auth.security_event_name || 'security_event';
let recent = 0;
try {
  const rows = $('Security Dedup Check').all().map((i) => i.json);
  recent = Number((rows.find((r) => r.recent_security != null) || rows[0] || {}).recent_security || 0);
} catch (e) { recent = 0; }
const should = !!auth.security_event && recent < 3;
return [{
  json: {
    should_emit_security: should,
    response: auth.response,
    http_status: auth.http_statu
```
### Code: Prepare Replay Security

- Linguagem: js
- Linhas: 31
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const ctx = $('Replay Gate').first().json;
let recent = 0;
try {
  const rows = $('Replay Security Dedup').all().map((i) => i.json);
  recent = Number((rows.find((r) => r.recent_security != null) || {}).recent_security || 0);
} catch (e) { recent = 0; }
const should = !!ctx.security_event && recent < 3;
const response = ctx.response;
if (!response) {
  throw new Error('Replay response missing');
}
return [{
  json: {
    should_emit_security: should,
    response,
    http_status: ctx.http_statu
```


## Dependências

### Aplicações

- audiobook
- credential:postgres
- docker
- immich
- media-manager
- omeab
- postgres
- postgresql
- rag
- restic

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
