# Impacto — 21 - INCIDENT NOTIFICATION MANAGER

## Eficiência

- **Benefício esperado:** Aprende política sem risco de silenciar alertas reais
- Reduz consultas manuais relacionadas a: notification, telegram.

## Confiabilidade

- Deduplicação / decisão condicional: limitada / não evidente
- Persistência de estado: não observada
- Retentativas nativas do workflow: não documentadas além do comportamento padrão do n8n.

## Observabilidade

- Integração típica: Event Bus Hestia (`00`) e/ou Hermes.
- Logs: execuções n8n + tabelas hestia_* quando Postgres está no fluxo.

## Segurança

- Credenciais tipadas no export original: nenhuma.
- Template público remove IDs de credencial e URLs privadas.
- Princípios OMEAB recorrentes: READ-ONLY, advisory ≠ execução, detect ≠ correct.

## Produtividade

- Aprende política sem risco de silenciar alertas reais
- Preserva caminho original de alerta

### IMPACTO COMPROVADO (amostra)

Amostra das últimas 100 execuções da API (`includeData=false`):

- Workflow ID de origem omitido no template público.
- Contagem na amostra: {"success": 21}
- Em toda a amostra global: 100/100 `success` (não generalizar como SLA histórico completo).


### BENEFÍCIO ESPERADO

Rodar evaluate em shadow (enforcement=false) e registrar decisões.

### POTENCIAL DE UTILIZAÇÃO

Reutilizável em outros homeservers/labs que implementem APIs equivalentes às placeholders.

### LIMITAÇÕES

- Dependências de serviços internos / URLs privadas / credenciais
- Métricas de tempo economizado **não mensuradas** na origem.
