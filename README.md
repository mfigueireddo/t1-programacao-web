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