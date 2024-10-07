from sqlalchemy import Column, Integer, String
from main import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(100))
    email = Column(String(100), unique=True)
