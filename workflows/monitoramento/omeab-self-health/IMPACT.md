# Impacto — 18 - OMEAB SELF HEALTH

## Eficiência

- **Benefício esperado:** Detecta monitores overdue/inactive inesperados
- Reduz consultas manuais relacionadas a: credential:postgres, docker, hermes, http-port:5678, immich, obsidian, omeab, postgresql.

## Confiabilidade

- Deduplicação / decisão condicional: presente (If/Filter/Code)
- Persistência de estado: Postgres
- Retentativas nativas do workflow: não documentadas além do comportamento padrão do n8n.

## Observabilidade

- Integração típica: Event Bus Hestia (`00`) e/ou Hermes.
- Logs: execuções n8n + tabelas hestia_* quando Postgres está no fluxo.

## Segurança

- Credenciais tipadas no export original: postgres.
- Template público remove IDs de credencial e URLs privadas.
- Princípios OMEAB recorrentes: READ-ONLY, advisory ≠ execução, detect ≠ correct.

## Produtividade

- Detecta monitores overdue/inactive inesperados
- Break-glass evita ponto único de falha no Event Bus
- Não faz auto-repair

### IMPACTO COMPROVADO (amostra)

Amostra das últimas 100 execuções da API (`includeData=false`):

- Workflow ID de origem omitido no template público.
- Contagem na amostra: {"success": 4}
- Em toda a amostra global: 100/100 `success` (não generalizar como SLA histórico completo).


### BENEFÍCIO ESPERADO

Avaliar saúde da automação a cada 5 minutos e alertar, com bypass Hermes se Event Bus cair.

### POTENCIAL DE UTILIZAÇÃO

Reutilizável em outros homeservers/labs que implementem APIs equivalentes às placeholders.

### LIMITAÇÕES

- Dependências de serviços internos / URLs privadas / credenciais
- Métricas de tempo economizado **não mensuradas** na origem.
