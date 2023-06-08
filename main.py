from typing import Union

from fastapi import FastAPI
from configs.configs import con
from modules.payments.models.payment import payment
from modules.payments.services.queries import getAllPayment

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/payment")
async def index():
    data = await getAllPayment()
    return data