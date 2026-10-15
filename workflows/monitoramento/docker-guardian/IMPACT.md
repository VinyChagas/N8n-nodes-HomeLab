# Impacto — 04 - DOCKER GUARDIAN

## Eficiência

- **Benefício esperado:** Sem necessidade de inspecionar Portainer manualmente
- Reduz consultas manuais relacionadas a: credential:postgres, docker, postgresql.

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

- Sem necessidade de inspecionar Portainer manualmente
- Sem docker.sock no n8n (menor superfície de ataque)

### IMPACTO COMPROVADO (amostra)

Amostra das últimas 100 execuções da API (`includeData=false`):

- Workflow ID de origem omitido no template público.
- Contagem na amostra: {"success": 10}
- Em toda a amostra global: 100/100 `success` (não generalizar como SLA histórico completo).


### BENEFÍCIO ESPERADO

Detectar mudanças no estado Docker e emitir eventos deduplicados.

### POTENCIAL DE UTILIZAÇÃO

Reutilizável em outros homeservers/labs que implementem APIs equivalentes às placeholders.

### LIMITAÇÕES

- Dependências de serviços internos / URLs privadas / credenciais
- Métricas de tempo economizado **não mensuradas** na origem.
