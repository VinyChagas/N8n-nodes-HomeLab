# Diagramas — 21 - INCIDENT NOTIFICATION MANAGER

## 1. Fluxo geral

```mermaid
flowchart TD
  Every_1_Minute["Every 1 Minute\n(scheduleTrigger)"]
  Manual_Trigger["Manual Trigger\n(manualTrigger)"]
  Run_Shadow_Evaluate["Run Shadow Evaluate\n(httpRequest)"]
  Shadow_Summary["Shadow Summary\n(code)"]
  Every_1_Minute --> Run_Shadow_Evaluate
  Manual_Trigger --> Run_Shadow_Evaluate
  Run_Shadow_Evaluate --> Shadow_Summary
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> notification[notification]
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
  This["21 - INCIDENT NOTIFICATION MANAGER"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
