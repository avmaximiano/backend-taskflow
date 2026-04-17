from pydantic import BaseModel
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str
    email: str
    funcao: str
    cor: Optional[str] = "#4D80FF"


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    funcao: Optional[str] = None
    cor: Optional[str] = None


class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        from_attributes = True


class TarefaBase(BaseModel):
    titulo: str
    desc: Optional[str] = ""
    prioridade: Optional[str] = "Baixa"
    status: Optional[str] = "A Fazer"
    responsavelId: Optional[int] = None
    prazo: Optional[str] = None


class TarefaCreate(TarefaBase):
    pass


class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    desc: Optional[str] = None
    prioridade: Optional[str] = None
    status: Optional[str] = None
    responsavelId: Optional[int] = None
    prazo: Optional[str] = None


class TarefaOut(TarefaBase):
    id: int

    class Config:
        from_attributes = True
