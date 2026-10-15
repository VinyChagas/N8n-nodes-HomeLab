# VinyLab Automation Hub

Biblioteca de automações n8n desenvolvidas para resolver problemas reais de infraestrutura, produtividade, integrações e inteligência artificial.

> Auditoria READ-ONLY · n8n `2.15.0` · instância homeserver/OMEAB · **sem publicação automática**.

## Objetivo

Organizar, documentar e disponibilizar **templates sanitizados** dos workflows operacionais, com análise de impacto, diagramas e guias de instalação — prontos para revisão humana antes de qualquer release pública.

## Catálogo de workflows

| Workflow | Categoria | Objetivo | Complexidade |
|----------|-----------|----------|--------------|
| [00 - HESTIA EVENT BUS](workflows/integracoes/hestia-event-bus/README.md) | Integrações e APIs | Receber eventos via webhook, persistir e encaminhar alertas relevantes ao Hestia… | Intermediário |
| [01 - Storage Guardian](workflows/infraestrutura/storage-guardian/README.md) | Infraestrutura e DevOps | Avaliar saúde do storage periodicamente e emitir eventos no Event Bus quando o e… | Intermediário |
| [02 - BACKUP VERIFICATION](workflows/backup/backup-verification/README.md) | Backup e Recuperação | Detectar falhas ou degradação no status de backup e notificar via Event Bus. | Intermediário |
| [03 - SERVICE DOWN ALERT](workflows/monitoramento/service-down-alert/README.md) | Monitoramento e Observabilidade | Normalizar status up/down e notificar mudanças significativas. | Intermediário |
| [04 - DOCKER GUARDIAN](workflows/monitoramento/docker-guardian/README.md) | Monitoramento e Observabilidade | Detectar mudanças no estado Docker e emitir eventos deduplicados. | Intermediário |
| [05 - DISK CAPACITY](workflows/infraestrutura/disk-capacity/README.md) | Infraestrutura e DevOps | Classificar capacidade (normal/warning/critical) e notificar mudanças. | Intermediário |
| [06 - DAILY OMEAB REPORT](workflows/monitoramento/daily-omeab-report/README.md) | Monitoramento e Observabilidade | Agregar métricas das últimas 24h e enviar relatório assinado (HMAC). | Avançado |
| [07 - WEEKLY OMEAB REPORT](workflows/monitoramento/weekly-omeab-report/README.md) | Monitoramento e Observabilidade | Compilar visão de 7 dias e entregar via Hermes com HMAC. | Avançado |
| [08 - RAG INGESTION](workflows/agentes-rag/rag-ingestion/README.md) | Agentes e RAG | Disparar/orquestrar ingestão RAG e reportar resultado ao Event Bus quando aplicá… | Intermediário |
| [09 - OBSIDIAN INGESTION](workflows/agentes-rag/obsidian-ingestion/README.md) | Agentes e RAG | Processar conteúdo Obsidian para indexação/disponibilização. | Intermediário |
| [10 - AUDIOBOOK FACTORY](workflows/arquivos/audiobook-factory/README.md) | Arquivos e Documentos | Integrar o factory ao Event Bus/monitoramento OMEAB. | Intermediário |
| [11 - MEDIA AUTOMATION](workflows/arquivos/media-automation/README.md) | Arquivos e Documentos | Integrar media automation ao barramento de eventos. | Intermediário |
| [12 - IMMICH MONITOR](workflows/monitoramento/immich-monitor/README.md) | Monitoramento e Observabilidade | Detectar anomalias Immich e notificar mudanças. | Avançado |
| [13 - HESTIA ACTION ROUTER](workflows/integracoes/hestia-action-router/README.md) | Integrações e APIs | Expor system/storage/backup/docker/disk status via webhook hestia-action. | Avançado |
| [14 - UPDATE ADVISOR](workflows/infraestrutura/update-advisor/README.md) | Infraestrutura e DevOps | Detectar, classificar e recomendar updates; emitir eventos só em mudanças releva… | Avançado |
| [15 - STORAGE CLEANUP ADVISOR](workflows/infraestrutura/storage-cleanup-advisor/README.md) | Infraestrutura e DevOps | Analisar growth, deduplicar alertas e notificar recomendações úteis. | Intermediário |
| [18 - OMEAB SELF HEALTH](workflows/monitoramento/omeab-self-health/README.md) | Monitoramento e Observabilidade | Avaliar saúde da automação a cada 5 minutos e alertar, com bypass Hermes se Even… | Avançado |
| [19 - CONFIGURATION DRIFT GUARDIAN](workflows/seguranca/configuration-drift-guardian/README.md) | Segurança e Governança | Detectar e persistir drift de componentes; notificar eventos novos. | Intermediário |
| [20 - INCIDENT CORRELATION ENGINE](workflows/comunicacao/incident-correlation-engine/README.md) | Comunicação e Notificações | Processar hestia_events periodicamente e notificar mudanças significativas de in… | Intermediário |
| [21 - INCIDENT NOTIFICATION MANAGER](workflows/comunicacao/incident-notification-manager/README.md) | Comunicação e Notificações | Rodar evaluate em shadow (enforcement=false) e registrar decisões. | Básico |

