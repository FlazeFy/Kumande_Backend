from configs.configs import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,DateTime,Date

model_user_profile=Table(
    'user',meta,
    Column('id',String(36),primary_key=True),
    Column('fullname',String(50)),
    Column('username',String(35)),
    Column('email',String(75)),
    Column('gender',String(6)),
    Column('image_url',String(255),nullable=True),
    Column('born_at',Date,nullable=True),

    # Props
    Column('created_at',DateTime),
    Column('updated_at',DateTime,nullable=True),
)