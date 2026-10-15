# Contribuindo

Obrigado por considerar contribuir com o VinyLab Automation Hub.

## Princípios

1. **Somente templates sanitizados** — nunca commit de API keys, tokens, IPs privados, chat IDs ou connection strings.
2. **Não executar** workflows de produção como parte da contribuição.
3. **Documentar impacto** com evidência; não inventar métricas.
4. **Preservar estrutura** de nodes/conexões ao ajustar placeholders.

## Fluxo sugerido

1. Fork / branch a partir da revisão aprovada.
2. Adicione ou melhore um workflow em `workflows/<categoria>/<slug>/`.
3. Inclua `workflow.json`, `README.md`, `TECHNICAL.md`, `IMPACT.md`, `SETUP.md`, `diagram.md`.
4. Rode `scripts/validate-workflows.py` e `scripts/scan-secrets.py`.
5. Abra PR descrevendo problema de negócio e adaptações necessárias.

## Classificação de reutilização

- **PRONTO PARA COMPARTILHAR** — pode entrar no catálogo público.
- **REQUER ADAPTAÇÃO** — template ok com SETUP claro.
- **NÃO PUBLICÁVEL** — apenas menção genérica.

## Segurança

Veja [SECURITY.md](SECURITY.md) e [docs/SECURITY-GUIDE.md](docs/SECURITY-GUIDE.md).
