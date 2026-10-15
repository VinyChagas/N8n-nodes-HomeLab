# Diagramas — 19 - CONFIGURATION DRIFT GUARDIAN

## 1. Fluxo geral

```mermaid
flowchart TD
  Every_15_Minutes["Every 15 Minutes\n(scheduleTrigger)"]
  Manual_Trigger["Manual Trigger\n(manualTrigger)"]
  Get_Configuration_Drift["Get Configuration Drift\n(httpRequest)"]
  Get_Previous_States["Get Previous States\n(postgres)"]
  Wait_Context["Wait Context\n(merge)"]
  Evaluate_Dedup_Persist_Plan["Evaluate Dedup Persist Plan\n(code)"]
  Persist_Component_States["Persist Component States\n(postgres)"]
  Upsert_Meta["Upsert Meta\n(postgres)"]
  Expand_Events["Expand Events\n(code)"]
  Should_Notify_["Should Notify?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Every_15_Minutes --> Get_Configuration_Drift
  Every_15_Minutes --> Get_Previous_States
  Manual_Trigger --> Get_Configuration_Drift
  Manual_Trigger --> Get_Previous_States
  Get_Configuration_Drift --> Wait_Context
  Get_Previous_States --> Wait_Context
  Wait_Context --> Evaluate_Dedup_Persist_Plan
  Evaluate_Dedup_Persist_Plan --> Persist_Component_States
  Evaluate_Dedup_Persist_Plan --> Upsert_Meta
  Evaluate_Dedup_Persist_Plan --> Expand_Events
  Expand_Events --> Should_Notify_
  Should_Notify_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> config_guardian[config-guardian]
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
  This["19 - CONFIGURATION DRIFT GUARDIAN"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
