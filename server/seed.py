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
        print("Starting seed...")
        # Seed code goes here!

        User.query.delete()
        Product.query.delete()

        users_data = [
            {'username': 'bahare', 'password': 'Bbbbbbbbb!'},
            {'username': 'loona1', 'password': 'Lllllllll!'},
            {'username': 'mishoul', 'password': 'Mmmmmmmmm!'},
            {'username': 'derakht', 'password': 'Ddddddddd!'},
            {'username': 'aseman', 'password': 'Aaaaaaaaa!'},
        ]

        users = []
        for user_data in users_data:
            user = User(
                username=user_data['username'])  
            user.password = user_data['password']
            
            users.append(user)
            db.session.add(user)
        db.session.commit()
            
            


