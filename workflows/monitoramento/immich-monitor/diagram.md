# Diagramas — 12 - IMMICH MONITOR

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Get_Immich_Jobs["Get Immich Jobs\n(httpRequest)"]
  Get_Immich_Server_Statistics["Get Immich Server Statistics\n(httpRequest)"]
  Get_Immich_Asset_Statistics["Get Immich Asset Statistics\n(httpRequest)"]
  Get_Immich_Storage["Get Immich Storage\n(httpRequest)"]
  Get_Immich_About["Get Immich About\n(httpRequest)"]
  Get_Immich_ML_Ping["Get Immich ML Ping\n(httpRequest)"]
  Build_Snapshot["Build Snapshot\n(code)"]
  Get_Previous_State["Get Previous State\n(postgres)"]
  Evaluate_Changes["Evaluate Changes\n(code)"]
  Persist_Snapshot["Persist Snapshot\n(postgres)"]
  Expand_Events["Expand Events\n(code)"]
  Should_Notify_["Should Notify?\n(if)"]
  Hestia_Event_Bus["Hestia Event Bus\n(httpRequest)"]
  Schedule_Trigger --> Get_Immich_Jobs
  Get_Immich_Jobs --> Get_Immich_Server_Statistics
  Get_Immich_Server_Statistics --> Get_Immich_Asset_Statistics
  Get_Immich_Asset_Statistics --> Get_Immich_Storage
  Get_Immich_Storage --> Get_Immich_About
  Get_Immich_About --> Get_Immich_ML_Ping
  Get_Immich_ML_Ping --> Build_Snapshot
  Build_Snapshot --> Get_Previous_State
  Get_Previous_State --> Evaluate_Changes
  Evaluate_Changes --> Persist_Snapshot
  Persist_Snapshot --> Expand_Events
  Expand_Events --> Should_Notify_
  Should_Notify_ --> Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> immich[immich]
  WF --> postgres[postgres]
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
  This["12 - IMMICH MONITOR"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
