from fastapi import FastAPI

app = FastAPI(title="Taskflow", version="1.0.0")

@app.get('/')
def pagina_inicial():
    return {"msg": "Conseguimos"}