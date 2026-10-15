# Diagramas — 01 - Storage Guardian

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  HTTP_Request["HTTP Request\n(httpRequest)"]
  Execute_a_SQL_query["Execute a SQL query\n(postgres)"]
  Decide_Notification["Decide Notification\n(code)"]
  Evaluate_Storage["Evaluate Storage\n(code)"]
  Merge_Storage_State["Merge Storage State\n(merge)"]
  Should_Notify_["Should Notify?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Schedule_Trigger --> HTTP_Request
  HTTP_Request --> Evaluate_Storage
  Execute_a_SQL_query --> Merge_Storage_State
  Evaluate_Storage --> Execute_a_SQL_query
  Evaluate_Storage --> Merge_Storage_State
  Merge_Storage_State --> Decide_Notification
  Decide_Notification --> Should_Notify_
  Should_Notify_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> omeab[omeab]
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
  This["01 - Storage Guardian"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
