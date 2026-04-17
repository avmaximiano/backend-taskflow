from database import SessionLocal, engine, Base
from models import Usuario, Tarefa


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(Usuario).count() > 0:
        print("Banco ja possui dados. Seed ignorado.")
        db.close()
        return

    usuarios = [
        Usuario(id=1, nome="Joao Silva",  email="joao@email.com",   funcao="Desenvolvedor",      cor="#4D80FF"),
        Usuario(id=2, nome="Maria Souza", email="maria@email.com",  funcao="Designer",            cor="#7B5CF5"),
        Usuario(id=3, nome="Carlos Lima", email="carlos@email.com", funcao="Gerente de Produto",  cor="#0E9F6E"),
    ]

    tarefas = [
        Tarefa(id=1, titulo="Implementar tela de login",  desc="Criar formulario de autenticacao com validacao",          prioridade="Alta",  status="Em Andamento", responsavelId=1, prazo="2026-04-10"),
        Tarefa(id=2, titulo="Criar API de usuarios",      desc="Endpoint REST para CRUD de usuarios",                    prioridade="Alta",  status="A Fazer",      responsavelId=1, prazo="2026-04-15"),
        Tarefa(id=3, titulo="Design do dashboard",        desc="Prototipo no Figma para revisao",                        prioridade="Media", status="Concluido",    responsavelId=2, prazo="2026-03-28"),
        Tarefa(id=4, titulo="Levantar requisitos v2",     desc="Reuniao com stakeholders para segunda versao",           prioridade="Baixa", status="Concluido",    responsavelId=3, prazo="2026-03-20"),
        Tarefa(id=5, titulo="Testes de integracao",       desc="Cobrir fluxo principal com testes automatizados",        prioridade="Alta",  status="A Fazer",      responsavelId=None, prazo="2026-04-20"),
        Tarefa(id=6, titulo="Deploy em producao",         desc="Configurar pipeline CI/CD no GitHub Actions",            prioridade="Media", status="A Fazer",      responsavelId=3, prazo="2026-04-30"),
    ]

    db.add_all(usuarios)
    db.commit()
    db.add_all(tarefas)
    db.commit()
    db.close()

    print("Seed concluido! 3 usuarios e 6 tarefas criados.")


if __name__ == "__main__":
    seed()
