# 20 - INCIDENT CORRELATION ENGINE

| Campo | Valor |
|-------|-------|
| Categoria | Comunicação e Notificações |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 6 |
| Tags | incident, correlation |

## Contexto

Correlação de eventos Hestia em incidentes situacionais.

## Problema

Muitos eventos sintomáticos ofuscam a situação real (incidente).

## Necessidade

Motor determinístico que agrega eventos em incidentes.

## Objetivo

Processar hestia_events periodicamente e notificar mudanças significativas de incidente.

## Solução

Schedule 1m → omeab-incident-engine /v1/process → expand notifications → Event Bus.

## Benefícios

- Separa sintoma de situação
- Reduz ruído operacional (quando há correlação)
- Observer-only no Action Router

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
