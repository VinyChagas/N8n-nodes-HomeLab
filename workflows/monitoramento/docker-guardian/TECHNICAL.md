# Técnica — 04 - DOCKER GUARDIAN

## Visão geral

- **Nodes:** 8
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, docker, postgresql
- **Webhooks:** []
- **Schedules:** `[{"node": "Schedule Trigger", "rule": {"interval": [{"field": "minutes", "minutesInterval": 2}]}}]`
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

- `GET` `{{$env.SERVICE_BASE_URL}}/v1/docker` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.
### Get Docker Health

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.
### Evaluate Docker

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.
### Get Previous Docker State

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.
### Merge Docker State

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.
### Decide Docker Notification

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.3`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `04 - DOCKER GUARDIAN`.


## Code nodes

### Code: Evaluate Docker

- Linguagem: js
- Linhas: 135
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const payload = $json;
const containers = Array.isArray(payload.containers) ? payload.containers : [];
const timestamp = payload.timestamp ?? new Date().toISOString();
const summary = payload.summary ?? {};

const items = [];

for (const c of containers) {
  if (c?.expected !== true) {
    continue;
  }

  const name = String(c.name ?? '').trim();
  if (!name) {
    continue;
  }

  const state = String(c.state ?? 'unknown').toLowerCase();
  const health = c.health == null ? null : String(c.heal
```
### Code: Decide Docker Notification

- Linguagem: js
- Linhas: 167
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const allItems = $input.all();
const results = [];

for (const item of allItems) {
  const data = item.json;

  const previousEvent = data.previous_event ?? null;
  const previousSeverity = data.previous_severity ?? null;
  const previousStatus = data.previous_status ?? null;

  let previousDetails = data.previous_details ?? null;
  if (typeof previousDetails === 'string') {
    try {
      previousDetails = JSON.parse(previousDetails);
    } catch (e) {
      previousDetails = null;
    }
  }


```


## Dependências

### Aplicações

- credential:postgres
- docker
- postgresql

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
