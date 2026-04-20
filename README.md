# t1-programacao-web

---

## 👥 Integrantes

- Matheus Figueiredo — 2320813  
- Luana Nobre — 2310204  

---

## 🌐 Rotas do sistema

| Rota | Descrição |
|------|----------|
| `/` | Redireciona à kanban/ |
| `/signup/` | Cadastro |
| `/login/` | Login |
| `/logout/` | Logout |
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

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar ambiente virtual

```bash
./venv/Scripts/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Aplicar migrações

```bash
python .\manage.py makemigrations
python .\manage.py migrate
```

### 5. Rodar o servidor

```bash
python manage.py runserver
```

---

## 🌍 Acessar o sistema

```bash
http://127.0.0.1:8000/
```