### Não publicáveis (apenas menção)

- `OSS-HOMOLOGATION-DO-NOT-USE` — Workflow de teste/homologação
- `ZZ - WORKFLOW MANAGER TEST` — Workflow de teste/homologação

### Planejados / bloqueados no ambiente de origem (sem workflow)

- **16 — POWER GUARDIAN** — bloqueado (`POWER_GUARDIAN_BLOCKED_NO_UPS`): sem UPS/telemetria.
- **17 — POWER RECOVERY** — bloqueado por dependência do 16.

## Categorias

| Pasta | Categoria |
|-------|-----------|
| `infraestrutura/` | Infraestrutura e DevOps |
| `monitoramento/` | Monitoramento e Observabilidade |
| `agentes-rag/` | Agentes e RAG |
| `integracoes/` | Integrações e APIs |
| `comunicacao/` | Comunicação e Notificações |
| `backup/` | Backup e Recuperação |
| `arquivos/` | Arquivos e Documentos |
| `seguranca/` | Segurança e Governança |
| `outros/` | Outros |

## Tecnologias

- n8n 2.15.0 (Docker Compose, Postgres)
- Nodes nativos: Webhook, Schedule, HTTP Request, Code, IF, Switch, Filter, Merge, Postgres, Respond to Webhook, Set, Manual Trigger
- Stack adjacente (origem): Hermes, health-agent OMEAB, Immich, microserviços omeab-*, Uptime Kuma

## Pré-requisitos

- n8n instalado (recomendado ≥ 2.15 ou compatível)
- Credenciais e serviços equivalentes aos placeholders
- Leitura de [docs/SECURITY-GUIDE.md](docs/SECURITY-GUIDE.md)

## Como importar

1. Abra o `workflow.json` do template desejado.
2. No n8n: Import from File.
3. Mantenha **inativo**.
4. Siga o `SETUP.md` do workflow.

## Credenciais

Recrie credenciais locais. Os templates usam `{{CREDENTIAL_ID}}` / `{{CREDENTIAL_NAME}}` e `{{$env.*}}`.

## Segurança

- Nunca commit de `.env` real.
- Rode `python3 scripts/scan-secrets.py` antes de publicar.
- Veja [SECURITY.md](SECURITY.md).

## Contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md). Licença: [LICENSE-REVIEW.md](LICENSE-REVIEW.md) (pendente).

## Limitações conhecidas

- Quase todos os templates **REQUEREM ADAPTAÇÃO** (serviços OMEAB internos).
- Exportações privadas ficam fora deste diretório (`~/VinyLab-Automation-Hub-PRIVATE`).
- Compatibilidade: estrutural apenas — importação real não executada nesta auditoria.
- Métricas: amostra das últimas 100 execuções; não é histórico completo.
