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
python .\manage.py makemigrations authentication kanban
python .\manage.py migrate
```

### 5. Rodar o servidor

```bash
python manage.py runserver
```

### Script consolidado

```bash
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
python .\manage.py makemigrations authentication kanban
python .\manage.py migrate
python manage.py runserver
```

## Nota

Tem de ser feito python .\manage.py makemigrations authentication kanban porque migrations/ não está sendo trackeada pelo Git.

O comando python .\manage.py makemigrations apenas detecta modificações nos modelos.