## Proposta de trabalho a ser desenvolvido:

### Quadro Kanban

#### Modelos

1. Tarefa
- Nome
- Status
- Responsável (ou responsáveis)
- Story points
- Descrição
- Data de criação
- Data limite
- Data de fechamento

2. Usuário
- Nome (Único)
- Senha
- Permissões

#### Permissões

1. Administrador: CRUD completo da tarefa

2. Usuário: Read e Update da tarefa
- Read: todas as informações
- Update: adicionar/remover si mesmo como responsável; alterar o status caso seja o responsável

#### Visões

1. Create
- Administrador: todas as informações

2. Read
- Administrador: todas as informações
- Usuário: todas as informações

3. Update
- Administrador: todas as informações
- Usuário: responsável (apenas adicionar ou remover a si mesmo); status (caso seja ele o responsável)

4. Delete
- Administrador: permissão concedida

#### Páginas 

- Cadastro
- Login
- Observar Kanban
- Criar tarefa (Administrador)
- Editar tarefa (Administrador)
- Editar tarefa (Usuário)
- Remover tarefa (Administrador)

#### Fluxo do programa 

**Primeira etapa**: Identificação do usuário
- Caso o usuário não esteja identificado, ele poderá fazer login ou se cadastrar. Deverá haver um botão de redirecionamento para o cadastro na página de login e vice-versa
- Caso o usuário esteja identificado, seguir para a segunda etapa.

**Segunda etapa**: Visualização das tarefas
- Visualização de todas as tarefas do quadro, separando-as em colunas de acordo com seu status

**Terceira etapa**: Ações sobre as tarefas
- 1. Criar tarefa (Administrador)
- 2. Editar tarefa (Administrador e Usuário)
- 3. Remover tarefa (Administrador)
- A opção de criação deverá ser um botão disponibilizado acima da visualização das tarefas
- As opções de edição e remoção deverão ser botões vinculados à cada tarefa
- Todas as ações dessa etapa deverão redirecionar à segunda etapa quando concluídas

**Terceira etapa**: Ações sobre a conta
- Haverá um botão acima da visualização das tarefas em que o usuário poderá acessar suas informações
- Ele poderá alterar seu nome, senha e permissçoes

#### Observações

O usuário deverá informar suas responsabilidades no momento de criação da conta.