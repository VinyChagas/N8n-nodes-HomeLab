# 02 - BACKUP VERIFICATION

| Campo | Valor |
|-------|-------|
| Categoria | Backup e Recuperação |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 8 |
| Tags | backup, restic, postgres, verification |

## Contexto

Verificação periódica do estado de backups (ex.: Postgres/restic) via health-agent.

## Problema

Backups podem falhar silenciosamente; descobrir tarde demais inviabiliza recuperação.

## Necessidade

Confirmar periodicamente se backups reportados estão ok e alertar mudanças.

## Objetivo

Detectar falhas ou degradação no status de backup e notificar via Event Bus.

## Solução

Schedule horário → GET /v1/backups → Evaluate → estado anterior → dedup → Event Bus.

## Benefícios

- Reduz checagens manuais de backup
- Histórico operacional
- Alerta precoce de falha

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
