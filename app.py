from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routers import tarefas, usuarios
from seed import seed

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tarefas.router)
app.include_router(usuarios.router)


@app.on_event("startup")
def on_startup():
    seed()


@app.get("/")
def raiz():
    return {"msg": "TaskFlow API rodando!", "docs": "/docs"}
