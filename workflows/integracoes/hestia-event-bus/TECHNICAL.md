# Técnica — 00 - HESTIA EVENT BUS

## Visão geral

- **Nodes:** 7
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.postgres`, `n8n-nodes-base.switch`, `n8n-nodes-base.webhook`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, hermes, postgresql
- **Webhooks:** [{"node": "Webhook", "path": "hestia-event", "httpMethod": "POST"}]
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

- `POST` `{{$env.HERMES_URL}}`

## Nodes

### Webhook

- **Tipo:** `n8n-nodes-base.webhook`
- **Versão:** `2.1`
- **Finalidade:** node do fluxo `00 - HESTIA EVENT BUS`.
### Normalize Event

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `00 - HESTIA EVENT BUS`.
### Route by Severity

- **Tipo:** `n8n-nodes-base.switch`
- **Versão:** `3.4`
- **Finalidade:** node do fluxo `00 - HESTIA EVENT BUS`.
### Persist Event

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `00 - HESTIA EVENT BUS`.
### Prepare Alert

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `00 - HESTIA EVENT BUS`.
### Generate HMAC

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `00 - HESTIA EVENT BUS`.
### Send to Hestia

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `00 - HESTIA EVENT BUS`.


## Code nodes

### Code: Normalize Event

- Linguagem: js
- Linhas: 59
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const input = $json.body ?? $json;

const allowedSeverities = [
  'info',
  'warning',
  'error',
  'critical'
];

let severity = String(
  input.severity ?? 'info'
).toLowerCase();

if (!allowedSeverities.includes(severity)) {
  severity = 'info';
}

const now = new Date().toISOString();

const correlationId =
  input.correlation_id ??
  `${input.source ?? 'unknown'}-${Date.now()}`;

return [
  {
    json: {
      source: input.source ?? 'unknown',
      severity: severity,
      component: inp
```
### Code: Prepare Alert

- Linguagem: js
- Linhas: 43
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const event = $json;

const icons = {
  error: '🔴',
  critical: '🚨'
};

const labels = {
  error: 'ERRO',
  critical: 'CRÍTICO'
};

const severity = event.severity;

return [{
  json: {
    ...event,

    alert: {
      type: 'HESTIA_SYSTEM_ALERT',
      priority: severity === 'critical' ? 'urgent' : 'high',

      title: `${icons[severity] ?? '⚠️'} ${labels[severity] ?? severity.toUpperCase()} — ${event.component}`,

      text: [
        `${icons[severity] ?? '⚠️'} HESTIA — ${labels[severity] 
```
### Code: Generate HMAC

- Linguagem: js
- Linhas: 47
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const crypto = require('crypto');

const event = $json;

// Secret armazenado no ambiente do n8n.
// Nunca fica gravado dentro do workflow.
const secret = $env.HESTIA_WEBHOOK_SECRET;

if (!secret) {
  throw new Error('HESTIA_WEBHOOK_SECRET não está disponível no ambiente do n8n.');
}

// O Hermes espera que o body possua alert.text.
// Serializamos UMA ÚNICA VEZ.
// Esta mesma string deverá ser enviada pelo HTTP Request.
const body = JSON.stringify({
  alert: {
    text: event.alert.text
  }
});
```


## Dependências

### Aplicações

- credential:postgres
- hermes
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
