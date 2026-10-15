# Técnica — 09 - OBSIDIAN INGESTION

## Visão geral

- **Nodes:** 5
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** nenhuma tipada no export
- **Integrações detectadas:** obsidian, rag
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

- `POST` `{{$env.OMEAB_SERVICE_URL}}/scan/obsidian` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `09 - OBSIDIAN INGESTION`.
### Call Obsidian Scan

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `09 - OBSIDIAN INGESTION`.
### Prepare Obsidian Events

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `09 - OBSIDIAN INGESTION`.
### Has Relevant Changes?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `1`
- **Finalidade:** node do fluxo `09 - OBSIDIAN INGESTION`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `09 - OBSIDIAN INGESTION`.


## Code nodes

### Code: Prepare Obsidian Events

- Linguagem: js
- Linhas: 88
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const scan = $json;
const now = new Date().toISOString();

const scanned = Number(scan.scanned || 0);
const indexed = Number(scan.indexed || 0);
const updated = Number(scan.updated || 0);
const skipped = Number(scan.skipped || 0);
const missing = Number(scan.missing || 0);
const errors = Array.isArray(scan.errors) ? scan.errors : [];
const errorCount = errors.length;

const relevant = indexed + updated + errorCount + missing;
const hasRelevant = relevant > 0;

const items = [];

if (!hasRelevant
```


## Dependências

### Aplicações

- obsidian
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
