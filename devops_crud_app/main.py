from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from devops_crud_app.orders.routers import router as orders_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)

app.include_router(orders_router)
