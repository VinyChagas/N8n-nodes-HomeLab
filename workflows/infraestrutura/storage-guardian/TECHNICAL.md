# Técnica — 01 - Storage Guardian

## Visão geral

- **Nodes:** 8
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, omeab, postgresql, rag
- **Webhooks:** []
- **Schedules:** `[{"node": "Schedule Trigger", "rule": {"interval": [{"field": "minutes"}]}}]`
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

- `GET` `{{$env.SERVICE_BASE_URL}}/v1/storage` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.
### HTTP Request

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.
### Execute a SQL query

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.
### Decide Notification

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.
### Evaluate Storage

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.
### Merge Storage State

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.3`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `01 - Storage Guardian`.


## Code nodes

### Code: Decide Notification

- Linguagem: js
- Linhas: 124
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const data = $json;

const previousEvent = data.previous_event ?? null;
const previousSeverity = data.previous_severity ?? null;
const previousStatus = data.previous_status ?? null;

let shouldNotify = false;
let reason = 'no_change';

// ==================================================
// 1. PRIMEIRO INCIDENTE
// ==================================================

if (
  previousEvent === null &&
  data.should_emit === true
) {
  shouldNotify = true;
  reason = 'first_incident';
}

// =======
```
### Code: Evaluate Storage

- Linguagem: js
- Linhas: 168
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const s = $json;

const errors = s.kernel_errors ?? {};

const ioErrors = Number(errors.io_error ?? 0);
const ext4Errors = Number(errors.ext4_error ?? 0);
const bufferErrors = Number(errors.buffer_io_error ?? 0);
const usbDisconnects = Number(errors.usb_disconnect ?? 0);
const usbResets = Number(errors.usb_reset ?? 0);
const remountRO = Number(errors.remount_read_only ?? 0);

let severity = 'info';
let event = 'storage_healthy';
let message = 'O storage principal do OMEAB está operando normalmen
```


## Dependências

### Aplicações

- credential:postgres
- omeab
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
