# 18 - OMEAB SELF HEALTH

| Campo | Valor |
|-------|-------|
| Categoria | Monitoramento e Observabilidade |
| Complexidade | Avançado |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 19 |
| Tags | self-health, observability, break-glass |

## Contexto

Autobservabilidade: monitora se os próprios workflows monitores estão saudáveis.

## Problema

Se monitores falham silenciosamente, o operador perde cobertura sem saber.

## Necessidade

Registry de intenção (active/inactive/blocked) + heartbeat + break-glass.

## Objetivo

Avaliar saúde da automação a cada 5 minutos e alertar, com bypass Hermes se Event Bus cair.

## Solução

Schedule → health-agent + n8n API workflows/executions → registry → evaluate → persist → Event Bus ou break-glass Hermes.

## Benefícios

- Detecta monitores overdue/inactive inesperados
- Break-glass evita ponto único de falha no Event Bus
- Não faz auto-repair

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
