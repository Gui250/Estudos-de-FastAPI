from models import database
from sqlalchemy.orm import sessionmaker
def pegar_sessao():
    try:
        Session = sessionmaker(bind=database)  # Criando a conexao com o banco de dados
        session = Session()
        yield session
    finally:
        session.close()