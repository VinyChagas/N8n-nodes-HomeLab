# Técnica — 02 - BACKUP VERIFICATION

## Visão geral

- **Nodes:** 8
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.if`, `n8n-nodes-base.merge`, `n8n-nodes-base.postgres`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** postgres
- **Integrações detectadas:** credential:postgres, omeab, postgres, postgresql, restic
- **Webhooks:** []
- **Schedules:** `[{"node": "Check Backups", "rule": {"interval": [{"field": "hours"}]}}]`
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

- `GET` `{{$env.SERVICE_BASE_URL}}/v1/backups` (URL privada original → placeholder)
- `POST` `http://n8n:5678/webhook/hestia-event`

## Nodes

### Check Backups

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.3`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.
### HTTP Request

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.
### Evaluate Backups

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.
### Get Previous Backup State

- **Tipo:** `n8n-nodes-base.postgres`
- **Versão:** `2.6`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.
### Merge Backup State

- **Tipo:** `n8n-nodes-base.merge`
- **Versão:** `3.2`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.
### Decide Backup Notification

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.
### Should Notify?

- **Tipo:** `n8n-nodes-base.if`
- **Versão:** `2.3`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.
### Send to Hestia Event Bus

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.4`
- **Finalidade:** node do fluxo `02 - BACKUP VERIFICATION`.


## Code nodes

### Code: Evaluate Backups

- Linguagem: js
- Linhas: 101
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const data = $json;

const problems = [];

// PostgreSQL
for (const [database, backup] of Object.entries(data.postgres ?? {})) {
  if (backup.status !== 'ok') {
    problems.push({
      component: `postgres.${database}`,
      status: backup.status ?? 'unknown',
      message: `Backup PostgreSQL de ${database} está com status ${backup.status ?? 'unknown'}.`,
      details: backup
    });
  }
}

// Restic
if (data.restic?.status !== 'ok') {
  problems.push({
    component: 'restic',
    status: 
```
### Code: Decide Backup Notification

- Linguagem: js
- Linhas: 105
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

// 1. PRIMEIRO INCIDENTE
if (
  previousEvent === null &&
  data.should_emit === true
) {
  shouldNotify = true;
  reason = 'first_incident';
}

// 2. RECUPERAÇÃO
if (
  data.event === 'backup_healthy' &&
  previousEvent !== null &&
  previousStatus !== 'healthy'

```


## Dependências

### Aplicações

- credential:postgres
- omeab
- postgres
- postgresql
- restic

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
