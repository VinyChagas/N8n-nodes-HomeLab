# Técnica — 21 - INCIDENT NOTIFICATION MANAGER

## Visão geral

- **Nodes:** 4
- **Tipos:** `n8n-nodes-base.code`, `n8n-nodes-base.httpRequest`, `n8n-nodes-base.manualTrigger`, `n8n-nodes-base.scheduleTrigger`
- **Credenciais (tipos):** nenhuma tipada no export
- **Integrações detectadas:** notification, telegram
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

- `POST` `{{$env.OMEAB_SERVICE_URL}}/v1/evaluate` (URL privada original → placeholder)

## Nodes

### Every 1 Minute

- **Tipo:** `n8n-nodes-base.scheduleTrigger`
- **Versão:** `1.2`
- **Finalidade:** node do fluxo `21 - INCIDENT NOTIFICATION MANAGER`.
### Manual Trigger

- **Tipo:** `n8n-nodes-base.manualTrigger`
- **Versão:** `1`
- **Finalidade:** node do fluxo `21 - INCIDENT NOTIFICATION MANAGER`.
### Run Shadow Evaluate

- **Tipo:** `n8n-nodes-base.httpRequest`
- **Versão:** `4.2`
- **Finalidade:** node do fluxo `21 - INCIDENT NOTIFICATION MANAGER`.
### Shadow Summary

- **Tipo:** `n8n-nodes-base.code`
- **Versão:** `2`
- **Finalidade:** node do fluxo `21 - INCIDENT NOTIFICATION MANAGER`.


## Code nodes

### Code: Shadow Summary

- Linguagem: js
- Linhas: 13
- Caminhos absolutos detectados: False
- URLs privadas no código: False
- Prévia sanitizada:

```javascript
const d=$input.first().json||{};
return [{json:{
  mode:'shadow',
  enforcement:false,
  evaluated:d.evaluated||0,
  ignored:d.ignored||0,
  decisions:Array.isArray(d.decisions)?d.decisions.length:0,
  metrics:d.metrics||{},
  bootstrap:!!d.bootstrap,
  lock_acquired:d.lock_acquired!==false,
  execution_time_ms:d.execution_time_ms||0,
  note:'Shadow Mode — no Event Bus / Telegram side effects'
}}];
```


## Dependências

### Aplicações

- notification
- telegram

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
