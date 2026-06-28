# Boas Práticas Defensivas para QA

## 1. Observar sem explorar

O papel do QA defensivo é identificar riscos, registrar evidências e comunicar o problema de forma responsável.

## 2. Validar exposição de dados

Durante a análise visual e funcional, verificar se informações sensíveis aparecem em:

- HTML público.
- Console do navegador.
- Mensagens de erro.
- Arquivos públicos.
- URLs.
- Respostas de API.

## 3. Registrar evidências com cuidado

Evidências devem demonstrar o problema sem divulgar credenciais, tokens, dados pessoais ou caminhos internos sensíveis.

## 4. Comunicar impacto e recomendação

Um bom relatório defensivo deve conter:

- O que foi observado.
- Onde foi observado.
- Qual o risco.
- Qual a recomendação.
- Qual a prioridade.

## 5. Respeitar escopo

Nenhum teste deve ultrapassar autorização, ambiente ou objetivo definido.

## 6. Conectar QA com segurança

Testes de qualidade também ajudam a melhorar segurança quando validam:

- Autenticação.
- Permissões.
- Erros.
- Logs.
- Dados expostos.
- Fluxos críticos.
