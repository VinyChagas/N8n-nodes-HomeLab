# Diagramas — 03 - SERVICE DOWN ALERT

## 1. Fluxo geral

```mermaid
flowchart TD
  Webhook["Webhook\n(webhook)"]
  Normalize_Service_Event["Normalize Service Event\n(code)"]
  Get_Previous_Service_State["Get Previous Service State\n(postgres)"]
  Merge["Merge\n(merge)"]
  Decide_Service_Notification["Decide Service Notification\n(code)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Should_Notify_["Should Notify?\n(if)"]
  Webhook --> Normalize_Service_Event
  Normalize_Service_Event --> Get_Previous_Service_State
  Normalize_Service_Event --> Merge
  Get_Previous_Service_State --> Merge
  Merge --> Decide_Service_Notification
  Decide_Service_Notification --> Should_Notify_
  Should_Notify_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> omeab[omeab]
  WF --> postgresql[postgresql]
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
  This["03 - SERVICE DOWN ALERT"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
