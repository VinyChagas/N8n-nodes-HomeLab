# 11 - MEDIA AUTOMATION

| Campo | Valor |
|-------|-------|
| Categoria | Arquivos e Documentos |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 8 |
| Tags | media, jellyfin-adjacent |

## Contexto

Automação de mídia via omeab-media-manager.

## Problema

Filas inbox/review/homologation precisam de orquestração e alertas.

## Necessidade

Monitorar/acionar fluxos de media manager de forma segura.

## Objetivo

Integrar media automation ao barramento de eventos.

## Solução

Schedule → HTTP media-manager → evaluate → Event Bus.

## Benefícios

- Status das filas de mídia
- Menos polling manual

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
