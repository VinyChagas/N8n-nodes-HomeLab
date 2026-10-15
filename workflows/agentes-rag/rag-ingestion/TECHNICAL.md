# Técnica — 08 - RAG INGESTION

## Visão geral

- **Nodes:** 5
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** nenhuma tipada no export
- **Integrações detectadas:** rag
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

- `POST` `{{$env.OMEAB_SERVICE_URL}}/scan` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `08 - RAG INGESTION`.
### Call RAG Scan

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `08 - RAG INGESTION`.
### Prepare RAG Events

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `08 - RAG INGESTION`.
### Should Emit Event?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `1`
- **Finalidade:** node do fluxo `08 - RAG INGESTION`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `08 - RAG INGESTION`.


## Code nodes

### Code: Prepare RAG Events

- Linguagem: js
- Linhas: 80
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const scan = $json;
const now = new Date().toISOString();
const items = [];

const results = Array.isArray(scan.results) ? scan.results : [];
for (const r of results) {
  if (r.status === 'indexed') {
    items.push({
      json: {
        should_emit: true,
        source: 'rag_ingestion',
        severity: 'info',
        component: 'knowledge',
        event: 'document_indexed',
        status: 'completed',
        timestamp: now,
        message: 'Documento indexado no RAG.',
        require
```


## Dependências

### Aplicações

- rag

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
