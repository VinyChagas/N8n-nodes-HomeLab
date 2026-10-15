# 14 - UPDATE ADVISOR

| Campo | Valor |
|-------|-------|
| Categoria | Infraestrutura e DevOps |
| Complexidade | Avançado |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 17 |
| Tags | updates, advisory, versions |

## Contexto

Conselheiro de atualizações de componentes (n8n, Hermes, Jellyfin, Immich, etc.).

## Problema

Descobrir updates disponíveis exige checagens manuais em vários projetos.

## Necessidade

Avaliação consultiva diária sem executar upgrades.

## Objetivo

Detectar, classificar e recomendar updates; emitir eventos só em mudanças relevantes.

## Solução

Cron 06:30 → contexto multi-fonte → omeab-update-advisor /v1/evaluate → persist → Event Bus.

## Benefícios

- Visibilidade de drift de versões
- Princípio descoberta ≠ execução
- Sem auto-update perigoso

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
