#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from models import User, Product
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
             ]

             }
             for seller in sellers
        ]

        return make_response(jsonify({'count': len(sellers_with_products), 'sellers': sellers_with_products}), 200)
    
class SellerByUsername(Resource):
    def get(self, username):
        seller = User.query.filter(User.username == username).first()
        if not seller:
            return make_response(jsonify({'error': f'Seller with ID: {username} not found.'}), 404)
        return make_response(jsonify(seller.to_dict()), 200)
    
class UpdateDelete(Resource):
    
    def patch(self, username, product_id):
                
        data = request.get_json()
        
        password = data.get('password')

        seller = User.query.filter(User.username == username).first()
        if not seller:
            return make_response(jsonify({'error': f'No seller with username: {username} found.'}), 404)
        

        if not password or not seller.check_password(password):
            return make_response(jsonify({'error': 'Username and password not match'}), 401)
        
        product = Product.query.filter(Product.id==product_id, Product.user_id==seller.id).first()
        if not product:
            return make_response(jsonify({'error': f'Product with ID: {product_id} not found for this seller.'}), 404)
        
        fieldes_to_update = ['name', 'description', 'image', 'price']       
        for attr in fieldes_to_update:
            if attr in data:
                setattr(product, attr, data[attr])
        db.session.commit()
        return make_response(jsonify(product.to_dict()), 200)

class PasswordAuthentication(Resource):
    def post(self, username):
        data = request.get_json()  
        password = data.get('password')

        user = User.query.filter(User.username == username).first()
        if not user:
            return make_response(jsonify({'error': 'User not found.'}), 400)
        if not user.check_password(password):
            return make_response(jsonify({'error': 'Password did not match.'}), 401)
        return make_response(jsonify({'message': 'Successfull authentication.'}), 200)
        


api.add_resource(Seller, '/sellers')
api.add_resource(SellerByUsername, '/sellers/<string:username>')
api.add_resource(UpdateDelete, '/sellers/<string:username>/<int:product_id>')
api.add_resource(PasswordAuthentication, '/sellers/<string:username>/authentication')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

# export FLASK_RUN_PORT=5555
# flask run


# sqlite3 /Users/layla/Development/code/se-prep/phase-4/Online_Marketplace/server/instance/app.db