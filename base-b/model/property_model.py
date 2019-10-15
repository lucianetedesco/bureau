from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from database.crypt_column import CryptColumn
from model.person_model import Person

Base = declarative_base()


class Property(Base):
    __tablename__ = 'person_property'
    id = Column(Integer, primary_key=True)
    value = Column(Float(precision=2), nullable=False)
    description = Column(CryptColumn(200), nullable=False)
    person_id = Column(Integer, ForeignKey(Person.id))
