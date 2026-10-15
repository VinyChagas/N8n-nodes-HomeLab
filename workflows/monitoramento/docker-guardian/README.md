# 04 - DOCKER GUARDIAN

| Campo | Valor |
|-------|-------|
| Categoria | Monitoramento e Observabilidade |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 8 |
| Tags | docker, containers, health |

## Contexto

Observabilidade READ-ONLY de containers Docker via health-agent (sem docker.sock no n8n).

## Problema

Containers unhealthy/exited podem degradar o homeserver sem alerta imediato.

## Necessidade

Monitorar estado/health dos containers a cada poucos minutos.

## Objetivo

Detectar mudanças no estado Docker e emitir eventos deduplicados.

## Solução

Schedule 2m → GET /v1/docker → evaluate → Postgres state → notify Event Bus.

## Benefícios

- Sem necessidade de inspecionar Portainer manualmente
- Sem docker.sock no n8n (menor superfície de ataque)

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
