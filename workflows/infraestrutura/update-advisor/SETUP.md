# Instalação — 14 - UPDATE ADVISOR

## Pré-requisitos

- n8n **2.15.0** (versão auditada) ou compatível com os `typeVersion` dos nodes.
- Nodes nativos apenas (sem community nodes neste template).
- Serviços externos equivalentes aos placeholders (health API, Hermes, Postgres hestia, etc., conforme o fluxo).

## Dependências

- credential:postgres
- docker
- immich
- postgres
- postgresql
- rag
- update-advisor

## Importação

1. n8n → **Workflows** → **Import from File**.
2. Selecione `workflow.json`.
3. Confirme que o workflow ficou **inativo**.

## Credenciais

- Criar credencial do tipo `postgres` e associar nos nodes que exibem `{{CREDENTIAL_ID}}`

## Variáveis

Configure no ambiente n8n (veja `examples/env.example`):

- `SERVICE_BASE_URL`
- `OMEAB_SERVICE_URL`
- `HERMES_URL`
- Segredos HMAC / tokens conforme nodes Code/HTTP.

## Webhooks

Nenhum webhook neste workflow.

Ajuste paths e `WEBHOOK_URL` para o seu host. **Não exponha WAN** sem autenticação.

## Permissões

- Preferir tokens READ-ONLY nos serviços consultados.
- Postgres: privilégios mínimos nas tabelas de estado/eventos.

## Teste

1. Use payloads em `examples/sample-payloads/` (quando aplicável).
2. Execute manualmente com dados fictícios.
3. Verifique que nenhum segredo de produção foi colado no workflow.

## Ativação

Ative **somente após revisão** de URLs, credenciais e impacto de alertas.

## Troubleshooting

| Sintoma | Verificação |
|---------|-------------|
| HTTP 401/403 | Token/HMAC/env |
| ECONNREFUSED | `SERVICE_BASE_URL` / rede Docker |
| Postgres error | Credencial e schema |
| Sem alertas | Dedup pode estar suprimindo — confira estado anterior |

## Segurança

- Não reutilizar secrets de produção.
- Não ativar Action Router / webhooks sem HMAC.
