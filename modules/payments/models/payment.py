from configs.configs import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String,DateTime

payment=Table(
    'payment',meta,
    Column('id',String(36),primary_key=True),
    Column('consume_id',String(36),nullable=False),
    Column('payment_method',String(20),nullable=False),
    Column('payment_price',Integer,nullable=True),
    Column('is_payment',Integer,nullable=False),
    Column('created_at',DateTime,nullable=False),
    Column('updated_at',DateTime,nullable=True),
    Column('created_by',String(36),nullable=False),
    Column('updated_by',String(36),nullable=True)
)