# Diagramas — 20 - INCIDENT CORRELATION ENGINE

## 1. Fluxo geral

```mermaid
flowchart TD
  Every_1_Minute["Every 1 Minute\n(scheduleTrigger)"]
  Manual_Trigger["Manual Trigger\n(manualTrigger)"]
  Run_Correlation_Process["Run Correlation Process\n(httpRequest)"]
  Expand_Notifications["Expand Notifications\n(code)"]
  Should_Notify_["Should Notify?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Every_1_Minute --> Run_Correlation_Process
  Manual_Trigger --> Run_Correlation_Process
  Run_Correlation_Process --> Expand_Notifications
  Expand_Notifications --> Should_Notify_
  Should_Notify_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> incident[incident]
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
  This["20 - INCIDENT CORRELATION ENGINE"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
