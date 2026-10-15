# Técnica — 20 - INCIDENT CORRELATION ENGINE

## Visão geral

- **Nodes:** 6
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.manualTrigger`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** nenhuma tipada no export
- **Integrações detectadas:** incident
- **Webhooks:** []
- **Schedules:** `[{"node": "Every 1 Minute", "rule": {"interval": [{"field": "minutes", "minutesInterval": 1}]}}]`
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

- `POST` `{{$env.OMEAB_SERVICE_URL}}/v1/process` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Every 1 Minute

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.2`
- **Finalidade:** node do fluxo `20 - INCIDENT CORRELATION ENGINE`.
### Manual Trigger

- **Tipo:** `n8n-nodes-base.manualTrigger`
- **Versão:** `1`
- **Finalidade:** node do fluxo `20 - INCIDENT CORRELATION ENGINE`.
### Run Correlation Process

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.2`
- **Finalidade:** node do fluxo `20 - INCIDENT CORRELATION ENGINE`.
### Expand Notifications

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `20 - INCIDENT CORRELATION ENGINE`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.2`
- **Finalidade:** node do fluxo `20 - INCIDENT CORRELATION ENGINE`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.2`
- **Finalidade:** node do fluxo `20 - INCIDENT CORRELATION ENGINE`.


## Code nodes

### Code: Expand Notifications

- Linguagem: js
- Linhas: 26
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const data = $input.first().json || {};
const notes = Array.isArray(data.notifications) ? data.notifications : [];
if (!notes.length) {
  return [{ json: { should_notify: false, skip: true, meta: {
    processed_events: data.processed_events || 0,
    ignored_events: data.ignored_events || 0,
    lock_acquired: data.lock_acquired,
    bootstrap: data.bootstrap,
    execution_time_ms: data.execution_time_ms,
  }}}];
}
return notes.map((ev) => ({
  json: {
    should_notify: true,
    source: ev.s
```


## Dependências

### Aplicações

- incident

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
