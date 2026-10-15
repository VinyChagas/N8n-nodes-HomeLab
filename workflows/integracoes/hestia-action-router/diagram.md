# Diagramas — 13 - HESTIA ACTION ROUTER

## 1. Fluxo geral

```mermaid
flowchart TD
  Webhook["Webhook\n(webhook)"]
  Rate_Limit_Check["Rate Limit Check\n(postgres)"]
  Auth_Validate_Policy["Auth Validate Policy\n(code)"]
  Should_Execute_["Should Execute?\n(if)"]
  Audit_Reject["Audit Reject\n(postgres)"]
  Respond_Reject["Respond Reject\n(respondToWebhook)"]
  Security_Dedup_Check["Security Dedup Check\n(postgres)"]
  Reserve_Request["Reserve Request\n(postgres)"]
  Replay_Gate["Replay Gate\n(code)"]
  Not_Replay_["Not Replay?\n(if)"]
  Resolve_Action["Resolve Action\n(switch)"]
  Exec_system_status["Exec system.status\n(httpRequest)"]
  Exec_storage_status["Exec storage.status\n(httpRequest)"]
  Exec_backup_status["Exec backup.status\n(httpRequest)"]
  Exec_docker_status["Exec docker.status\n(httpRequest)"]
  Exec_disk_status["Exec disk.status\n(httpRequest)"]
  Exec_rag_stats["Exec rag.stats\n(httpRequest)"]
  Exec_audiobook_stats["Exec audiobook.stats\n(httpRequest)"]
  Exec_media_stats["Exec media.stats\n(httpRequest)"]
  Exec_immich_status["Exec immich.status\n(postgres)"]
  Exec_Fallback["Exec Fallback\n(code)"]
  Sanitize_Result["Sanitize Result\n(code)"]
  Audit_Update["Audit Update\n(postgres)"]
  Respond_Success["Respond Success\n(respondToWebhook)"]
  Respond_Replay["Respond Replay\n(respondToWebhook)"]
  Prepare_Security_Event["Prepare Security Event\n(code)"]
  Should_Emit_Security_["Should Emit Security?\n(if)"]
  Emit_Security_Event["Emit Security Event\n(httpRequest)"]
  Replay_Security_Dedup["Replay Security Dedup\n(postgres)"]
  Prepare_Replay_Security["Prepare Replay Security\n(code)"]
  Emit_Replay_Security_["Emit Replay Security?\n(if)"]
  Emit_Replay_Security_Event["Emit Replay Security Event\n(httpRequest)"]
  Webhook --> Rate_Limit_Check
  Rate_Limit_Check --> Auth_Validate_Policy
  Auth_Validate_Policy --> Should_Execute_
  Should_Execute_ --> Reserve_Request
  Should_Execute_ --> Audit_Reject
  Reserve_Request --> Replay_Gate
  Replay_Gate --> Not_Replay_
  Not_Replay_ --> Resolve_Action
  Not_Replay_ --> Replay_Security_Dedup
  Resolve_Action --> Exec_system_status
  Resolve_Action --> Exec_storage_status
  Resolve_Action --> Exec_backup_status
  Resolve_Action --> Exec_docker_status
  Resolve_Action --> Exec_disk_status
  Resolve_Action --> Exec_immich_status
  Resolve_Action --> Exec_rag_stats
  Resolve_Action --> Exec_audiobook_stats
  Resolve_Action --> Exec_media_stats
  Resolve_Action --> Exec_Fallback
  Exec_system_status --> Sanitize_Result
  Exec_storage_status --> Sanitize_Result
  Exec_backup_status --> Sanitize_Result
  Exec_docker_status --> Sanitize_Result
  Exec_disk_status --> Sanitize_Result
  Exec_immich_status --> Sanitize_Result
  Exec_rag_stats --> Sanitize_Result
  Exec_audiobook_stats --> Sanitize_Result
  Exec_media_stats --> Sanitize_Result
  Exec_Fallback --> Sanitize_Result
  Sanitize_Result --> Audit_Update
  Audit_Update --> Respond_Success
  Audit_Reject --> Security_Dedup_Check
  Security_Dedup_Check --> Prepare_Security_Event
  Prepare_Security_Event --> Should_Emit_Security_
  Should_Emit_Security_ --> Emit_Security_Event
  Should_Emit_Security_ --> Respond_Reject
  Emit_Security_Event --> Respond_Reject
  Replay_Security_Dedup --> Prepare_Replay_Security
  Prepare_Replay_Security --> Emit_Replay_Security_
  Emit_Replay_Security_ --> Emit_Replay_Security_Event
  Emit_Replay_Security_ --> Respond_Replay
  Emit_Replay_Security_Event --> Respond_Replay
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> audiobook[audiobook]
  WF --> credential_postgres[credential:postgres]
  WF --> docker[docker]
  WF --> immich[immich]
  WF --> media_manager[media-manager]
  WF --> omeab[omeab]
  WF --> postgres[postgres]
  WF --> postgresql[postgresql]
  WF --> rag[rag]
  WF --> restic[restic]
```

## 3. Tratamento de erros / decisão

```mermaid
flowchart TD
  Input[Entrada] --> Eval[Avaliação Code/HTTP]
  Eval --> Decision{Decisão If/Filter/Switch}
  Decision -->|sem mudança / ignore| EndSilent[Fim silencioso]
  Decision -->|notificar| Notify[Event Bus / Hermes]
  Decision -->|persistir| DB[(Postgres)]
  DB --> Notify
```

> Diagrama 3 é o padrão recorrente OMEAB; o grafo real está no diagrama 1.

## 4. Dependências entre workflows (visão local)

```mermaid
flowchart LR
  This["13 - HESTIA ACTION ROUTER"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
