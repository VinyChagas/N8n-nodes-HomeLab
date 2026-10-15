# 01 - Storage Guardian

| Campo | Valor |
|-------|-------|
| Categoria | Infraestrutura e DevOps |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 8 |
| Tags | storage, health-agent, dedup, schedule |

## Contexto

Monitoramento contínuo do storage doméstico exposto pelo health-agent OMEAB.

## Problema

Falhas de montagem, I/O e inconsistências de storage podem passar despercebidas até corrupção ou indisponibilidade.

## Necessidade

Detectar degradação de storage e notificar apenas em mudanças relevantes (deduplicação).

## Objetivo

Avaliar saúde do storage periodicamente e emitir eventos no Event Bus quando o estado mudar.

## Solução

Schedule → HTTP /v1/storage → avaliação em Code → estado anterior no Postgres → Merge → decisão de notificação → Event Bus.

## Benefícios

- Substitui verificação manual de mounts
- Histórico de estados no banco
- Evita spam de alertas via dedup

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
