# Técnica — 05 - DISK CAPACITY

## Visão geral

- **Nodes:** 8
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, postgresql, rag
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

- `GET` `{{$env.SERVICE_BASE_URL}}/v1/disk-capacity` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Schedule Trigger

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.
### Get Disk Capacity

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.
### Evaluate Filesystems

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.
### Get Previous Filesystem State

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.
### Merge State

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.
### Decide Notification

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.3`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `05 - DISK CAPACITY`.


## Code nodes

### Code: Evaluate Filesystems

- Linguagem: js
- Linhas: 164
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const payload = $json;
const filesystems = Array.isArray(payload.filesystems) ? payload.filesystems : [];
const timestamp = payload.timestamp ?? new Date().toISOString();
const summary = payload.summary ?? {};

// Limiares: preferir os do Health Agent (fonte única em disk_capacity.py).
// Fallback local apenas se o agent não enviar thresholds.
const THRESHOLDS = payload.thresholds ?? {
  warning: 70,
  error: 85,
  critical: 95,
};

function formatFree(bytes) {
  const n = Number(bytes);
  if (!
```
### Code: Decide Notification

- Linguagem: js
- Linhas: 159
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const allItems = $input.all();
const results = [];

const severityRank = {
  info: 1,
  warning: 2,
  error: 3,
  critical: 4,
};

const capacityRank = {
  normal: 0,
  warning: 1,
  error: 2,
  critical: 3,
  unknown: 2,
};

// Decisão de downgrade:
// CRITICAL→ERROR ou ERROR→WARNING NÃO gera notificação (silencioso).
// Motivo: evitar spam por oscilação pequena entre faixas altas.
// Só notifica recuperação completa (qualquer faixa → normal) ou escalada.
const NOTIFY_ON_DEESCALATION = false;


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
