#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from models import User
# Local imports, 
from config import app, db, api
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Seller(Resource):
    def get(self):

        sellers = User.query.all()
        if not sellers:
            return make_response(jsonify({'count': 0, 'sellers': [] }), 200)

        sellers_with_products = [
            {'id': seller.id,
             'username': seller.username,
             'products': [
                 {'id': product.id,
                  'name': product.name,
                  'description': product.description,
                  'image': product.image,
                  'price': product.price
                  }
                  for product in seller.products
             ],

             }
             for seller in sellers


        ]
        return make_response(jsonify({'count': len(sellers_with_products), 'sellers': sellers_with_products}), 200)
    
class Seller_by_username(Resource):
    def get(self, username):
        seller = User.query.filter(User.username == username).first()
        if not seller:
            return make_response(jsonify({'error': f'Seller with ID: {username} not found.'}), 404)
        return make_response(jsonify(seller.to_dict()), 200)
 
api.add_resource(Seller, '/sellers')
api.add_resource(Seller_by_username, '/sellers/<string:username>')
if __name__ == '__main__':
    app.run(port=5555, debug=True)

# export FLASK_RUN_PORT=5555
# flask run


# sqlite3 /Users/layla/Development/code/se-prep/phase-4/Online_Marketplace/server/instance/app.db