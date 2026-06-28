# Checklist — QA + Cibersegurança Defensiva

## Comunicação segura

- [ ] Site utiliza HTTPS.
- [ ] Links principais apontam para URLs confiáveis.
- [ ] Não há redirecionamentos suspeitos.
- [ ] Links externos abrem corretamente.

## Exposição de informações

- [ ] Não há credenciais expostas no HTML.
- [ ] Não há tokens visíveis no código-fonte.
- [ ] Não há chaves de API públicas indevidas.
- [ ] Não há comentários internos sensíveis no HTML.
- [ ] Não há caminhos locais sensíveis expostos ao usuário final.

## Mensagens de erro

- [ ] Erros não revelam stack trace.
- [ ] Erros não expõem tecnologia interna desnecessária.
- [ ] Mensagens são claras para o usuário.
- [ ] Mensagens não ajudam exploração indevida.

## Formulários e entradas

- [ ] Campos obrigatórios são indicados.
- [ ] Entradas inválidas são tratadas.
- [ ] Mensagens de validação são amigáveis.
- [ ] Campos sensíveis não exibem dados indevidos.

## Permissões e acesso

- [ ] Áreas restritas não aparecem para usuário sem permissão.
- [ ] Links administrativos não são expostos.
- [ ] Arquivos privados não estão acessíveis publicamente.
- [ ] Pastas sensíveis não estão listadas.

## Logs e rastreabilidade

- [ ] Eventos relevantes podem ser registrados.
- [ ] Logs não devem armazenar senhas.
- [ ] Logs não devem expor tokens.
- [ ] Logs devem ajudar investigação defensiva.

## Boas práticas

- [ ] Princípio do menor privilégio considerado.
- [ ] Dados sensíveis tratados com cuidado.
- [ ] Arquivos públicos revisados.
- [ ] Dependências e integrações devem ser mantidas atualizadas.
