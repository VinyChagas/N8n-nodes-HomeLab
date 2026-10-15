# Técnica — 11 - MEDIA AUTOMATION

## Visão geral

- **Nodes:** 8
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** nenhuma tipada no export
- **Integrações detectadas:** media-manager
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

- `POST` `{{$env.OMEAB_SERVICE_URL}}/scan` (URL privada original → placeholder)
- `POST` `{{$env.OMEAB_SERVICE_URL}}/process-queue` (URL privada original → placeholder)
- `GET` `{{$env.OMEAB_SERVICE_URL}}/events/pending` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`
- `POST` `{{$env.OMEAB_SERVICE_URL}}/events/ack` (URL privada original → placeholder)

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.
### Scan Media Inbox

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.
### Process Queue

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.
### Get Pending Events

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.
### Prepare Media Events

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.
### Has Events?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `1`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.
### Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.
### Ack Events

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `11 - MEDIA AUTOMATION`.


## Code nodes

### Code: Prepare Media Events

- Linguagem: js
- Linhas: 66
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const scan = $('Scan Media Inbox').first().json || {};
const queue = $('Process Queue').first().json || {};
const pending = $json || {};
const now = new Date().toISOString();
const items = [];

const events = Array.isArray(pending.events) ? pending.events : [];
for (const ev of events) {
  items.push({
    json: {
      should_emit: true,
      source: ev.source || 'media_automation',
      severity: ev.severity || 'info',
      component: ev.component || 'media',
      event: ev.event,
      st
```


## Dependências

### Aplicações

- media-manager

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
