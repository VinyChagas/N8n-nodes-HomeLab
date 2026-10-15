# Diagramas — 11 - MEDIA AUTOMATION

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Scan_Media_Inbox["Scan Media Inbox\n(httpRequest)"]
  Process_Queue["Process Queue\n(httpRequest)"]
  Get_Pending_Events["Get Pending Events\n(httpRequest)"]
  Prepare_Media_Events["Prepare Media Events\n(code)"]
  Has_Events_["Has Events?\n(if)"]
  Hestia_Event_Bus["Hestia Event Bus\n(httpRequest)"]
  Ack_Events["Ack Events\n(httpRequest)"]
  Schedule_Trigger --> Scan_Media_Inbox
  Scan_Media_Inbox --> Process_Queue
  Process_Queue --> Get_Pending_Events
  Get_Pending_Events --> Prepare_Media_Events
  Prepare_Media_Events --> Has_Events_
  Has_Events_ --> Hestia_Event_Bus
  Hestia_Event_Bus --> Ack_Events
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> media_manager[media-manager]
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
  This["11 - MEDIA AUTOMATION"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
