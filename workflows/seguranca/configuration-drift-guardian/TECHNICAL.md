# Técnica — 19 - CONFIGURATION DRIFT GUARDIAN

## Visão geral

- **Nodes:** 11
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.manualTrigger`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** config-guardian, credential:postgres, omeab, postgresql
- **Webhooks:** []
- **Schedules:** `[{"node": "Every 15 Minutes", "rule": {"interval": [{"field": "minutes", "minutesInterval": 15}]}}]`
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

- `GET` `{{$env.OMEAB_SERVICE_URL}}/v1/configuration-drift` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Every 15 Minutes

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Manual Trigger

- **Tipo:** `n8n-nodes-base.manualTrigger`
- **Versão:** `1`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Get Configuration Drift

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Get Previous States

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Wait Context

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Evaluate Dedup Persist Plan

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Persist Component States

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Upsert Meta

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Expand Events

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `19 - CONFIGURATION DRIFT GUARDIAN`.


## Code nodes

### Code: Evaluate Dedup Persist Plan

- Linguagem: js
- Linhas: 185
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript

function safe(name) {
  try { return $(name).first().json || {}; } catch (e) { return { _error: true, _message: String(e.message || e) }; }
}

const driftResp = safe('Get Configuration Drift');
const prevRows = (() => {
  try {
    return $('Get Previous States').all().map(i => i.json);
  } catch (e) {
    return [];
  }
})();

const now = new Date().toISOString();
const sevMap = { low: 'info', medium: 'warning', high: 'error', critical: 'critical' };

if (driftResp._error || !driftResp.summary
```
### Code: Expand Events

- Linguagem: js
- Linhas: 7
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript

const root = $input.first().json || {};
const events = Array.isArray(root.events) ? root.events : [];
if (!events.length) {
  return [{ json: { should_emit: false } }];
}
return events.map((e) => ({ json: { should_emit: true, ...e } }));

```


## Dependências

### Aplicações

- config-guardian
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
