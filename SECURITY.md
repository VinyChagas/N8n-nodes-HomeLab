# Segurança

## Relatar vulnerabilidades

Não abra issue pública com segredos. Contate o mantenedor do repositório por canal privado.

## Escopo deste hub

- Templates n8n **sanitizados**.
- Documentação de arquitetura e impacto.
- Scripts de validação estrutural e scan de segredos.

## Fora de escopo

- Credenciais reais do ambiente OMEAB.
- Exportações privadas (`VinyLab-Automation-Hub-PRIVATE/`).
- Endereços internos, webhooks de produção e payloads de clientes.

## Boas práticas ao importar

1. Importe **desativado**.
2. Recrie credenciais locais.
3. Substitua placeholders `{{$env.*}}`.
4. Teste com dados fictícios.
5. Ative só após revisão.
