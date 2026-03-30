# Planejamento de Desenvolvimento — Sistema Kanban

## 1. Contexto do Projeto

Este documento descreve o planejamento de desenvolvimento de um sistema web no formato de quadro Kanban, desenvolvido para a disciplina de Programação para Web.

O sistema terá como objetivo permitir o gerenciamento de tarefas com múltiplos usuários, incluindo diferenciação de permissões entre administrador e usuário comum, conforme definido na proposta do projeto.

O desenvolvimento será realizado entre **29 de março de 2026 e 21 de abril de 2026**, respeitando os requisitos da disciplina, incluindo:
- uso de Django (Python), HTML e CSS;
- implementação completa de operações CRUD;
- autenticação de usuários;
- diferenciação de permissões;
- publicação do sistema;
- uso de Git com versionamento contínuo;
- entrega com documentação (README).

---

## 2. Estratégia de Desenvolvimento

Devido ao prazo curto, o projeto será desenvolvido de forma incremental, priorizando funcionamento antes de refinamento.

A ordem de construção será:

1. Estrutura base + autenticação  
2. Modelagem e CRUD principal  
3. Regras de permissão  
4. Interface Kanban  
5. Deploy e documentação  

Essa abordagem reduz o risco de atraso e garante que o sistema esteja funcional desde as primeiras semanas.

---

## 3. Escopo Prioritário

### 3.1 Funcionalidades obrigatórias

- Cadastro de usuário  
- Login e logout  
- Visualização do quadro Kanban  
- Criação de tarefas (admin)  
- Edição de tarefas (admin e usuário com restrições)  
- Remoção de tarefas (admin)  
- Associação de responsáveis  
- Alteração de status  
- Página de perfil  

### 3.2 Regras de permissão

Administrador:
- Pode criar, editar e excluir tarefas
- Pode alterar qualquer campo

Usuário comum:
- Pode visualizar todas as tarefas
- Pode alterar o status apenas se for responsável
- Pode adicionar/remover a si mesmo como responsável
- Não pode editar outros campos
- Não pode criar ou excluir tarefas

### 3.3 Decisões importantes

- Permissão não será editável pelo próprio usuário (evita inconsistência)
- Controle de acesso será feito no backend, não apenas na interface
- Interface será simples, sem uso de JavaScript (conforme exigido)

---

## 4. Planejamento Detalhado por Semana

---

## Semana 1 — 29/03 a 04/04  
### Foco: Estrutura inicial e autenticação

### Objetivo
Estabelecer a base do sistema e garantir autenticação funcional.

### Atividades

#### Definição final do escopo
- Revisar proposta inicial e versão incrementada
- Confirmar modelos de dados
- Definir rotas principais
- Alinhar divisão de trabalho

#### Pré-projeto
- Escrever resumo do sistema
- Enviar e-mail ao professor

#### Setup técnico
- Criar repositório Git
- Criar projeto Django
- Criar app principal
- Configurar templates e estrutura de pastas

#### Autenticação
- Implementar cadastro de usuário
- Implementar login
- Implementar logout
- Garantir validação de usuário único
- Redirecionamento correto após login

### Entregas da semana
- Projeto rodando
- Autenticação funcional
- Estrutura organizada
- Primeiro push relevante no Git

---

## Semana 2 — 05/04 a 11/04  
### Foco: CRUD de tarefas (núcleo do sistema)

### Objetivo
Implementar completamente o modelo de tarefas e suas operações principais.

### Atividades

#### Modelagem
Criar model `Tarefa` com:
- nome
- status
- descrição
- responsáveis (relação com usuário)
- story points
- data de criação (automática)
- data limite
- data de fechamento
- criador

#### Implementação do CRUD
- Criar tarefa (admin)
- Listar tarefas
- Editar tarefa (admin)
- Deletar tarefa (admin)

#### Visualização Kanban
- Separar tarefas por status:
  - A Fazer
  - Em Progresso
  - Pronto
  - Entregue
- Exibir cards com informações principais

#### Permissões básicas
- Usuário comum não acessa criação
- Usuário comum não deleta
- Rotas protegidas

### Entregas da semana
- CRUD funcionando
- Tarefas persistindo no banco
- Kanban exibindo corretamente
- Permissões iniciais aplicadas

---

## Semana 3 — 12/04 a 18/04  
### Foco: Permissões completas e refinamento do sistema

### Objetivo
Garantir coerência das regras de negócio e melhorar usabilidade.

### Atividades

#### Regras completas de permissão
- Usuário altera status somente se for responsável
- Usuário adiciona/remove a si mesmo como responsável
- Bloquear edição de outros campos
- Garantir validação no backend

#### Perfil do usuário
- Criar página `/profile`
- Permitir edição de nome
- Permitir alteração de senha

#### Interface
- Melhorar layout do Kanban
- Organizar colunas visualmente
- Ajustar botões de ação
- Melhorar navegação

### Entregas da semana
- Sistema completo funcional
- Permissões corretas
- Interface organizada

---

## Semana 4 — 19/04 a 21/04  
### Foco: Finalização, deploy e entrega

### Objetivo
Garantir que o sistema esteja pronto para avaliação.

### Atividades

#### Deploy
- Publicar sistema
- Testar ambiente online
- Corrigir erros de configuração

#### README
Incluir:
- descrição do sistema
- escopo implementado
- manual de uso
- descrição das páginas
- explicação das permissões
- o que funciona
- o que não funciona

#### Testes

Autenticação:
- cadastro
- login
- logout

Administrador:
- CRUD completo

Usuário:
- visualização
- alteração de status
- restrições de acesso

Perfil:
- edição de dados

#### Revisão final
- Conferir funcionamento geral
- Validar fluxos
- Preparar apresentação

### Entregas finais
- Sistema publicado
- README completo
- Repositório atualizado
- Links prontos para envio

---

## 5. Marcos do Projeto

- 04/04 → Autenticação pronta  
- 11/04 → CRUD completo  
- 18/04 → Sistema funcional  
- 20/04 → Deploy + README  
- 21/04 → Entrega  

---

## 6. Considerações Finais

O projeto é totalmente viável dentro do prazo, desde que o foco seja mantido nas funcionalidades essenciais.

A qualidade da entrega dependerá principalmente de:
- consistência das permissões
- funcionamento completo do CRUD
- clareza da navegação
- documentação bem escrita

A prioridade deve ser entregar um sistema simples, funcional e bem estruturado.