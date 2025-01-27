from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import validates, relationship
import re
from config import db, bcrypt




class User(db.Model, SerializerMixin):
    """
    User model for storing user data, including a hashed password.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _hash_password = db.Column(db.String(128), nullable=False)

    products = db.relationship('Product', secondary='purchases', back_populates='users', overlaps='purchases', viewonly=True)
    purchases = db.relationship('Purchase', back_populates='user', overlaps='products')
    
    @property
    def password(self):
        raise AttributeError('Password is not readable.')
    
    @password.setter
    def password(self, password):
        pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$')
        if not password or not isinstance(password, str):
            raise ValueError('Password is required and must be a string.')
        if not pattern.match(password):
            raise ValueError('Password must be at least 8 characters long and include one lowercase letter, one uppercase letter, and one symbol.')
        self._hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._hash_password, password)
   
    
    @validates('username')
    def validate_username(self,key, username):
        if not username or not isinstance(username, str):
            raise ValueError('Username is required and must be a string.')
        if len(username) < 5 or len(username) > 50:
            raise ValueError('Username must be between 5 and 50 characters inclusive.')
        return username
    
    serialize_only = ('id', 'username')


class Product(db.Model, SerializerMixin):
    """
    Product model for storing product details, including name, description, image, and price.
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)

    users = db.relationship('User', secondary='purchases', back_populates='products', overlaps='purchases', viewonly=True)
    purchases = db.relationship('Purchase', back_populates='product', overlaps='users')

    @validates('name')
    def validate_name(self, key, name):
        if not name or not isinstance(name, str):
            raise ValueError('Name is required and must be a string.')
        if len(name) > 20:
            raise ValueError('Name must be shorter than 20 characters.')
        return name
    
    @validates('description')
    def validate_description(self, key, description):
        if not description or not isinstance(description, str):
            raise ValueError('Description is required and must be a string.')
        if len(description) > 200:
            raise ValueError('Description must be shorter than 200 characters.')
        return description
    
    @validates('image')
    def validate_image(self, key, image):
        if image is not None and not isinstance(image, str):
            raise ValueError('Image must be a string.')
        return image
    
    @validates('price')
    def validate_price (self, key, price ):
        if not price or not isinstance(price, (int, float)) or price <= 0:
            raise ValueError('Price must be a positive float.')
        return price 
    
    serialize_only = ('id', 'name', 'description', 'image', 'price')

class Purchase(db.Model, SerializerMixin):
    """
    Purchase model for storing details of a user's purchase, including the associated user, product, total price, and payment method.
    """
    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    delivery_address = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String, nullable=False)

    user = db.relationship('User', back_populates='purchases', overlaps='products', viewonly=True)
    product = db.relationship('Product', back_populates='purchases', overlaps='users', viewonly=True)

    @validates('total_price')
    def validate_total_price(self, key, total_price):
        if not total_price or not isinstance(total_price, (int, float)):
            raise ValueError('Total price is required and must be a float.')
        if total_price <= 0:
            raise ValueError('Price must be greater than 0.')
        return total_price
    
    @validates('delivery_address')
    def validate_delivery_address(self, key, delivery_address):
        if not delivery_address or not isinstance(delivery_address, str):
            raise ValueError('Delivery address is required and must be a string.')
        if len(delivery_address) > 255:
            raise ValueError('Delivery address must be shorter than 255 characters.')
        return delivery_address
    
    @validates('payment_method')
    def validate_payment_method(self, key, payment_method):
        if not payment_method or not isinstance(payment_method, str):
            raise ValueError('Payment method is required and must be a string.')
        return payment_method
    
    serialize_only = ('id', 'user_id', 'product_id', 'total_price', 'delivery_address', 'payment_method')


    

    

        
   







