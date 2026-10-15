# Instalação geral

## 1. Pré-requisitos

- n8n (Docker ou npm) — versão de referência **2.15.0**
- Postgres se o template usar node Postgres
- Variáveis de `examples/env.example`

## 2. Importar um template

1. Escolha `workflows/<categoria>/<slug>/workflow.json`
2. Importe no n8n **desativado**
3. Siga o `SETUP.md` local

## 3. Validar localmente

```bash
python3 scripts/validate-workflows.py
python3 scripts/scan-secrets.py
```

## 4. Não fazer

- Não apontar templates para produção sem revisão
- Não reutilizar secrets do ambiente auditado
- Não expor webhooks na WAN sem autenticação
