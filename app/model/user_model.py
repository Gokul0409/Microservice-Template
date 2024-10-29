from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserModel(Base):

    """
    UserModel : Sqlalchemy UserModel ORM Class to create new table
    """

    __tablename__ = "people"

    sn = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
