# BUG-002 — Botão Baixar Currículo QA pode apontar para arquivo ausente

## Identificação

| Campo | Informação |
|---|---|
| ID | BUG-002 |
| Título | Botão de currículo precisa validar existência do PDF |
| Projeto | SID.DEV.BR |
| Tipo | Risco funcional |
| Status | Aberto / a validar |

## Ambiente

- Sistema operacional: Windows 10/11
- Navegador: Chrome
- URL local: http://localhost:5520
- Área afetada: Hero principal

## Pré-condição

Site carregado com a versão QA visualmente aprovada.

## Passos para reprodução

1. Acessar a página inicial.
2. Clicar no botão `BAIXAR CURRÍCULO QA`.
3. Observar se o arquivo PDF é aberto ou baixado corretamente.

## Resultado esperado

O botão deve abrir ou baixar o arquivo `Curriculo_Sidinei_QA_Junior.pdf`.

## Resultado obtido

Necessário validar se o arquivo existe no caminho indicado no site.

## Severidade

Média.

## Prioridade

Alta.

## Evidência

A ser adicionada após teste do link.

## Observações

Antes do deploy oficial, o currículo QA precisa existir no diretório esperado e ser testado no ambiente local e público.
