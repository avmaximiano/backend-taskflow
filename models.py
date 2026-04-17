from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    funcao = Column(String, nullable=False)
    cor = Column(String, default="#4D80FF")

    tarefas = relationship("Tarefa", back_populates="responsavel")


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    desc = Column(String, default="")
    prioridade = Column(String, default="Baixa")
    status = Column(String, default="A Fazer")
    responsavelId = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    prazo = Column(String, nullable=True)

    responsavel = relationship("Usuario", back_populates="tarefas")
