# Casos de Teste — Segurança Defensiva

| ID | Categoria | Cenário | Passos | Resultado esperado | Status |
|---|---|---|---|---|---|
| SEC-001 | HTTPS | Validar acesso seguro | Acessar a URL pública do site | Site deve carregar via HTTPS | Pendente |
| SEC-002 | Links externos | Validar links de perfil | Clicar em GitHub e LinkedIn | Links devem abrir destinos corretos e confiáveis | Pendente |
| SEC-003 | Exposição de dados | Verificar código-fonte visível | Inspecionar HTML público | Não deve haver senha, token ou chave sensível | Pendente |
| SEC-004 | Mensagens de erro | Simular recurso inexistente | Acessar caminho inexistente do site | Erro não deve revelar informação sensível | Pendente |
| SEC-005 | Arquivos públicos | Validar arquivos esperados | Verificar robots.txt, sitemap.xml e llms.txt | Arquivos públicos devem estar coerentes e sem dados sensíveis | Pendente |
| SEC-006 | Currículo | Validar arquivo público | Acessar link do currículo QA | Arquivo deve existir e não expor dados indevidos | Pendente |
| SEC-007 | Console | Validar erros no navegador | Abrir DevTools e carregar site | Console não deve mostrar erro crítico ou dado sensível | Pendente |
| SEC-008 | Conteúdo público | Revisar textos publicados | Ler seções principais do site | Não deve haver informação privada ou sensível | Pendente |
