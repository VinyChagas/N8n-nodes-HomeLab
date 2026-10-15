# 19 - CONFIGURATION DRIFT GUARDIAN

| Campo | Valor |
|-------|-------|
| Categoria | Segurança e Governança |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 11 |
| Tags | drift, governance, baseline |

## Contexto

Detecção de drift de configuração contra baseline aprovada (config-guardian).

## Problema

Mudanças não autorizadas em configs podem introduzir regressões silenciosas.

## Necessidade

Comparar estado atual com baseline; alertar drift — sem auto-correção.

## Objetivo

Detectar e persistir drift de componentes; notificar eventos novos.

## Solução

Schedule 15m → GET configuration-drift → evaluate/dedup/persist → Event Bus.

## Benefícios

- Governança de configuração
- Princípio DETECTAR ≠ CORRIGIR
- Baseline versionada

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
