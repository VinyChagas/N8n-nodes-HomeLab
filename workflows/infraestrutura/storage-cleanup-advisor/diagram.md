# Diagramas — 15 - STORAGE CLEANUP ADVISOR

## 1. Fluxo geral

```mermaid
flowchart TD
  Daily_Schedule["Daily Schedule\n(scheduleTrigger)"]
  Get_Storage_Analysis["Get Storage Analysis\n(httpRequest)"]
  Get_Previous_Snapshot["Get Previous Snapshot\n(postgres)"]
  Get_Advisor_Meta["Get Advisor Meta\n(postgres)"]
  Wait_Context["Wait Context\n(merge)"]
  Evaluate_Growth_And_Dedup["Evaluate Growth And Dedup\n(code)"]
  Persist_Snapshot["Persist Snapshot\n(postgres)"]
  Upsert_Meta["Upsert Meta\n(postgres)"]
  Should_Notify_["Should Notify?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Daily_Schedule --> Get_Storage_Analysis
  Daily_Schedule --> Get_Previous_Snapshot
  Daily_Schedule --> Get_Advisor_Meta
  Get_Storage_Analysis --> Wait_Context
  Get_Previous_Snapshot --> Wait_Context
  Get_Advisor_Meta --> Wait_Context
  Wait_Context --> Evaluate_Growth_And_Dedup
  Evaluate_Growth_And_Dedup --> Persist_Snapshot
  Evaluate_Growth_And_Dedup --> Upsert_Meta
  Evaluate_Growth_And_Dedup --> Should_Notify_
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
  This["15 - STORAGE CLEANUP ADVISOR"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
