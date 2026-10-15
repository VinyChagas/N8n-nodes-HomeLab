# Técnica — 03 - SERVICE DOWN ALERT

## Visão geral

- **Nodes:** 7
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.webhook`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, omeab, postgresql
- **Webhooks:** [{"node": "Webhook", "path": "service-status", "httpMethod": "POST"}]
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

- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Webhook

- **Tipo:** `n8n-nodes-base.webhook`
- **Versão:** `2.1`
- **Finalidade:** node do fluxo `03 - SERVICE DOWN ALERT`.
### Normalize Service Event

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `03 - SERVICE DOWN ALERT`.
### Get Previous Service State

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `03 - SERVICE DOWN ALERT`.
### Merge

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `03 - SERVICE DOWN ALERT`.
### Decide Service Notification

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `03 - SERVICE DOWN ALERT`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `03 - SERVICE DOWN ALERT`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.3`
- **Finalidade:** node do fluxo `03 - SERVICE DOWN ALERT`.


## Code nodes

### Code: Normalize Service Event

- Linguagem: js
- Linhas: 124
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const input = $json.body ?? $json;

const heartbeat = input.heartbeat ?? {};
const monitor = input.monitor ?? {};
const rawStatus = heartbeat.status;

const statusMap = {
  0: 'down',
  1: 'up',
  2: 'pending',
  3: 'maintenance',
};

const normalizedStatus = statusMap[rawStatus] ?? 'unknown';

const tagNames = Array.isArray(monitor.tags)
  ? monitor.tags
      .map(tag => String(tag.name ?? tag.value ?? '').toUpperCase())
      .filter(Boolean)
  : [];

let severity = 'warning';

if (tagNames.i
```
### Code: Decide Service Notification

- Linguagem: js
- Linhas: 84
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const data = $json;

const previousEvent = data.previous_event ?? null;
const previousSeverity = data.previous_severity ?? null;
const previousStatus = data.previous_status ?? null;

const currentEvent = data.event;
const currentSeverity = data.severity;
const currentStatus = data.status;

let shouldNotify = false;
let reason = 'no_change';

// 1. Primeiro DOWN conhecido desse serviço
if (
  currentEvent === 'service_down' &&
  previousEvent === null
) {
  shouldNotify = true;
  reason = 'first_
```


## Dependências

### Aplicações

- credential:postgres
- omeab
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
