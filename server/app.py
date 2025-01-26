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
        sellers = [seller.to_dict() for seller in User.query.all()]
        if not sellers:
            return make_response(jsonify([]), 200)
        return make_response(jsonify(sellers), 200)
    
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

