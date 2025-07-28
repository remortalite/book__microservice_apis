from fastapi import FastAPI

from orders.api import api

app = FastAPI()

app.include_router(api.app)

