# Diagramas — 18 - OMEAB SELF HEALTH

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Get_Health_Agent["Get Health Agent\n(httpRequest)"]
  List_n8n_Workflows["List n8n Workflows\n(httpRequest)"]
  Get_Self_Health_Meta["Get Self Health Meta\n(postgres)"]
  Merge_Inputs["Merge Inputs\n(merge)"]
  Build_Exec_Targets["Build Exec Targets\n(code)"]
  Get_Last_Executions["Get Last Executions\n(httpRequest)"]
  Attach_Exec_Meta["Attach Exec Meta\n(code)"]
  Evaluate_Self_Health["Evaluate Self Health\n(code)"]
  Filter_Persist["Filter Persist\n(filter)"]
  Filter_Meta["Filter Meta\n(filter)"]
  Filter_Notify["Filter Notify\n(filter)"]
  Persist_State["Persist State\n(postgres)"]
  Update_Meta["Update Meta\n(postgres)"]
  Is_Break_Glass_["Is Break Glass?\n(if)"]
  Generate_Break_Glass_HMAC["Generate Break-Glass HMAC\n(code)"]
  Break_Glass_to_Hermes["Break-Glass to Hermes\n(httpRequest)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Manual_Trigger["Manual Trigger\n(manualTrigger)"]
  Schedule_Trigger --> Get_Health_Agent
  Schedule_Trigger --> List_n8n_Workflows
  Schedule_Trigger --> Get_Self_Health_Meta
  Get_Health_Agent --> Merge_Inputs
  List_n8n_Workflows --> Merge_Inputs
  Get_Self_Health_Meta --> Merge_Inputs
  Merge_Inputs --> Build_Exec_Targets
  Build_Exec_Targets --> Get_Last_Executions
  Get_Last_Executions --> Attach_Exec_Meta
  Attach_Exec_Meta --> Evaluate_Self_Health
  Evaluate_Self_Health --> Filter_Persist
  Evaluate_Self_Health --> Filter_Meta
  Evaluate_Self_Health --> Filter_Notify
  Filter_Persist --> Persist_State
  Filter_Meta --> Update_Meta
  Filter_Notify --> Is_Break_Glass_
  Is_Break_Glass_ --> Generate_Break_Glass_HMAC
  Is_Break_Glass_ --> Send_to_Hestia_Event_Bus
  Generate_Break_Glass_HMAC --> Break_Glass_to_Hermes
  Manual_Trigger --> Get_Health_Agent
  Manual_Trigger --> List_n8n_Workflows
  Manual_Trigger --> Get_Self_Health_Meta
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> docker[docker]
  WF --> hermes[hermes]
  WF --> http_port_5678[http-port:5678]
  WF --> immich[immich]
  WF --> obsidian[obsidian]
  WF --> omeab[omeab]
  WF --> postgresql[postgresql]
  WF --> rag[rag]
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
  This["18 - OMEAB SELF HEALTH"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
