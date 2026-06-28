# Plano de Teste de API — JSONPlaceholder

## 1. Objetivo

Validar endpoints REST da API JSONPlaceholder, demonstrando entendimento de requisições HTTP, status codes, corpo JSON e critérios básicos de aceitação para QA.

## 2. Escopo

### Incluído

- Requisição GET para buscar recurso existente.
- Requisição POST para criar recurso simulado.
- Requisição PUT para atualizar recurso simulado.
- Requisição DELETE para remover recurso simulado.
- Validação de status code.
- Validação de campos no JSON.
- Validação de tipos básicos de dados.

### Fora do escopo

- Testes de autenticação real.
- Testes de performance.
- Testes de carga.
- Testes de banco de dados.
- Testes de segurança ofensiva.

## 3. Ambiente

- Ferramenta: Postman
- API base: https://jsonplaceholder.typicode.com
- Sistema operacional: Windows 10/11
- Responsável: Sidinei Schaedler

## 4. Critérios de entrada

- Postman instalado ou versão web disponível.
- Collection importada.
- Environment configurado com `base_url`.
- Conexão com internet disponível.

## 5. Critérios de saída

- Todos os casos executados.
- Resultados documentados.
- Falhas registradas como bug report, quando aplicável.

## 6. Riscos

- API pública indisponível temporariamente.
- Mudança no comportamento do serviço externo.
- Bloqueio de rede local.
- Diferença entre resposta simulada e API real de produção.
