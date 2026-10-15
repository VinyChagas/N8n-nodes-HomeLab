# Impacto — 03 - SERVICE DOWN ALERT

## Eficiência

- **Benefício esperado:** Integra monitoring externo ao Event Bus
- Reduz consultas manuais relacionadas a: credential:postgres, omeab, postgresql.

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

- Integra monitoring externo ao Event Bus
- Evita flood de alertas
- Centraliza status de serviços

### IMPACTO COMPROVADO

Sem execuções deste workflow na amostra das últimas 100 execuções no momento da auditoria.
Não inventar taxa de sucesso histórica.


### BENEFÍCIO ESPERADO

Normalizar status up/down e notificar mudanças significativas.

### POTENCIAL DE UTILIZAÇÃO

Reutilizável em outros homeservers/labs que implementem APIs equivalentes às placeholders.

### LIMITAÇÕES

- Dependências de serviços internos / URLs privadas / credenciais
- Métricas de tempo economizado **não mensuradas** na origem.
