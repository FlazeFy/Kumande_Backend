from pydantic import BaseModel

class Payment(BaseModel):
    id:str
    consume_id:str
    payment_method:str
    payment_price:str
    is_payment:int
    created_at:str
    updated_at:str
    created_by:str
    updated_by:str