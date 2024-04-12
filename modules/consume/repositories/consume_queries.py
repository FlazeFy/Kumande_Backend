from modules.consume.models.consume_queries import model_get_consume_history
from configs.configs import con
from sqlalchemy import select, desc, and_, func

async def get_all_consume():
    # Query builder
    query = select(
        model_get_consume_history.c.consume_name, 
        model_get_consume_history.c.consume_type,
        model_get_consume_history.c.consume_from,
        model_get_consume_history.c.consume_comment,
        model_get_consume_history.c.is_favorite,
        model_get_consume_history.c.created_at
    ).where(
        and_(
            model_get_consume_history.c.created_by == "2d98f524-de02-11ed-b5ea-0242ac120002",
            model_get_consume_history.c.deleted_at.is_(None) 
        )
    ).order_by(
        desc(model_get_consume_history.c.created_at),
        desc(model_get_consume_history.c.consume_name),
    )

    # Exec
    result = con.execute(query)
    data = result.fetchall()

    res = f"Here is the list of your consume history:\n"
    day_before = ''

    for dt in data:    
        if day_before == '' or day_before != dt.created_at.strftime('%d %b %Y'):
            day_before = dt.created_at.strftime('%d %b %Y')
            res += f"\n"+day_before+"\n"
            date = dt.created_at.strftime('%H:%M')
        else: 
            date = dt.created_at.strftime('%H:%M')
                
        if dt.is_favorite == 1:
            res += f"- ❤️ "
        else: 
            res += f"-"

        res += f"{dt.consume_name} ({dt.consume_type}) from {dt.consume_from} at {date}\n"
        
        if dt.consume_comment is not None:
            res += f"Notes : {dt.consume_comment}\n"

    return res