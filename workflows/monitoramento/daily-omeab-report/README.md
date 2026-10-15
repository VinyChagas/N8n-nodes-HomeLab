# 06 - DAILY OMEAB REPORT

| Campo | Valor |
|-------|-------|
| Categoria | Monitoramento e Observabilidade |
| Complexidade | Avançado |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 11 |
| Tags | report, daily, hermes |

## Contexto

Relatório diário consolidado da saúde do OMEAB.

## Problema

Visão fragmentada de system/storage/disk/docker/backups/eventos exige consultas manuais.

## Necessidade

Snapshot diário enviável ao Hestia/Hermes.

## Objetivo

Agregar métricas das últimas 24h e enviar relatório assinado (HMAC).

## Solução

Cron 08:00 → múltiplos GET health-agent → Postgres eventos → build snapshot → HMAC → Hermes.

## Benefícios

- Briefing operacional diário automatizado
- Visão consolidada sem dashboard manual

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
