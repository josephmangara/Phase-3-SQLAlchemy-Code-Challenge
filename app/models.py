#!/usr/bin/env python3
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (CheckConstraint,
    Column, Integer, ForeignKey, String)

engine = create_engine('sqlite:///restaurants.db')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer(), primary_key=True)
    name = (String)
    price = (Integer)

    reviews = relationship('Review', backref=backref('restaurant'))

    def __repr__(self):
        return f'Restaurant(id={self.id}, ' + \
            f'name="{self.name}", ' + \
            f'price="{self.price})"'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = (String)
    last_name = (String)

    reviews = relationship('Review', backref=backref('customer'))

    def __repr__(self):
        return f'Customer(id={self.id}, ' + \
            f'first name="{self.first_name}", ' + \
            f'last name="{self.last_name})"'

class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = (
         CheckConstraint('star_rating BETWEEN 0 AND 5', name='star_rating_between_0_and_5')
    )

    id = Column(Integer(), primary_key=True)
    star_rating = (Integer)
    restaurant_id = Column(Integer(), ForeignKey('restuarants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'star rating="{self.star_rating}", ' + \
            f'restuarant id="{self.restaurant_id})"' + \
            f'customer id="{self.customer_id}"'
    
class RestaurantCustomers(Base):
    __tablename__ = "restaurant_customers"

    id = Column(Integer(), primary_key=True)
    restaurant_id = Column(ForeignKey('restaurants.id'))
    customer_id = Column(ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='restaurant_customers')
    customer = relationship('Customer', back_populates='restaurant_customers')
    
    def __repr__(self):
        return f'RestaurantCustomers(restaurant_id={self.restaurant_id}, ' +\
            f'customer_id={self.customer_id})'
