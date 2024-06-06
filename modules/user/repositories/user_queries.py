from modules.user.models.user import model_user_profile
from configs.configs import con
from sqlalchemy import select, desc, and_, func

async def get_my_profile():
    # Query builder
    query = select(
        model_user_profile.c.fullname, 
        model_user_profile.c.username,
        model_user_profile.c.email, 
        model_user_profile.c.gender, 
        model_user_profile.c.image_url, 
        model_user_profile.c.born_at, 
        model_user_profile.c.created_at, 
        model_user_profile.c.updated_at,  
    ).where(
        model_user_profile.c.id == "2d98f524-de02-11ed-b5ea-0242ac120002"
    )

    # Exec
    result = con.execute(query)
    data = result.first()

    res = (
        f"<b>Here is your profile:</b>\n"
        f"\nFullname : {data.fullname}\n"
        f"Username : {data.username}\n"
        f"Email : {data.email}\n"
        f"Gender : {data.gender}\n"
        f"Born At : {data.born_at.strftime('%d %B %Y') if data.born_at else '-'}\n\n"
        f"<b>Props:</b>\n"
        f"Created At : {data.created_at.strftime('%d %B %Y %H:%M')}\n"
        f"Updated At : {data.updated_at.strftime('%d %B %Y %H:%M') if data.updated_at else '-'}\n"
        )

    return res