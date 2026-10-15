# 13 - HESTIA ACTION ROUTER

| Campo | Valor |
|-------|-------|
| Categoria | Integrações e APIs |
| Complexidade | Avançado |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 32 |
| Tags | hestia, hmac, action-router, read-only |

## Contexto

Roteador de ações READ-ONLY solicitadas pelo Hestia/Hermes.

## Problema

Assistente precisa consultar status do sistema sem acesso shell/docker.sock.

## Necessidade

Endpoint autenticado (HMAC) com catálogo restrito de actions de leitura.

## Objetivo

Expor system/storage/backup/docker/disk status via webhook hestia-action.

## Solução

Webhook → validação HMAC/timestamp → Switch de actions → HTTP health-agent → respondToWebhook.

## Benefícios

- Hestia consulta status sem privilégios destrutivos
- Contrato versionado de actions
- Replay protection (janela 300s)

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
