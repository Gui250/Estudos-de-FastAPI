from fastapi import APIRouter

product_router = APIRouter(prefix="/products", tags=["products"])

@product_router.get("/")
def index():
    return {'message': 'Hello from product router!'}
