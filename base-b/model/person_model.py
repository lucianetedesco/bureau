from sqlalchemy import Column, Integer, Date, Float
from sqlalchemy.ext.declarative import declarative_base

from database.crypt_column import CryptColumn

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(CryptColumn(150), nullable=False)
    birth = Column(Date(), nullable=False)
    document = Column(CryptColumn(50), nullable=False)
    wage = Column(Float(precision=2), nullable=False)
    address = Column(CryptColumn(200), nullable=False)
