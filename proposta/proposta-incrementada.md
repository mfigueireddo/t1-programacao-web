# Quadro Kanban - Proposta de Desenvolvimento

Este arquivo foi inspirado em [proposta.md](./proposta.md) com ajuda de IA no seguinte prompt:
```
Essa é a proposta que eu tenho para meu website. Formate o arquivo, complemente com informações, corrija possíveis erros e incremente caso julgue necessário
```

## 1. Visão Geral

Sistema web para gerenciamento de tarefas em formato de quadro Kanban, com suporte a múltiplos usuários, controle de permissões baseado em papéis e rastreamento de responsabilidades entre membros da equipe.

---

## 2. Modelos de Dados

### 2.1 Tarefa

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| Nome | String | Sim | Título da tarefa (máx. 255 caracteres) |
| Status | Enum | Sim | Estágio da tarefa (ver seção 2.3) |
| Descrição | Text | Não | Detalhes da tarefa |
| Responsáveis | List<Usuário> | Não | Um ou mais usuários responsáveis |
| Story Points | Number | Não | Estimativa de esforço (0-100) |
| Data de Criação | DateTime | Sim | Preenchida automaticamente |
| Data Limite | DateTime | Não | Prazo da tarefa |
| Data de Fechamento | DateTime | Não | Preenchida ao mudar para "Concluído" |
| Criador | Usuário | Sim | Usuário que criou a tarefa |

### 2.2 Usuário

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| Nome | String | Sim | Único no sistema |
| Senha | String (Hash) | Sim | Senha |
| Permissão | Enum | Sim | `ADMINISTRADOR` ou `USUÁRIO` |

### 2.3 Status de Tarefa

Os possíveis status são:
- `A Fazer`
- `Em Progresso`
- `Pronto`
- `Entregue`

---

## 3. Modelo de Permissões

### Matriz de Permissões

| Ação | Administrador | Usuário |
|------|---------------|---------|
| **Create** | Tarefa completa | X |
| **Read** | Todas informações | Todas informações |
| **Update** | Todas informações | Responsável (adicionar/remover a si mesmo); Status (se for responsável) |
| **Delete** | Permissão concedida | X |
| **Editar Usuário** | Todas informações | Todas informações |

---

## 4. Jornada do Usuário

### 4.1 Primeira Etapa: Autenticação

**Condição:** Usuário não autenticado

**Comportamento:**
- Usuário pode fazer **login** com nome/senha
- Usuário pode fazer **cadastro** de nova conta
- Links de redirecionamento entre login e cadastro
- Validações: nome de usuário único

**Saída:** Após autenticação bem-sucedida, redirecionar para a Segunda Etapa

### 4.2 Segunda Etapa: Visualização do Kanban

**Condição:** Usuário autenticado

**Comportamento:**
- Visualizar todas as tarefas organizadas em **colunas por status**
- Layout em cards dentro de cada coluna
- Botão **Criar Tarefa** no topo (apenas para Administrador)
- Botão **Perfil** no topo-direito para acessar informações da conta
- Botão **Logout** no topo-direito

**Conteúdo de cada Card:**
- Nome da tarefa
- Status (destacado visualmente)
- Responsáveis (avatares ou nomes)
- Story points (opcional)
- Data limite (se definida)
- Icones de ações que o usuário pode executar (editar, remover)

### 4.3 Terceira Etapa: Ações sobre Tarefas

**Criar Tarefa** (apenas Administrador)
- Link/botão: acima da visualização do Kanban
- Preencher: nome, descrição, data limite, responsáveis, story points
- Redirecionar para Segunda Etapa após sucesso

**Editar Tarefa** (Administrador e Usuário com restrições)
- Link/botão: em cada card de tarefa
- Administrador: alterar todos os campos
- Usuário: apenas responsáveis (adicionar/remover a si mesmo) e status (se for responsável)
- Redirecionar para Segunda Etapa após sucesso

**Remover Tarefa** (apenas Administrador)
- Link/botão: em cada card de tarefa
- Confirmação de exclusão (modal/diálogo)
- Redirecionar para Segunda Etapa após sucesso

### 4.4 Quarta Etapa: Gerenciar Conta

**Acesso:**
- Botão **Perfil** no topo-direito (Segunda Etapa)

**Opções de Edição:**
- **Nome:** texto editável, máx. 100 caracteres
- **Senha:** campo oculto, com confirmação, mínimo 8 caracteres
- **Permissões:** Administrador ou Usuário

**Ações:**
- **Voltar** para Segunda Etapa (Kanban)
- **Logout** da conta
- **Salvar Alterações** com validação

---

## 5. Páginas do Sistema

| Página | Rota | Acesso | Descrição |
|--------|------|--------|-----------|
| Cadastro | `/signup` | Anônimo | Criar nova conta |
| Login | `/login` | Anônimo | Autenticar usuário |
| Kanban | `/kanban` | Autenticado | Visualizar e gerenciar tarefas |
| Criar Tarefa | `/tasks/create` | Admin | Criar nova tarefa |
| Editar Tarefa | `/tasks/:id/edit` | Admin + Usuário (restrito) | Editar tarefa existente |
| Remover Tarefa | `/tasks/:id/delete` | Admin | Remover tarefa (com confirmação) |
| Perfil/Conta | `/profile` | Autenticado | Editar informações e permissões |