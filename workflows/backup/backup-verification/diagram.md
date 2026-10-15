# Diagramas — 02 - BACKUP VERIFICATION

## 1. Fluxo geral

```mermaid
flowchart TD
  Check_Backups["Check Backups\n(scheduleTrigger)"]
  HTTP_Request["HTTP Request\n(httpRequest)"]
  Evaluate_Backups["Evaluate Backups\n(code)"]
  Get_Previous_Backup_State["Get Previous Backup State\n(postgres)"]
  Merge_Backup_State["Merge Backup State\n(merge)"]
  Decide_Backup_Notification["Decide Backup Notification\n(code)"]
  Should_Notify_["Should Notify?\n(if)"]
  Send_to_Hestia_Event_Bus["Send to Hestia Event Bus\n(httpRequest)"]
  Check_Backups --> HTTP_Request
  HTTP_Request --> Evaluate_Backups
  Evaluate_Backups --> Get_Previous_Backup_State
  Evaluate_Backups --> Merge_Backup_State
  Get_Previous_Backup_State --> Merge_Backup_State
  Merge_Backup_State --> Decide_Backup_Notification
  Decide_Backup_Notification --> Should_Notify_
  Should_Notify_ --> Send_to_Hestia_Event_Bus
```

## 2. Integrações externas

```mermaid
flowchart LR
  WF[Workflow]
  WF --> credential_postgres[credential:postgres]
  WF --> omeab[omeab]
  WF --> postgres[postgres]
  WF --> postgresql[postgresql]
  WF --> restic[restic]
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
  This["02 - BACKUP VERIFICATION"] -->|"eventos"| EB["00 - HESTIA EVENT BUS"]
  EB --> Hermes[Hermes/Hestia]
```
