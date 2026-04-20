# t1-programacao-web

---

## 👥 Integrantes

- Matheus Figueiredo — 2320813  
- Luana Nobre — 2310204  

---

## 🌍 Acessar o sistema (localmente)

Endereço padrão
```bash
http://127.0.0.1:8000/
```

---

## 🌐 Rotas do sistema

| Rota | Descrição |
|------|----------|
| `/` | Redireciona à kanban/ |
| `/authentication/signup/` | Cadastro |
| `/authentication/login/` | Login |
| `/authentication/logout/` | Logout |
| `/kanban/` | Kanban |
| `/kanban/criar/` | Criar tarefa |
| `/kanban/<int:tarefa_id>/editar/` | Editar tarefa |
| `/kanban/<int:tarefa_id>/deletar/` | Deletar tarefa |

---

## 🔐 Funcionamento da recuperação de senha por e-mail

A funcionalidade de recuperação de senha foi implementada utilizando o sistema de autenticação padrão do Django.

Quando o usuário clica na opção **"Esqueci minha senha"**, ele é direcionado para uma tela onde deve informar o e-mail cadastrado no sistema.

Após o envio do formulário, o Django gera automaticamente um token único e temporário associado ao usuário. Esse token é utilizado para criar um link seguro de redefinição de senha.

Como o projeto está em ambiente de desenvolvimento, o envio de e-mails foi configurado utilizando o backend de console (`console.EmailBackend`). Dessa forma, ao invés de enviar um e-mail real, o conteúdo da mensagem é exibido diretamente no terminal.

O e-mail contém:
- Uma mensagem informando a solicitação de redefinição
- Um link com token único para redefinir a senha

O usuário deve copiar e colar esse link no navegador. Ao acessá-lo, o sistema valida o token:
- Se o token for válido, o usuário pode cadastrar uma nova senha
- Se o token for inválido ou já utilizado, uma mensagem de erro é exibida

Após a redefinição da senha, o usuário pode realizar login normalmente com a nova senha.

Essa abordagem garante segurança no processo, evitando que terceiros consigam redefinir a senha sem acesso ao e-mail do usuário.

---

## 🛠️ Como rodar o projeto

Acesse [BUILD.md](BUILD.md)

---

## O que foi feito

Aqui listaremos os pontos levantados na [proposta inicial](proposta/proposta-incrementada.md) e discutiremos o que fizemos e não fizemos, o que funcionou e não funcionou.

### "2. Modelos de Dados"

Os modelos de dados implementados seguem o que foi proposto.

Podemos encontrar o modelo de kanban [aqui](kanban/models.py) e o de usuário [aqui](authentication/models.py)

Na verdade, houveram 2 mudanças no modelo de Usuário. 

1. Ao invés de delimitar os usuários em "Administrador" e "Usuário", os chamamos de "Mantenedor" e "Usuário", para evitar qualquer tipo de relação com o modelo de admin do Django.

2. Adicionamos os campos email e mantenedor definido.
O campo email serve para envio de email de recuperação de senha.
O campo mantenedor definido serve para evitar que o usuário altere sua permissão depois de criar sua conta.

### "3. Modelo de Permissões"

As permissões de administrador e usuário seguem as especificações a não ser em 1 ponto.
Até o momento, não implementamos uma aba para o usuário visualizar e editar sua conta.

### "4. Jornada do Usuário"

A jornada do usuário segue o proposto, menos a questão já levantada sobre o gerenciamento do perfil.

### 5. "Páginas do Sistema"

As páginas do sistema possuem nomes diferentes mas funcionalidades equivalentes.

Qualquer página que seja relacionada ao kanban deve começar com 'kanban/', assim como qualquer página relacionada ao perfil do usuário deve começar com 'authentication/'.

## Resumo

Com isso, concluímos que a única coisa não feita até o momento foi o gerenciamento do perfil do usuário.

Além disso, um detalhe que notamos ao fazermos alguns testes é que a página de visualização do kanban não possui restrições que regulem o tamanho de um card. Isso quer dizer que se o usuário resolver criar uma tarefa excessivamente grande, toda a descrição dessa tarefa será exibida.