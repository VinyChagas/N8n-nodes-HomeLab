# Diagramas — 05 - DISK CAPACITY

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Get_Disk_Capacity["Get Disk Capacity\n(httpRequest)"]
  Evaluate_Filesystems["Evaluate Filesystems\n(code)"]
  Get_Previous_Filesystem_State["Get Previous Filesystem State\n(postgres)"]
  Merge_State["Merge State\n(merge)"]
  Decide_Notification["Decide Notification\n(code)"]
  Should_Notify_["Should Notify?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Schedule_Trigger --> Get_Disk_Capacity
  Get_Disk_Capacity --> Evaluate_Filesystems
  Evaluate_Filesystems --> Get_Previous_Filesystem_State
  Evaluate_Filesystems --> Merge_State
  Get_Previous_Filesystem_State --> Merge_State
  Merge_State --> Decide_Notification
  Decide_Notification --> Should_Notify_
  Should_Notify_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> postgresql[postgresql]
  WF --> rag[rag]
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
  This["05 - DISK CAPACITY"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
