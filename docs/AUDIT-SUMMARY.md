# Resumo da Auditoria

**Modo:** READ-ONLY sobre n8n  
**Escrita:** apenas em `/home/vini/VinyLab-Automation-Hub` e cópia privada isolada  
**Data de referência do ambiente:** 2026-10-15

## Ambientes

| Ambiente | Acessível | Observação |
|----------|-----------|------------|
| n8n VPS/homeserver OMEAB | Sim | Docker `n8nio/n8n:2.15.0`, Postgres, API pública |
| Outra instância n8n “OMEAB” | Não encontrada | OMEAB = microserviços orquestrados por este n8n |
| Servidores remotos sem evidência de permissão | Não acessados | Limitação registrada |

## Coleta

- Public API `/api/v1/workflows` + detalhe por ID
- JSONs versionados em `/opt/homeserver/n8n/workflows`
- Documentação operacional em `/opt/homeserver/n8n/docs`
- Métricas: `/api/v1/executions?includeData=false` (amostra)

## Não realizado (conforme regras)

- Reinício/alteração de containers
- Ativar/desativar/executar workflows
- Alterar credenciais, env, DB, webhooks
- Importação de teste em produção
- git push / publicação GitHub

## Exportação privada

`/home/vini/VinyLab-Automation-Hub-PRIVATE/` (chmod 700) — fora do hub público e do Git.
