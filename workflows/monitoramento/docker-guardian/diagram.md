# Diagramas — 04 - DOCKER GUARDIAN

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Get_Docker_Health["Get Docker Health\n(httpRequest)"]
  Evaluate_Docker["Evaluate Docker\n(code)"]
  Get_Previous_Docker_State["Get Previous Docker State\n(postgres)"]
  Merge_Docker_State["Merge Docker State\n(merge)"]
  Decide_Docker_Notification["Decide Docker Notification\n(code)"]
  Should_Notify_["Should Notify?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Schedule_Trigger --> Get_Docker_Health
  Get_Docker_Health --> Evaluate_Docker
  Evaluate_Docker --> Get_Previous_Docker_State
  Evaluate_Docker --> Merge_Docker_State
  Get_Previous_Docker_State --> Merge_Docker_State
  Merge_Docker_State --> Decide_Docker_Notification
  Decide_Docker_Notification --> Should_Notify_
  Should_Notify_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> docker[docker]
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
  This["04 - DOCKER GUARDIAN"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
