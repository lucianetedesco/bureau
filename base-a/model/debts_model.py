from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from model.person_model import Person

Base = declarative_base()


class Debts(Base):
    __tablename__ = 'person_debts'
    id = Column(Integer, primary_key=True)
    value = Column(Float(precision=2), nullable=False)
    description = Column(String(50), nullable=False)
    person_id = Column(Integer, ForeignKey(Person.id))
