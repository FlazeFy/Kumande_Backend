from configs.configs import con
from sqlalchemy import alias, func, text

async def get_my_schedule():
    # Query builder
    sql_query = f"""
        SELECT day, time, GROUP_CONCAT(schedule_consume SEPARATOR ', ') AS schedule_consume
        FROM (
        SELECT 
            REPLACE(JSON_EXTRACT(schedule_time, '$[0].day'), '\"', '') AS day, 
            REPLACE(JSON_EXTRACT(schedule_time, '$[0].category'), '\"', '') AS time,
                schedule_consume
            FROM `schedule`
        ) AS q
        GROUP BY 1, 2
        ORDER BY DAYNAME(1)
    """
    compiled_sql = text(sql_query)

    # Exec
    result = con.execute(compiled_sql)
    data = result.fetchall()

    res = 'Consume Schedule : \n\n'

    for dt in data:
        res += (
            f"Day : <b>{dt.day}</b>\n"
            f"Time : {dt.day}\n"
            f"Consume : {dt.schedule_consume}\n\n"
        )

    return res