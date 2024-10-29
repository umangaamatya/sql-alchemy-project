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


def add_multiple_users(users):
    user_list = []

    for user in users:
        user_details = User(first_name=user["first_name"], last_name=user["last_name"], email=user["email"])
        user_list.append(user_details)

    session.add_all(user_list)
    session.commit()
    session.refresh(user_list)

    return user_list


def get_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()

    if user:
        return {
            'ID': user.id,
            'First Name': user.first_name,
            'Last Name': user.last_name,
            'Email': user.email
        }
    else:
        return {'error': 'User not found'}


def get_all_users():
    users = session.query(User).order_by(User.id).all()
    user_list = [
        {
            'ID': user.id,
            'First Name': user.first_name,
            'Last Name': user.last_name,
            'Email': user.email
        }
        for user in users
    ]

    return user_list


def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()

    if user:
        user_details = {
            'ID': user.id,
            'First Name': user.first_name,
            'Last Name': user.last_name,
            'Email': user.email
        }

        session.delete(user)
        session.commit()

        return user_details
    else:
        return {'error': 'User not found'}


def update_user(user_id, first_name=None, last_name=None, email=None):
    user = session.query(User).filter(User.id == user_id).first()

    if not user:
        return f"User with ID {user_id} does not exist"

    data = {'first_name': first_name, 'last_name': last_name, 'email': email}

    updates = {k: v for k, v in data.items() if v is not None}

    session.query(User).filter(User.id == user_id).update(updates)
    session.commit()
    session.refresh(user)

    user_details = {
        'ID': user.id,
        'First Name': user.first_name,
        'Last Name': user.last_name,
        'Email': user.email
    }

    return user_details
