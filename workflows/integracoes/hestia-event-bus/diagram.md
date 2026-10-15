# Diagramas — 00 - HESTIA EVENT BUS

## 1. Fluxo geral

```mermaid
flowchart TD
  Webhook["Webhook\n(webhook)"]
  Normalize_Event["Normalize Event\n(code)"]
  Route_by_Severity["Route by Severity\n(switch)"]
  Persist_Event["Persist Event\n(postgres)"]
  Prepare_Alert["Prepare Alert\n(code)"]
  Generate_HMAC["Generate HMAC\n(code)"]
  Send_to_Hestia["Send to Hestia\n(httpRequest)"]
  Webhook --> Normalize_Event
  Normalize_Event --> Route_by_Severity
  Route_by_Severity --> Persist_Event
  Route_by_Severity --> Persist_Event
  Route_by_Severity --> Persist_Event
  Route_by_Severity --> Prepare_Alert
  Route_by_Severity --> Persist_Event
  Route_by_Severity --> Prepare_Alert
  Prepare_Alert --> Generate_HMAC
  Generate_HMAC --> Send_to_Hestia
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> hermes[hermes]
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
  This["00 - HESTIA EVENT BUS"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
