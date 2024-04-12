from modules.stats.models.stats_queries import model_count_calorie
from configs.configs import con
from sqlalchemy import select, desc, and_, func

async def get_my_calorie_need():
    # Query builder
    query = select(
        model_count_calorie.c.weight, 
        model_count_calorie.c.height,
        model_count_calorie.c.result,
        model_count_calorie.c.created_at
    ).where(
        model_count_calorie.c.created_by == "2d98f524-de02-11ed-b5ea-0242ac120002"
    ).order_by(
        desc(model_count_calorie.c.created_at)
    )

    # Exec
    result = con.execute(query)
    data = result.fetchall()

    res = f"Here is the list of your calorie needed:\n"
    day_before = ''

    for dt in data:    
        res += f"\nWeight / Height : {dt.weight} Kg / {dt.height} Cm\nCount at : {dt.created_at.strftime('%d %b %Y %H:%M')}\n"

    return res