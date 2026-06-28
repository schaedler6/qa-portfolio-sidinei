# Casos de Teste de API — JSONPlaceholder

| ID | Método | Endpoint | Cenário | Resultado esperado | Status |
|---|---|---|---|---|---|
| API-001 | GET | `/posts/1` | Buscar post existente | Retornar status 200 e objeto JSON com `id`, `userId`, `title` e `body` | Pendente |
| API-002 | GET | `/posts/999999` | Buscar post inexistente | Retornar objeto vazio ou resposta controlada pela API | Pendente |
| API-003 | POST | `/posts` | Criar post simulado | Retornar status 201 e JSON com os dados enviados | Pendente |
| API-004 | PUT | `/posts/1` | Atualizar post simulado | Retornar status 200 e JSON com os dados atualizados | Pendente |
| API-005 | DELETE | `/posts/1` | Remover post simulado | Retornar status 200 ou 204 conforme comportamento da API | Pendente |

## Observações

A API utilizada é pública e simula operações. Os dados não são persistidos como em uma aplicação real de produção.
