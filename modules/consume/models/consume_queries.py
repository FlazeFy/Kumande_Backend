from configs.configs import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,DateTime,SmallInteger

model_get_consume_history=Table(
    'consume',meta,
    Column('id',String(36),primary_key=True),
    Column('slug_name',String(80)),
    Column('consume_type',String(10)),
    Column('consume_name',String(75)),
    Column('consume_from',String(15)),
    Column('consume_comment',String(255),nullable=True),

    # Props
    Column('is_favorite',SmallInteger),
    Column('created_at',DateTime),
    Column('created_by',String(36)),
    Column('deleted_at',DateTime,nullable=True),
)