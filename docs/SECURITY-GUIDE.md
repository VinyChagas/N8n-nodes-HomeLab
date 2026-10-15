# Guia de Segurança

## Sanitização aplicada

- IDs de workflow de produção removidos do template
- IDs de credenciais → `{{CREDENTIAL_ID}}`
- URLs com IP privado → `{{$env.SERVICE_BASE_URL}}` / placeholders
- Tokens/secrets embutidos → `{{$env.*}}`
- `active: false` nos templates
- `pinData` limpo

## Exportação privada

Cópias brutas (se existentes) permanecem apenas em diretório restrito fora do Git público:
`~/VinyLab-Automation-Hub-PRIVATE/` (mode 700).

## Checklist pré-publicação

1. `scan-secrets.py` sem findings `high`
2. Revisar sticky notes e Code nodes
3. Confirmar LICENSE
4. Remover IPs de inventário dos docs se a publicação for estritamente pública
