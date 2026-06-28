# BUG-001 — Partículas visíveis, mas sem movimento

## Identificação

| Campo | Informação |
|---|---|
| ID | BUG-001 |
| Título | Partículas do fundo aparecem estáticas |
| Projeto | SID.DEV.BR |
| Tipo | Defeito visual / regressão |
| Status | Corrigido na base aprovada |

## Ambiente

- Sistema operacional: Windows 10/11
- Navegador: Chrome
- URL local: http://localhost:5520
- Área afetada: Home / fundo animado

## Pré-condição

Site aberto em ambiente local via servidor HTTP.

## Passos para reprodução

1. Abrir o site local em `http://localhost:5520`.
2. Observar o fundo da página inicial.
3. Aguardar alguns segundos.
4. Comparar o comportamento das partículas com a versão aprovada anteriormente.

## Resultado esperado

As partículas devem permanecer visíveis e em movimento suave no fundo da página, sem interferir no menu, botões ou conteúdo principal.

## Resultado obtido

As partículas aparecem visualmente, porém ficam estáticas, dando a impressão de fundo travado.

## Severidade

Média.

## Prioridade

Alta.

## Evidência

Evidência visual registrada durante a validação local.

## Observações

O problema já havia ocorrido anteriormente no projeto e a solução aprovada foi manter a base com `sid-canvas-bg-visivel`, preservando `preview.js` e `requestAnimationFrame`.
