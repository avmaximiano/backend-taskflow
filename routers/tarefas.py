from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from models import Tarefa
from schemas import TarefaCreate, TarefaUpdate, TarefaOut

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])


@router.get("/", response_model=List[TarefaOut])
def listar_tarefas(
    status: Optional[str] = None,
    prioridade: Optional[str] = None,
    responsavelId: Optional[int] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Tarefa)

    if status:
        query = query.filter(Tarefa.status == status)
    if prioridade:
        query = query.filter(Tarefa.prioridade == prioridade)
    if responsavelId:
        query = query.filter(Tarefa.responsavelId == responsavelId)

    return query.all()


@router.get("/{tarefa_id}", response_model=TarefaOut)
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return tarefa


@router.post("/", response_model=TarefaOut, status_code=201)
def criar_tarefa(dados: TarefaCreate, db: Session = Depends(get_db)):
    tarefa = Tarefa(**dados.model_dump())
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)
    return tarefa


@router.put("/{tarefa_id}", response_model=TarefaOut)
def atualizar_tarefa(tarefa_id: int, dados: TarefaUpdate, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(tarefa, campo, valor)

    db.commit()
    db.refresh(tarefa)
    return tarefa


@router.patch("/{tarefa_id}/status", response_model=TarefaOut)
def atualizar_status(tarefa_id: int, status: str, db: Session = Depends(get_db)):
    validos = ["A Fazer", "Em Andamento", "Concluido"]
    if status not in validos:
        raise HTTPException(status_code=400, detail=f"Status invalido. Use: {validos}")

    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")

    tarefa.status = status
    db.commit()
    db.refresh(tarefa)
    return tarefa


@router.delete("/{tarefa_id}", status_code=204)
def deletar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    db.delete(tarefa)
    db.commit()
