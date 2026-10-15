# 00 - HESTIA EVENT BUS

| Campo | Valor |
|-------|-------|
| Categoria | Integrações e APIs |
| Complexidade | Intermediário |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 7 |
| Tags | event-bus, webhook, hmac, hermes, postgres |

## Contexto

Barramento central de eventos do ecossistema OMEAB/Hestia no homeserver.

## Problema

Múltiplos monitores precisam notificar falhas e alertas sem cada um falar diretamente com o canal de mensagens.

## Necessidade

Centralizar normalização, persistência e roteamento de eventos por severidade.

## Objetivo

Receber eventos via webhook, persistir e encaminhar alertas relevantes ao Hestia/Hermes com autenticação HMAC.

## Solução

Webhook POST recebe o evento; Code normaliza severidade; Switch roteia; Postgres persiste; HMAC assina; HTTP envia ao Hermes.

## Benefícios

- Elimina integração ponto a ponto com Telegram/Hermes
- Padroniza severidade e payload
- Permite auditoria via Postgres
- Reduz risco de alertas malformados

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
