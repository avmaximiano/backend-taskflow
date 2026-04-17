import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

class PriorityEnum(enum.Enum):
    ALTA = "Alta"
    MEDIA = "Media"
    BAIXA = "Baixa"

class StatusEnum(enum.Enum):
    A_FAZER = "A fazer"
    EM_ANDAMENTO = "Em andamento"
    CONCLUIDO = "Concluido"

class Task():
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    priority = Column(Enum(PriorityEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    status = Column(Enum(StatusEnum,values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="tasks")