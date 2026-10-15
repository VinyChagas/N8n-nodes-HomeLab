# 08 - RAG INGESTION

| Campo | Valor |
|-------|-------|
| Categoria | Agentes e RAG |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 5 |
| Tags | rag, ingestion, embeddings |

## Contexto

Ingestão de documentos no pipeline RAG OMEAB.

## Problema

Conteúdo novo precisa entrar no índice vetorial de forma controlada.

## Necessidade

Automatizar gatilho de ingestão sem operação manual repetitiva.

## Objetivo

Disparar/orquestrar ingestão RAG e reportar resultado ao Event Bus quando aplicável.

## Solução

Trigger → HTTP ao serviço RAG → processamento/normalização → notificação opcional.

## Benefícios

- Padroniza ingestão
- Reduz passos manuais no pipeline de conhecimento

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
