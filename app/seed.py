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

    # Add restaurants
    restaurants = []
    for i in range(10):
        restaurant = Restaurant(
            name=fake.name(),
            price=random.randint(5, 60)
        )
        session.add(restaurant)
        restaurants.append(restaurant)

    # Add and commit all restaurants at once
    # session.bulk_save_objects(restaurants)
    session.commit()

     # Add customers
    customers = []
    for i in range(10):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer) 
        customers.append(customer)

    # session.bulk_save_objects(customers)
    session.commit()

    # Add reviews 
    reviews = []
    for restaurant in restaurants:
        for customer in customers:
            review = Review(
                star_rating=random.randint(0, 10),
                restaurant_id=restaurant.id,
                customer_id=customer.id  # Associate the review with a specific customer
            )
            session.add(review)
            reviews.append(review)

    # session.bulk_save_objects(reviews)
    session.commit()
    session.close()
