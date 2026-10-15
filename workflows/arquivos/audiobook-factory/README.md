# 10 - AUDIOBOOK FACTORY

| Campo | Valor |
|-------|-------|
| Categoria | Arquivos e Documentos |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | inativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 8 |
| Tags | audiobook, media-pipeline |

## Contexto

Orquestração do serviço audiobook-factory OMEAB.

## Problema

Pipeline de audiolivros (inbox/processing/generated) exige coordenação.

## Necessidade

Automatizar verificação/disparo consultivo do factory.

## Objetivo

Integrar o factory ao Event Bus/monitoramento OMEAB.

## Solução

Schedule/manual → HTTP audiobook-factory → evaluate → Event Bus.

## Benefícios

- Visibilidade do pipeline de audiobooks
- Menos acompanhamento manual de filas

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
