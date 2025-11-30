from fastapi import FastAPI

app = FastAPI()

from auth_router import auth_router
from produtos import product_router

app.include_router(auth_router)
app.include_router(product_router)