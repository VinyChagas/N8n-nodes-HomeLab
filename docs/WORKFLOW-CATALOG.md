# Catálogo de Workflows

Total auditado: **22**  
Templates no hub: **20**  
Bloqueados: **2**

## Tabela

| Workflow | Categoria | Objetivo | Complexidade | Reutilização |
|----------|-----------|----------|--------------|--------------|
| [00 - HESTIA EVENT BUS](../workflows/integracoes/hestia-event-bus/README.md) | Integrações e APIs | Receber eventos via webhook, persistir e encaminhar alertas relevantes | Intermediário | REQUER ADAPTAÇÃO |
| [01 - Storage Guardian](../workflows/infraestrutura/storage-guardian/README.md) | Infraestrutura e DevOps | Avaliar saúde do storage periodicamente e emitir eventos no Event Bus  | Intermediário | REQUER ADAPTAÇÃO |
| [02 - BACKUP VERIFICATION](../workflows/backup/backup-verification/README.md) | Backup e Recuperação | Detectar falhas ou degradação no status de backup e notificar via Even | Intermediário | REQUER ADAPTAÇÃO |
| [03 - SERVICE DOWN ALERT](../workflows/monitoramento/service-down-alert/README.md) | Monitoramento e Observabilidade | Normalizar status up/down e notificar mudanças significativas. | Intermediário | REQUER ADAPTAÇÃO |
| [04 - DOCKER GUARDIAN](../workflows/monitoramento/docker-guardian/README.md) | Monitoramento e Observabilidade | Detectar mudanças no estado Docker e emitir eventos deduplicados. | Intermediário | REQUER ADAPTAÇÃO |
| [05 - DISK CAPACITY](../workflows/infraestrutura/disk-capacity/README.md) | Infraestrutura e DevOps | Classificar capacidade (normal/warning/critical) e notificar mudanças. | Intermediário | REQUER ADAPTAÇÃO |
| [06 - DAILY OMEAB REPORT](../workflows/monitoramento/daily-omeab-report/README.md) | Monitoramento e Observabilidade | Agregar métricas das últimas 24h e enviar relatório assinado (HMAC). | Avançado | REQUER ADAPTAÇÃO |
| [07 - WEEKLY OMEAB REPORT](../workflows/monitoramento/weekly-omeab-report/README.md) | Monitoramento e Observabilidade | Compilar visão de 7 dias e entregar via Hermes com HMAC. | Avançado | REQUER ADAPTAÇÃO |
| [08 - RAG INGESTION](../workflows/agentes-rag/rag-ingestion/README.md) | Agentes e RAG | Disparar/orquestrar ingestão RAG e reportar resultado ao Event Bus qua | Intermediário | REQUER ADAPTAÇÃO |
| [09 - OBSIDIAN INGESTION](../workflows/agentes-rag/obsidian-ingestion/README.md) | Agentes e RAG | Processar conteúdo Obsidian para indexação/disponibilização. | Intermediário | REQUER ADAPTAÇÃO |
| [10 - AUDIOBOOK FACTORY](../workflows/arquivos/audiobook-factory/README.md) | Arquivos e Documentos | Integrar o factory ao Event Bus/monitoramento OMEAB. | Intermediário | REQUER ADAPTAÇÃO |
| [11 - MEDIA AUTOMATION](../workflows/arquivos/media-automation/README.md) | Arquivos e Documentos | Integrar media automation ao barramento de eventos. | Intermediário | REQUER ADAPTAÇÃO |
| [12 - IMMICH MONITOR](../workflows/monitoramento/immich-monitor/README.md) | Monitoramento e Observabilidade | Detectar anomalias Immich e notificar mudanças. | Avançado | REQUER ADAPTAÇÃO |
| [13 - HESTIA ACTION ROUTER](../workflows/integracoes/hestia-action-router/README.md) | Integrações e APIs | Expor system/storage/backup/docker/disk status via webhook hestia-acti | Avançado | REQUER ADAPTAÇÃO |
| [14 - UPDATE ADVISOR](../workflows/infraestrutura/update-advisor/README.md) | Infraestrutura e DevOps | Detectar, classificar e recomendar updates; emitir eventos só em mudan | Avançado | REQUER ADAPTAÇÃO |
| [15 - STORAGE CLEANUP ADVISOR](../workflows/infraestrutura/storage-cleanup-advisor/README.md) | Infraestrutura e DevOps | Analisar growth, deduplicar alertas e notificar recomendações úteis. | Intermediário | REQUER ADAPTAÇÃO |
| [18 - OMEAB SELF HEALTH](../workflows/monitoramento/omeab-self-health/README.md) | Monitoramento e Observabilidade | Avaliar saúde da automação a cada 5 minutos e alertar, com bypass Herm | Avançado | REQUER ADAPTAÇÃO |
| [19 - CONFIGURATION DRIFT GUARDIAN](../workflows/seguranca/configuration-drift-guardian/README.md) | Segurança e Governança | Detectar e persistir drift de componentes; notificar eventos novos. | Intermediário | REQUER ADAPTAÇÃO |
| [20 - INCIDENT CORRELATION ENGINE](../workflows/comunicacao/incident-correlation-engine/README.md) | Comunicação e Notificações | Processar hestia_events periodicamente e notificar mudanças significat | Intermediário | REQUER ADAPTAÇÃO |
| [21 - INCIDENT NOTIFICATION MANAGER](../workflows/comunicacao/incident-notification-manager/README.md) | Comunicação e Notificações | Rodar evaluate em shadow (enforcement=false) e registrar decisões. | Básico | REQUER ADAPTAÇÃO |

## Bloqueados

- `OSS-HOMOLOGATION-DO-NOT-USE` — Workflow de teste/homologação
- `ZZ - WORKFLOW MANAGER TEST` — Workflow de teste/homologação
