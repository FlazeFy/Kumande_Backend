from configs.configs import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import String,DateTime,Integer

model_count_calorie=Table(
    'count_calorie',meta,
    Column('weight',Integer),
    Column('height',Integer),
    Column('result',Integer),

    # Props
    Column('created_at',DateTime),
    Column('created_by',String(36)),
)