# Técnica — 18 - OMEAB SELF HEALTH

## Visão geral

- **Nodes:** 19
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.filter`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.manualTrigger`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, docker, hermes, http-port:5678, immich, obsidian, omeab, postgresql, rag, telegram
- **Webhooks:** []
- **Schedules:** `[{"node": "Schedule Trigger", "rule": {"interval": [{"field": "minutes", "minutesInterval": 5}]}}]`
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

- `GET` `{{$env.SERVICE_BASE_URL}}/health` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/api/v1/workflows?limit=50` (URL privada original → placeholder)
- `GET` `={{ '{{$env.SERVICE_BASE_URL}}/api/v1/executions?limit=5&includeData=false&workflowId=' + $json.workflow_id }}` (URL privada original → placeholder)
- `POST` `{{$env.HERMES_URL}}`
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Get Health Agent

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### List n8n Workflows

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Get Self Health Meta

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Merge Inputs

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Build Exec Targets

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Get Last Executions

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Attach Exec Meta

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Evaluate Self Health

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Filter Persist

- **Tipo:** `n8n-nodes-base.filter`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Filter Meta

- **Tipo:** `n8n-nodes-base.filter`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Filter Notify

- **Tipo:** `n8n-nodes-base.filter`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Persist State

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Update Meta

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Is Break Glass?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Generate Break-Glass HMAC

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Break-Glass to Hermes

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.
### Manual Trigger

- **Tipo:** `n8n-nodes-base.manualTrigger`
- **Versão:** `1`
- **Finalidade:** node do fluxo `18 - OMEAB SELF HEALTH`.


## Code nodes

### Code: Build Exec Targets

- Linguagem: js
- Linhas: 24
- Caminhos absolutos detectados: False
- URLs privadas no código: True
- Prévia sanitizada:

```javascript

const REGISTRY = {"version":"1.0","updated_at":"2026-09-15","notes":"Intent registry for OMEAB Self Health. expected_state reflects architectural INTENT, not only live active flag. 16/17 are known hardware/docs limitations — never incidents.","defaults":{"grace_factor":2.5,"failure_streak_warn":2,"failure_streak_error":3,"schedule_minutes":5},"workflows":[{"slug":"00-hestia-event-bus","workflow_id":"q3NtPXnyj8ahrZE4","name":"00 - HESTIA EVENT BUS","expected_state":"active","architectural_status
```
### Code: Attach Exec Meta

- Linguagem: js
- Linhas: 22
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const ctx = $('Build Exec Targets').item.json || {};
const body = $json || {};
let executions = [];
if (Array.isArray(body.data)) executions = body.data;
else if (body.data && Array.isArray(body.data.data)) executions = body.data.data;
const forbidden = String(body.message || '').toLowerCase().includes('forbidden') || body.statusCode === 403;
return {
  json: {
    workflow_id: ctx.workflow_id,
    target: ctx.target,
    registry: ctx.registry,
    workflows: ctx.workflows,
    workflowsOk: ctx
```
### Code: Evaluate Self Health

- Linguagem: js
- Linhas: 285
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript

function severityFor(criticality, event) {
  const crit = (criticality || 'medium').toLowerCase();
  if (event === 'event_bus_unavailable') return 'critical';
  const mapInactive = { critical: 'error', high: 'error', medium: 'warning', low: 'warning' };
  const mapOverdue = { critical: 'error', high: 'error', medium: 'warning', low: 'info' };
  if (event === 'workflow_unexpectedly_inactive') return mapInactive[crit] || 'warning';
  if (event === 'workflow_execution_overdue') return mapOverdue[c
```
### Code: Generate Break-Glass HMAC

- Linguagem: js
- Linhas: 8
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const crypto = require('crypto');
const event = $json;
const secret = $env.HESTIA_WEBHOOK_SECRET;
if (!secret) return [{ json: { ...event, break_glass_error: 'HESTIA_WEBHOOK_SECRET missing', skip_break_glass: true } }];
const body = JSON.stringify({ alert: { text: '[BREAK_GLASS_ONLY] ' + (event.alert?.text || event.message || 'automation chain issue') } });
const timestamp = String(Math.floor(Date.now() / 1000));
const signature = crypto.createHmac('sha256', secret).update(`${timestamp}.${body}`
```


## Dependências

### Aplicações

- credential:postgres
- docker
- hermes
- http-port:5678
- immich
- obsidian
- omeab
- postgresql
- rag
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
