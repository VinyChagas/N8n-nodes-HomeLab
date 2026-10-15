# 09 - OBSIDIAN INGESTION

| Campo | Valor |
|-------|-------|
| Categoria | Agentes e RAG |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 5 |
| Tags | obsidian, notes, ingestion |

## Contexto

Ingestão de notas Obsidian no ecossistema de conhecimento/RAG.

## Problema

Notas locais precisam ser sincronizadas/indexadas de forma repetível.

## Necessidade

Automatizar fluxo de ingestão a partir do vault Obsidian.

## Objetivo

Processar conteúdo Obsidian para indexação/disponibilização.

## Solução

Trigger → chamada a serviço de ingestão → normalização → Event Bus se necessário.

## Benefícios

- Mantém base de conhecimento atualizada
- Menos sync manual

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
