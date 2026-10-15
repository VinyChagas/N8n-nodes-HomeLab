# Diagramas — 09 - OBSIDIAN INGESTION

## 1. Fluxo geral

```mermaid
flowchart TD
  Schedule_Trigger["Schedule Trigger\n(scheduleTrigger)"]
  Call_Obsidian_Scan["Call Obsidian Scan\n(httpRequest)"]
  Prepare_Obsidian_Events["Prepare Obsidian Events\n(code)"]
  Has_Relevant_Changes_["Has Relevant Changes?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Schedule_Trigger --> Call_Obsidian_Scan
  Call_Obsidian_Scan --> Prepare_Obsidian_Events
  Prepare_Obsidian_Events --> Has_Relevant_Changes_
  Has_Relevant_Changes_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> obsidian[obsidian]
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
  This["09 - OBSIDIAN INGESTION"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
