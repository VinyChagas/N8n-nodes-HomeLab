# Diagramas — 08 - RAG INGESTION

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Call_RAG_Scan["Call RAG Scan\n(httpRequest)"]
  Prepare_RAG_Events["Prepare RAG Events\n(code)"]
  Should_Emit_Event_["Should Emit Event?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Schedule_Trigger --> Call_RAG_Scan
  Call_RAG_Scan --> Prepare_RAG_Events
  Prepare_RAG_Events --> Should_Emit_Event_
  Should_Emit_Event_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
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
  This["08 - RAG INGESTION"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
