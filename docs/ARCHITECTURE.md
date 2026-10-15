# Arquitetura

## Ambientes identificados

### 1) n8n VPS / homeserver (OMEAB)

| Campo | Valor |
|-------|-------|
| Nome | n8n OMEAB Homeserver |
| Servidor | VPS/homeserver (bind LAN `<LAN_BIND_IP>`) |
| Versão n8n | 2.15.0 |
| Execução | Docker Compose (`/opt/homeserver/n8n`) |
| Imagem | `n8nio/n8n:2.15.0` |
| Banco | PostgreSQL (`DB_TYPE=postgresdb`, database `n8n`, host container `postgres`) |
| Persistência | `/opt/homeserver/n8n/data` → `/home/node/.n8n` |
| Nodes comunitários | Nenhum (`dependencies: {}`) |
| Workflows (API) | 22 |
| Ativos | 19 |
| Inativos | 3 |
| Método de coleta | Public API READ (`workflow:list/read`) + JSON versionados em `/opt/homeserver/n8n/workflows` |

### 2) n8n no “OMEAB” como produto separado

Não foi encontrada **outra** instância n8n dedicada “OMEAB” além da acima.
OMEAB aparece como **conjunto de microserviços** (rag, incident-engine, notification-manager, update-advisor, config-guardian, media-manager, audiobook-factory, control-center) orquestrados **por** este n8n.

Acesso a outros servidores internos **não** foi tentado sem evidência de permissão.

## Papel do n8n

```
Monitores / Schedules / Webhooks
        │
        ▼
      n8n  ──orquestra──►  APIs OMEAB / health-agent (READ)
        │
        ├── Postgres (estado / eventos)
        │
        └── Hestia Event Bus → Hermes / Hestia (alertas)
```

Princípios observados na documentação operacional:

- Sem `docker.sock` no container n8n
- Advisory ≠ execução (updates/cleanup)
- Detectar ≠ corrigir (drift)
- Action Router V1 somente READ
