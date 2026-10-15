# 05 - DISK CAPACITY

| Campo | Valor |
|-------|-------|
| Categoria | Infraestrutura e DevOps |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 8 |
| Tags | disk, capacity, filesystem |

## Contexto

Capacidade de filesystems monitorados no homeserver.

## Problema

Disco cheio causa falhas em cascata (bancos, mídia, backups).

## Necessidade

Alertar quando uso de disco ultrapassa limiares.

## Objetivo

Classificar capacidade (normal/warning/critical) e notificar mudanças.

## Solução

Schedule 15m → GET /v1/disk-capacity → evaluate → dedup → Event Bus.

## Benefícios

- Antecipa esgotamento de espaço
- Histórico por filesystem

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
