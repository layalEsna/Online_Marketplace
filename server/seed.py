#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Product

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        print("Starting seed...")

        # Seed code goes here!

        db.create_all()
        print("Tables created successfully!")

        User.query.delete()
        # Product.query.delete()

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

        # db.session(User(username='bahare', password='Bbbbbbbbb!'))
        # db.session(User(username='loona1', password='Lllllllll!'))
        # db.session(User(username='mishoul', password='Mmmmmmmmm!'))
        # db.session(User(username='derakht', password='Ddddddddd!'))
        # db.session(User(username='aseman', password='Aaaaaaaaa'))

        # db.session.commit()

        # users_data = [
        #     {'username': 'bahare', 'password': 'Bbbbbbbbb!'},
        #     {'username': 'loona1', 'password': 'Lllllllll!'},
        #     {'username': 'mishoul', 'password': 'Mmmmmmmmm!'},
        #     {'username': 'derakht', 'password': 'Ddddddddd!'},
        #     {'username': 'aseman', 'password': 'Aaaaaaaaa!'},
        # ]

        # users = []
        # for user_data in users_data:
        #     user = User(
        #         username=user_data['username'])  
        #     user.password = user_data['password']
            
        #     users.append(user)
        #     db.session.add(user)
        # db.session.commit()
            
            


