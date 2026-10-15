# Diagramas — 06 - DAILY OMEAB REPORT

## 1. Fluxo geral

```mermaid
flowchart TD
  Daily_Schedule["Daily Schedule\n(scheduleTrigger)"]
  Get_System_Health["Get System Health\n(httpRequest)"]
  Get_Storage_Health["Get Storage Health\n(httpRequest)"]
  Get_Disk_Capacity["Get Disk Capacity\n(httpRequest)"]
  Get_Docker_Health["Get Docker Health\n(httpRequest)"]
  Get_Backup_Health["Get Backup Health\n(httpRequest)"]
  Get_Last_24h_Events["Get Last 24h Events\n(postgres)"]
  Build_Daily_Snapshot["Build Daily Snapshot\n(code)"]
  Prepare_Daily_Message["Prepare Daily Message\n(code)"]
  Generate_HMAC["Generate HMAC\n(code)"]
  Send_Daily_Report_to_Hestia["Send Daily Report to Hestia\n(httpRequest)"]
  Daily_Schedule --> Get_System_Health
  Get_System_Health --> Get_Storage_Health
  Get_Storage_Health --> Get_Disk_Capacity
  Get_Disk_Capacity --> Get_Docker_Health
  Get_Docker_Health --> Get_Backup_Health
  Get_Backup_Health --> Get_Last_24h_Events
  Get_Last_24h_Events --> Build_Daily_Snapshot
  Build_Daily_Snapshot --> Prepare_Daily_Message
  Prepare_Daily_Message --> Generate_HMAC
  Generate_HMAC --> Send_Daily_Report_to_Hestia
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
  This["06 - DAILY OMEAB REPORT"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
