# Técnica — 15 - STORAGE CLEANUP ADVISOR

## Visão geral

- **Nodes:** 10
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, postgresql, rag
- **Webhooks:** []
- **Schedules:** `[{"node": "Daily Schedule", "rule": {"interval": [{"field": "cronExpression", "expression": "0 7 * * *"}]}}]`
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

- `GET` `{{$env.SERVICE_BASE_URL}}/v1/storage-analysis` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Daily Schedule

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Get Storage Analysis

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Get Previous Snapshot

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Get Advisor Meta

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Wait Context

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Evaluate Growth And Dedup

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Persist Snapshot

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Upsert Meta

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `1`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `15 - STORAGE CLEANUP ADVISOR`.


## Code nodes

### Code: Evaluate Growth And Dedup

- Linguagem: js
- Linhas: 154
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
function safe(name) {
  try { return $(name).first().json || {}; } catch (e) { return { _error: true, _message: String(e.message || e) }; }
}

const analysis = safe('Get Storage Analysis');
const prev = safe('Get Previous Snapshot');
const meta = safe('Get Advisor Meta');
const now = new Date().toISOString();

if (analysis._error || !analysis.checked_at) {
  return [{
    json: {
      should_emit: false,
      skip_persist: true,
      error: analysis._message || 'storage_analysis_unavailable',
```


## Dependências

### Aplicações

- credential:postgres
- postgresql
- rag

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
