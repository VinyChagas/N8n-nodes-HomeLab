# 07 - WEEKLY OMEAB REPORT

| Campo | Valor |
|-------|-------|
| Categoria | Monitoramento e Observabilidade |
| Complexidade | Avançado |
| Estado na origem (auditoria) | ativo |
| Reutilização | REQUER ADAPTAÇÃO |
| Nodes | 16 |
| Tags | report, weekly |

## Contexto

Relatório semanal consolidado OMEAB.

## Problema

Tendências semanais (eventos, saúde, capacidade) não ficam evidentes no dia a dia.

## Necessidade

Resumo semanal para revisão operacional.

## Objetivo

Compilar visão de 7 dias e entregar via Hermes com HMAC.

## Solução

Schedule semanal → coleta multi-fonte → agregação Code → HMAC → Hermes.

## Benefícios

- Revisão periódica estruturada
- Suporte a planejamento de manutenção

## Arquivos

- [TECHNICAL.md](TECHNICAL.md) — nodes, conexões, código
- [IMPACT.md](IMPACT.md) — impacto operacional
- [SETUP.md](SETUP.md) — instalação
- [diagram.md](diagram.md) — diagramas Mermaid
- [workflow.json](workflow.json) — template sanitizado

## Aviso

Template sanitizado. **REQUER ADAPTAÇÃO** ao seu ambiente. Não contém credenciais reais.
Compatibilidade estrutural validada. Importação real não executada.
