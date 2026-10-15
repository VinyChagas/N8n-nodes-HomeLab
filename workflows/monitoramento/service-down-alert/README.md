# 03 - SERVICE DOWN ALERT

| Campo | Valor |
|-------|-------|
| Categoria | Monitoramento e Observabilidade |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 7 |
| Tags | uptime, webhook, service-status |

## Contexto

Recepção de webhooks de monitoramento de serviços (padrão compatível com Uptime Kuma).

## Problema

Quedas de serviço precisam virar eventos padronizados OMEAB com deduplicação.

## Necessidade

Traduzir heartbeats de monitores externos para o Event Bus Hestia.

## Objetivo

Normalizar status up/down e notificar mudanças significativas.

## Solução

Webhook service-status → normalize → estado anterior Postgres → decide → Event Bus.

## Benefícios

- Integra monitoring externo ao Event Bus
- Evita flood de alertas
- Centraliza status de serviços

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
