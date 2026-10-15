# Diagramas — 10 - AUDIOBOOK FACTORY

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Scan_Audiobook_Inbox["Scan Audiobook Inbox\n(httpRequest)"]
  Start_Jobs_Async["Start Jobs Async\n(httpRequest)"]
  Fetch_Pending_Events["Fetch Pending Events\n(httpRequest)"]
  Prepare_Event["Prepare Event\n(code)"]
  Has_Events_["Has Events?\n(if)"]
  Hestia_Event_Bus["Hestia Event Bus\n(httpRequest)"]
  Ack_Events["Ack Events\n(httpRequest)"]
  Schedule_Trigger --> Scan_Audiobook_Inbox
  Scan_Audiobook_Inbox --> Start_Jobs_Async
  Start_Jobs_Async --> Fetch_Pending_Events
  Fetch_Pending_Events --> Prepare_Event
  Prepare_Event --> Has_Events_
  Has_Events_ --> Hestia_Event_Bus
  Hestia_Event_Bus --> Ack_Events
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> audiobook[audiobook]
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
  This["10 - AUDIOBOOK FACTORY"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
