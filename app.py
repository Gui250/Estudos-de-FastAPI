import os

from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

from sqlalchemy.util import deprecated

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

from auth_router import auth_router
from produtos import product_router

app.include_router(auth_router)
app.include_router(product_router)