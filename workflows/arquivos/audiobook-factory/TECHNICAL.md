# Técnica — 10 - AUDIOBOOK FACTORY

## Visão geral

- **Nodes:** 8
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** nenhuma tipada no export
- **Integrações detectadas:** audiobook
- **Webhooks:** []
- **Schedules:** `[{"node": "Schedule Trigger", "rule": {"interval": [{"field": "minutes", "minutesInterval": 15}]}}]`
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

- `POST` `http://audiobook-factory:8080/scan`
- `POST` `http://audiobook-factory:8080/process-queue`
- `GET` `http://audiobook-factory:8080/events/pending`
- `POST` `http://n8n:5678/webhook/hestia-event`
- `POST` `http://audiobook-factory:8080/events/ack`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.
### Scan Audiobook Inbox

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.
### Start Jobs Async

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.
### Fetch Pending Events

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.
### Prepare Event

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.
### Has Events?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `1`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.
### Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.
### Ack Events

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `10 - AUDIOBOOK FACTORY`.


## Code nodes

### Code: Prepare Event

- Linguagem: js
- Linhas: 61
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const scan = $('Scan Audiobook Inbox').first().json || {};
const queue = $('Start Jobs Async').first().json || {};
const pending = $json || {};
const now = new Date().toISOString();
const items = [];

const events = Array.isArray(pending.events) ? pending.events : [];
for (const ev of events) {
  items.push({
    json: {
      should_emit: true,
      source: ev.source || 'audiobook_factory',
      severity: ev.severity || 'info',
      component: ev.component || 'audiobook',
      event: ev.eve
```


## Dependências

### Aplicações

- audiobook

### Credenciais a recriar

- Nenhuma

### Variáveis de ambiente esperadas (placeholders)

- `SERVICE_BASE_URL`
- `OMEAB_SERVICE_URL`
- `HERMES_URL`
- `HESTIA_WEBHOOK_SECRET` / `HESTIA_ACTION_SECRET` (quando aplicável)
- `AUTH_TOKEN` / `SECRET` (genéricos após sanitização)

## Segurança do código

Não foram embutidos valores de segredos no template público. Secrets devem viver em `$env` ou credenciais n8n.
