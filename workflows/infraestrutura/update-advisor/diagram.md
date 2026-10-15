# Diagramas — 14 - UPDATE ADVISOR

## 1. Fluxo geral

```mermaid
flowchart TD
  Daily_Schedule["Daily Schedule\n(scheduleTrigger)"]
  Get_Backup_Status["Get Backup Status\n(httpRequest)"]
  Get_Storage_Status["Get Storage Status\n(httpRequest)"]
  Get_Docker_Status["Get Docker Status\n(httpRequest)"]
  Get_Postgres_Version["Get Postgres Version\n(postgres)"]
  Get_Immich_Status["Get Immich Status\n(postgres)"]
  Get_Previous_States["Get Previous States\n(postgres)"]
  Get_Advisor_Meta["Get Advisor Meta\n(postgres)"]
  Wait_All_Context["Wait All Context\n(merge)"]
  Build_Evaluate_Request["Build Evaluate Request\n(code)"]
  Call_Update_Advisor["Call Update Advisor\n(httpRequest)"]
  Prepare_Persist_And_Events["Prepare Persist And Events\n(code)"]
  Route_Outputs["Route Outputs\n(switch)"]
  Persist_State["Persist State\n(postgres)"]
  Upsert_Meta["Upsert Meta\n(postgres)"]
  Should_Emit_Event_["Should Emit Event?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Daily_Schedule --> Get_Backup_Status
  Daily_Schedule --> Get_Storage_Status
  Daily_Schedule --> Get_Docker_Status
  Daily_Schedule --> Get_Postgres_Version
  Daily_Schedule --> Get_Immich_Status
  Daily_Schedule --> Get_Previous_States
  Daily_Schedule --> Get_Advisor_Meta
  Get_Backup_Status --> Wait_All_Context
  Get_Storage_Status --> Wait_All_Context
  Get_Docker_Status --> Wait_All_Context
  Get_Postgres_Version --> Wait_All_Context
  Get_Immich_Status --> Wait_All_Context
  Get_Previous_States --> Wait_All_Context
  Get_Advisor_Meta --> Wait_All_Context
  Wait_All_Context --> Build_Evaluate_Request
  Build_Evaluate_Request --> Call_Update_Advisor
  Call_Update_Advisor --> Prepare_Persist_And_Events
  Prepare_Persist_And_Events --> Route_Outputs
  Route_Outputs --> Persist_State
  Route_Outputs --> Upsert_Meta
  Route_Outputs --> Should_Emit_Event_
  Should_Emit_Event_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> docker[docker]
  WF --> immich[immich]
  WF --> postgres[postgres]
  WF --> postgresql[postgresql]
  WF --> rag[rag]
  WF --> update_advisor[update-advisor]
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
  This["14 - UPDATE ADVISOR"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
