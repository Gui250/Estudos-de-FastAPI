from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import declarative_base

# Faz a conexão com o banco de dados
database = create_engine('sqlite:///database.db')

# declara a base do banco de dados
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column( "id",Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column("name",String)
    email = Column("email",String, nullable=False)
    password = Column("password",String)
    admin = Column("admin",Boolean, default=False)
    ativo = Column("ativo",Boolean)

    def __init__(self, name, email, password, admin, ativo):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        self.ativo = ativo

class Pedido(Base):
    __tablename__ = 'pedidos'

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('CANCELED', 'CANCELED'),
        ('FINISHED', 'FINISHED'),
    )

    id = Column("id",Integer, primary_key=True, nullable=False, autoincrement=True)
    status = Column("status",ChoiceType(STATUS_CHOICES), nullable=False)
    usuario = Column("usuario",ForeignKey("users.id"))
    preco = Column("preco",Float, nullable=False)

class ItemPedido(Base):
    __tablename__ = 'item_pedidos'

    id = Column("id",Integer, primary_key=True, nullable=False, autoincrement=True)
    quantidade = Column("quantidade",Integer, nullable=False)
    sabor = Column("sabor",String, nullable=False)
    tamanho = Column("tamanho",Integer, nullable=False)
    preco_unitario = Column("preco_unitario",Float, nullable=False)
    pedido = Column("pedido",ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario