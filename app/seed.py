#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Review, Customer

if __name__ == '__main__':
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Restaurant).delete()
    session.query(Review).delete()
    session.query(Customer).delete()

    fake = Faker()

    restaurants = []
    for i in range(10):
        restaurant = Restaurant(
            name=fake.name(),
            price=random.randint(5, 60)
        )
        restaurants.append(restaurant)

    # Add and commit all restaurants at once
    session.bulk_save_objects(restaurants)
    session.commit()

     # Add customers
    customers = []
    for i in range(5):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        customers.append(customer)

    session.bulk_save_objects(customers)
    session.commit()

    # Add reviews 
    reviews = []
    for restaurant in restaurants:
        for i in range(random.randint(0, 5)):
            review = Review(
                star_rating=random.randint(0, 10),
                
                restaurant_id=restaurant.id,
            )
            reviews.append(review)

    session.bulk_save_objects(reviews)
    session.commit()
    session.close()
