from fastapi import APIRouter
from models import User, database
from sqlalchemy.orm import sessionmaker
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
def index():
    return {'message': 'Hello from auth router!'}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha : str, nome: str):
    Session = sessionmaker(bind=database) # Criando a conexao com o banco de dados
    session = Session()
    usuario = session.query(User).filter(User.email == email).first()

    if usuario:
        return {'message': 'Já existe um usuário com esse email'}
    else:
        novo_usuario = User(nome, email, senha)
        session.add(novo_usuario)
        session.commit()