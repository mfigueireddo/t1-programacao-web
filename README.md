# t1-programacao-web

# 🧩 Sistema Kanban Web

## 📌 Sobre o projeto

Sistema web no formato de quadro Kanban, desenvolvido com:
- Python (Django)
- HTML
- CSS

---

## 👥 Integrantes

- Matheus Figueiredo — 2320813  
- Luana Nobre — 2310204  

---

## 🚀 Funcionalidades já implementadas

- Cadastro de usuário (`/signup/`)
- Login (`/login/`)
- Logout (`/logout/`)
- Redirecionamento após login
- Proteção da página principal (`/`)
- Validação de usuário único

---

## 🌐 Rotas do sistema

| Rota | Descrição |
|------|----------|
| `/signup/` | Cadastro |
| `/login/` | Login |
| `/logout/` | Logout |
| `/` | Página principal (Kanban) |
| `/admin/` | Painel do Django |

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