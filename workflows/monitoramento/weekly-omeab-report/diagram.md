# Diagramas — 07 - WEEKLY OMEAB REPORT

## 1. Fluxo geral

```mermaid
flowchart TD
  Weekly_Schedule["Weekly Schedule\n(scheduleTrigger)"]
  Get_System["Get System\n(httpRequest)"]
  Get_Storage["Get Storage\n(httpRequest)"]
  Get_Disk_Capacity["Get Disk Capacity\n(httpRequest)"]
  Get_Docker["Get Docker\n(httpRequest)"]
  Get_Backups["Get Backups\n(httpRequest)"]
  Get_Current_Week_Events["Get Current Week Events\n(postgres)"]
  Get_Previous_Week_Events["Get Previous Week Events\n(postgres)"]
  Get_Capacity_History["Get Capacity History\n(postgres)"]
  Build_Weekly_Snapshot["Build Weekly Snapshot\n(code)"]
  Prepare_Weekly_Message["Prepare Weekly Message\n(code)"]
  Prepare_Capacity_Persist["Prepare Capacity Persist\n(code)"]
  Store_Capacity_Snapshot["Store Capacity Snapshot\n(postgres)"]
  Restore_Snapshot_Context["Restore Snapshot Context\n(code)"]
  Generate_HMAC["Generate HMAC\n(code)"]
  Send_Weekly_Report_to_Hestia["Send Weekly Report to Hestia\n(httpRequest)"]
  Weekly_Schedule --> Get_System
  Get_System --> Get_Storage
  Get_Storage --> Get_Disk_Capacity
  Get_Disk_Capacity --> Get_Docker
  Get_Docker --> Get_Backups
  Get_Backups --> Get_Current_Week_Events
  Get_Current_Week_Events --> Get_Previous_Week_Events
  Get_Previous_Week_Events --> Get_Capacity_History
  Get_Capacity_History --> Build_Weekly_Snapshot
  Build_Weekly_Snapshot --> Prepare_Weekly_Message
  Prepare_Weekly_Message --> Prepare_Capacity_Persist
  Prepare_Capacity_Persist --> Store_Capacity_Snapshot
  Store_Capacity_Snapshot --> Restore_Snapshot_Context
  Restore_Snapshot_Context --> Generate_HMAC
  Generate_HMAC --> Send_Weekly_Report_to_Hestia
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> docker[docker]
  WF --> hermes[hermes]
  WF --> omeab[omeab]
  WF --> postgres[postgres]
  WF --> postgresql[postgresql]
  WF --> rag[rag]
  WF --> restic[restic]
  WF --> telegram[telegram]
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
  This["07 - WEEKLY OMEAB REPORT"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
