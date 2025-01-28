#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Product, Purchase

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        print("Starting seed...")

        # Seed code goes here!

        db.create_all()
        print("Tables created successfully!")

        User.query.delete()
        Product.query.delete()
        Purchase.query.delete()

        users = [
            User(username='bahare', password='Bbbbbbbbb!'),
            User(username='loona1', password='Lllllllll!'),
            User(username='mishoul', password='Mmmmmmmmm!'),
            User(username='derakht', password='Ddddddddd!'),
            User(username='aseman', password='Aaaaaaaaa!')
        ]

        db.session.add_all(users)
        db.session.commit()
        print('seeding completes')

        products = [
            Product(name='Laptop', description='A high-performance laptop.', image='laptop.jpg', price=999.99, user_id=1),
            Product(name='Headphones', description='Noise-cancelling headphones.', image='headphones.jpg', price=199.99, user_id=1),
            Product(name='Smartphone', description='Latest smartphone model.', image='smartphone.jpg', price=799.99, user_id=2),
            Product(name='Backpack', description='Durable and waterproof backpack.', image='backpack.jpg', price=99.99, user_id=2),
            Product(name='Smartwatch', description='Stylish smartwatch with health tracking.', image='smartwatch.jpg', price=299.99, user_id=3),
            Product(name='Keyboard', description='Mechanical keyboard with RGB lighting.', image='keyword.jpg', price=199.99, user_id=3),
            Product(name='Mouse', description='Ergonomic wireless mouse.', image='mouse.jpg', price=99.99, user_id=4),
            Product(name='Monitor', description='4K ultra-wide monitor.', image='monitor.jpg', price=399.99, user_id=4),
            Product(name='Tablet', description='Lightweight tablet for work and play.', image='tablet.jpg', price=499.99, user_id=5),
            Product(name='Camera', description='DSLR camera for photography enthusiasts.', image='camera.jpg', price=699.99, user_id=5),
        ]
        db.session.add_all(products)
        db.session.commit()
        