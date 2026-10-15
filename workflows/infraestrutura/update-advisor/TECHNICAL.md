# Técnica — 14 - UPDATE ADVISOR

## Visão geral

- **Nodes:** 17
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`, `n8n-nodes-base.switch`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, docker, immich, postgres, postgresql, rag, update-advisor
- **Webhooks:** []
- **Schedules:** `[{"node": "Daily Schedule", "rule": {"interval": [{"field": "cronExpression", "expression": "30 6 * * *"}]}}]`
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

- `GET` `{{$env.SERVICE_BASE_URL}}/v1/backups` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/storage` (URL privada original → placeholder)
- `GET` `{{$env.SERVICE_BASE_URL}}/v1/docker` (URL privada original → placeholder)
- `POST` `{{$env.OMEAB_SERVICE_URL}}/v1/evaluate` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Daily Schedule

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Get Backup Status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Get Storage Status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Get Docker Status

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Get Postgres Version

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Get Immich Status

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Get Previous States

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Get Advisor Meta

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Wait All Context

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Build Evaluate Request

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Call Update Advisor

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Prepare Persist And Events

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Route Outputs

- **Tipo:** `n8n-nodes-base.switch`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Persist State

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Upsert Meta

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Should Emit Event?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `1`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `14 - UPDATE ADVISOR`.


## Code nodes

### Code: Build Evaluate Request

- Linguagem: js
- Linhas: 52
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
function safe(name) {
  try { return $(name).first().json || {}; } catch (e) { return { _error: true, _message: String(e.message || e) }; }
}

const backup = safe('Get Backup Status');
const storage = safe('Get Storage Status');
const docker = safe('Get Docker Status');
const pg = safe('Get Postgres Version');
const immich = safe('Get Immich Status');
const prevRows = (() => { try { return $('Get Previous States').all().map(i => i.json).filter(Boolean); } catch (e) { return []; } })();
const met
```
### Code: Prepare Persist And Events

- Linguagem: js
- Linhas: 73
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const result = $('Call Update Advisor').first().json || {};
const components = Array.isArray(result.components) ? result.components : [];
const events = Array.isArray(result.events) ? result.events : [];
const metaUpdates = result.meta_updates || {};
const now = new Date().toISOString();

const persistItems = components.map((c) => ({
  json: {
    kind: 'persist',
    checked_at: now,
    component: c.component,
    installed_version: c.installed_version ?? null,
    available_version: c.availab
```


## Dependências

### Aplicações

- credential:postgres
- docker
- immich
- postgres
- postgresql
- rag
- update-advisor

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
