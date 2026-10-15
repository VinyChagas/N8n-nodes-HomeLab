# 12 - IMMICH MONITOR

| Campo | Valor |
|-------|-------|
| Categoria | Monitoramento e Observabilidade |
| Complexidade | Avançado |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 14 |
| Tags | immich, photos, monitor |

## Contexto

Monitoramento do Immich (fotos) no homeserver.

## Problema

Falhas no Immich (API, jobs, storage) impactam biblioteca de fotos.

## Necessidade

Observar saúde Immich e correlacionar com Event Bus.

## Objetivo

Detectar anomalias Immich e notificar mudanças.

## Solução

Schedule → HTTP Immich/health-agent → evaluate → Postgres → Event Bus.

## Benefícios

- Detecção precoce de problemas Immich
- Integração ao stack de alertas OMEAB

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
