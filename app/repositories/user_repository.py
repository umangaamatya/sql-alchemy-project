from main import session
from models.user import User
from sqlalchemy import select


def add_user_details(first_name, last_name, email):
    user = User(first_name=first_name, last_name=last_name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)

    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }


def get_user(id):
    stmt = select(User).where(User.id == id)
    user = session.execute(stmt).scalars().first()

    return {
        'ID': user.id,
        'First Name': user.first_name,
        'Last Name': user.last_name,
        'Email': user.email
    }


def get_all_users():
    stmt = select(User).order_by(User.id)
    result = session.execute(stmt).scalars()
    user_list = []

    for user in result:
        user_list.append(
            {
                'ID': user.id,
                'First Name': user.first_name,
                'Last Name': user.last_name,
                'Email': user.email
            }
        )
    return user_list


def del_user():
    return
