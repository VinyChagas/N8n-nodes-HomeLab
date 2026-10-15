# Impacto — 13 - HESTIA ACTION ROUTER

## Eficiência

- **Benefício esperado:** Hestia consulta status sem privilégios destrutivos
- Reduz consultas manuais relacionadas a: audiobook, credential:postgres, docker, immich, media-manager, omeab, postgres, postgresql.

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

- Hestia consulta status sem privilégios destrutivos
- Contrato versionado de actions
- Replay protection (janela 300s)

### IMPACTO COMPROVADO

Sem execuções deste workflow na amostra das últimas 100 execuções no momento da auditoria.
Não inventar taxa de sucesso histórica.


### BENEFÍCIO ESPERADO

Expor system/storage/backup/docker/disk status via webhook hestia-action.

### POTENCIAL DE UTILIZAÇÃO

Reutilizável em outros homeservers/labs que implementem APIs equivalentes às placeholders.

### LIMITAÇÕES

- Dependências de serviços internos / URLs privadas / credenciais
- Métricas de tempo economizado **não mensuradas** na origem.
