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