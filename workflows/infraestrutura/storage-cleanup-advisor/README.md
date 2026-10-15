# 15 - STORAGE CLEANUP ADVISOR

| Campo | Valor |
|-------|-------|
| Categoria | Infraestrutura e DevOps |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 10 |
| Tags | cleanup, advisory, disk |

## Contexto

Análise consultiva de espaço recuperável (Docker cache, logs, inboxes).

## Problema

Espaço desperdiçado acumula sem orientação clara do que é seguro limpar.

## Necessidade

Recomendações com risk/confidence — sem prune/delete automático.

## Objetivo

Analisar growth, deduplicar alertas e notificar recomendações úteis.

## Solução

Cron 07:00 → GET /v1/storage-analysis → evaluate growth/dedup → persist → Event Bus.

## Benefícios

- Orienta limpeza segura
- Nunca remove automaticamente
- Protege dados Immich/backups/RAG

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
