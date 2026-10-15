# Revisão de Licenciamento — VinyLab Automation Hub

**Status:** decisão humana pendente. Nenhuma licença pública definitiva foi aplicada.

## Contexto

Os workflows documentados originam-se do ambiente n8n operacional OMEAB/homeserver.
A autoria aparente é do mantenedor do ambiente (VinyLab/OMEAB), mas a redistribuição
pública exige confirmação explícita do proprietário.

## Pontos que exigem decisão

1. **Autoria e titularidade** dos workflows e da documentação derivada.
2. **Dependências de serviços privados** (health-agent, Hermes, microserviços OMEAB) — o código JSON sanitizado pode ser OSS, mas o runtime completo não é reproduzível sem esses serviços.
3. **Nodes utilizados:** apenas nodes nativos n8n (`n8n-nodes-base.*`). Sem nodes comunitários instalados no ambiente auditado (`data/nodes/package.json` com `dependencies: {}`).
4. **n8n** em si é software separado (licença Fair-Code / Sustainable Use da n8n GmbH) — este repositório não redistribui o binário n8n.
5. **Marcas e nomes** (OMEAB, Hestia, Immich, Jellyfin, etc.) — uso documental vs. branding de produto.

## Alternativas relevantes (para escolha humana)

| Opção | Quando faz sentido |
|-------|-------------------|
| MIT | Máxima reutilização de templates sanitizados |
| Apache-2.0 | Preferência por patente grant explícito |
| Source-available / uso interno | Se a intenção for documentação interna apenas |
| Dual license | Templates MIT + docs CC-BY |

## Recomendação do auditor

Não publicar no GitHub público até:

- escolher a licença;
- confirmar que nenhum segredo restou nos templates;
- revisar workflows classificados como REQUER ADAPTAÇÃO quanto a lógica confidencial.

Este arquivo **não** constitui LICENSE.
