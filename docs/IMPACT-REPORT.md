# Relatório de Impacto

## Respostas objetivas

1. **Workflows encontrados:** 22
2. **Ativos:** 19
3. **Inativos:** 3
4. **Categorias identificadas:** 9
5. **Tipos de nodes diferentes:** 12
6. **Integrações mais recorrentes:** postgresql (14), rag (11), omeab (8), docker (6), postgres (6), hermes (4), restic (4), telegram (4)
7. **Problemas automatizados:** monitoramento de storage/disk/docker/backup/serviços; ingestão RAG/Obsidian; media/audiobook; updates consultivos; drift de config; correlação de incidentes; event bus Hestia; self-health da automação.
8. **Benefícios comprováveis:** na amostra das últimas 100 execuções, **100% success**; self-health e incident pipelines operacionais conforme docs OMEAB de gate (evidência documental local, sem reexecução).
9. **Métricas disponíveis:** amostra API `includeData=false` (n=100); sem tempos economizados mensurados.
10. **Melhorias possíveis:** error workflows dedicados; enforcement gradual do notification manager; UPS para power guardian; reduzir acoplamento a IPs internos via env desde o design; publicar só após LICENSE.

## Visão por categoria

### Agentes e RAG

Problema (síntese): Conteúdo novo precisa entrar no índice vetorial de forma controlada.; Notas locais precisam ser sincronizadas/indexadas de forma repetível.

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).

### Arquivos e Documentos

Problema (síntese): Pipeline de audiolivros (inbox/processing/generated) exige coordenação.; Filas inbox/review/homologation precisam de orquestração e alertas.

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).

### Backup e Recuperação

Problema (síntese): Backups podem falhar silenciosamente; descobrir tarde demais inviabiliza recuper

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).

### Comunicação e Notificações

Problema (síntese): Muitos eventos sintomáticos ofuscam a situação real (incidente).; Nem todo evento/incidente merece notificação imediata.

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).

### Infraestrutura e DevOps

Problema (síntese): Falhas de montagem, I/O e inconsistências de storage podem passar despercebidas ; Disco cheio causa falhas em cascata (bancos, mídia, backups).; Descobrir updates disponíveis exige checagens manuais em vários projetos.

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).

### Integrações e APIs

Problema (síntese): Múltiplos monitores precisam notificar falhas e alertas sem cada um falar direta; Assistente precisa consultar status do sistema sem acesso shell/docker.sock.

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).

### Monitoramento e Observabilidade

Problema (síntese): Quedas de serviço precisam virar eventos padronizados OMEAB com deduplicação.; Containers unhealthy/exited podem degradar o homeserver sem alerta imediato.; Visão fragmentada de system/storage/disk/docker/backups/eventos exige consultas 

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).

### Segurança e Governança

Problema (síntese): Mudanças não autorizadas em configs podem introduzir regressões silenciosas.

Solução: templates n8n documentados em `workflows/`.

Impacto: automação de coleta, deduplicação e alerta — qualitativo, salvo amostra de execuções.

Métrica: somente a amostra API quando disponível (ver workflows individuais).


## Diferenciação

| Tipo | Conteúdo |
|------|----------|
| IMPACTO COMPROVADO | Amostra 100 execuções success; docs de gate OMEAB para 19/20/21 |
| BENEFÍCIO ESPERADO | Menos checagens manuais; alertas centralizados |
| POTENCIAL | Templates adaptáveis a outros labs |
| LIMITAÇÕES | Stack OMEAB; shadow mode no 21; 16/17 bloqueados |
