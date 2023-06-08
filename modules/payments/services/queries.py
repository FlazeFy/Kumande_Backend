from fastapi import FastAPI
from modules.payments.models.payment import payment
from configs.configs import con
app = FastAPI()

async def getAllPayment():
    data=con.execute(payment.select()).fetchall()
    return {
        "success": True,
        "message": "Data retrived",
        "data":data
    }