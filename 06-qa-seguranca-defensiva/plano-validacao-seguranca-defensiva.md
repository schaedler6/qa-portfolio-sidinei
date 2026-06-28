# Plano de Validação — QA + Segurança Defensiva

## 1. Objetivo

Validar pontos básicos de segurança defensiva que podem ser observados durante atividades de QA em aplicações web, sem executar ações ofensivas.

## 2. Sistema de referência

- Tipo: Aplicação web / site institucional / portfólio
- Exemplo usado: SID.DEV.BR
- Foco: validações defensivas e boas práticas

## 3. Escopo incluído

- Verificação de links HTTPS.
- Verificação de mensagens de erro.
- Observação de exposição indevida de informações.
- Verificação de arquivos públicos esperados.
- Validação de comportamento de links externos.
- Análise de permissões quando aplicável.
- Verificação de campos sensíveis quando aplicável.
- Registro de evidências defensivas.

## 4. Fora do escopo

- Teste de invasão.
- Exploração de vulnerabilidades.
- Ataques de força bruta.
- Varredura automatizada agressiva.
- Engenharia social.
- Acesso a áreas não autorizadas.
- Manipulação maliciosa de dados.

## 5. Ambiente

- Windows 10/11
- Navegador Chrome, Edge ou Firefox
- DevTools do navegador
- PowerShell para validações simples
- Acesso somente a recursos públicos e autorizados

## 6. Critérios de entrada

- Aplicação acessível.
- Ambiente autorizado.
- Escopo definido.
- Nenhum teste ofensivo planejado.

## 7. Critérios de saída

- Checklist preenchido.
- Riscos documentados.
- Evidências registradas.
- Recomendações defensivas descritas.
