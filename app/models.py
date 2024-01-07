#!/usr/bin/env python3
from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (CheckConstraint, UniqueConstraint,
    Column, Integer, String)

engine = create_engine('sqlite:///restaurants.db')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"
    # __table_args__ = (
        
    # )

    id = Column(Integer(), primary_key=True)
    name = (String)
    price = (Integer)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = (String)
    last_name = (String)

