# Backend Taskflow

### Dev
1. Clone o projeto
2. Crie e ative um ambiente virtual
2. ```pip install "fastapi[standard]"```
3. ```fastapi dev``` 
4. Acesse "http://127.0.0.1:8000

### Estrutura de Arquivos
backend-taskflow/
├── main.py
├── database.py
├── models.py
├── schemas.py
└── routers/
    ├── __init__.py
    ├── users.py
    ├── tasks.py
    └── dashboard.py