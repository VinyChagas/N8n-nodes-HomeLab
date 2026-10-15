# 21 - INCIDENT NOTIFICATION MANAGER

| Campo | Valor |
|-------|-------|
| Categoria | Comunicação e Notificações |
| Complexidade | Básico |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 4 |
| Tags | notifications, shadow-mode, policy |

## Contexto

Decisão do que vale comunicar sobre incidentes (shadow mode em produção).

## Problema

Nem todo evento/incidente merece notificação imediata.

## Necessidade

Avaliar política de notificação sem alterar o caminho original (shadow).

## Objetivo

Rodar evaluate em shadow (enforcement=false) e registrar decisões.

## Solução

Schedule 1m → omeab-notification-manager /v1/evaluate → Shadow Summary.

## Benefícios

- Aprende política sem risco de silenciar alertas reais
- Preserva caminho original de alerta

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
