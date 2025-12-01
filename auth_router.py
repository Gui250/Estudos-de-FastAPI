from fastapi import APIRouter, Depends
from models import User, database
from sqlalchemy.orm import sessionmaker
from app import bcrypt_context
from dependeces import pegar_sessao
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
def index():
    return {'message': 'Hello from auth router!'}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha : str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(User).filter(User.email == email).first()

    if usuario:
        return {'message': 'Já existe um usuário com esse email'}
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = User(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"message": "cadastro realizado com sucesso"}