from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import ForeignKey
from sqlalchemy.orm import validates
from datetime import datetime

from config import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    about_me = db.Column(db.String)
    profile_image = db.Column(db.String)
    _password_hash = db.Column(db.String, unique=True, nullable=False)
    
    library = db.relationship('UserLibrary', back_populates='user')
    user_shopping_cart = db.relationship('ShoppingCart', back_populates='user')
    
    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("Validation Failed: Please enter a valid email address")
        return address
    
    @validates('about_me')
    def validate_about_me_length(self, key, about_me):
        if len(about_me) > 250:
            raise ValueError("Validation Failed: About me must be shorter than 250 characters")
        return about_me
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))
    
    def __repr__(self):
        return f'id: {self.id}, \
                username: {self.username}, \
                email: {self.email}, \
                about_me: {self.about_me}, \
                profile_image: {self.profile_image}'

class Game(db.Model):
    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    game_image = db.Column(db.String, nullable=False)
    carousel_image = db.Column(db.String)
    game_trailer = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    
    user_library = db.relationship('UserLibrary', back_populates='game')
    platforms = db.relationship('GamePlatform', back_populates='game')
    cart_item = db.relationship('CartItem', back_populates='game')
    
    def __repr__(self):
        return f'id: {self.id}, \
                title: {self.title}, \
                description: {self.description}, \
                genre: {self.genre}, \
                release_date: {self.release_date}, \
                publisher: {self.publisher}, \
                game_image: {self.game_image}, \
                price: {self.price}'

class UserLibrary(db.Model):
    __tablename__ = 'user_library'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    game_id = db.Column(db.Integer, ForeignKey('games.id'))
    
    game = db.relationship('Game', back_populates='user_library')
    user = db.relationship('User', back_populates='library')
    
    def __repr__(self):
        return f'id: {self.id}, user: {self.user}, games: {self.games}'
    
class Platform(db.Model):
    __tablename__ = 'platforms'
    
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String, nullable=False)
    
    platforms = db.relationship('GamePlatform', back_populates='platform')
    
    def __repr__(self):
        return f'ID: {self.id}, \
                Platform: {self.platform}'
    
class GamePlatform(db.Model):
    __tablename__ = 'game_platform'
    
    id = db.Column(db.Integer, primary_key=True)
    platform_id = db.Column(db.Integer, ForeignKey('platforms.id'), nullable=False)
    game_id = db.Column(db.Integer, ForeignKey('games.id'), nullable=False)
    
    game = db.relationship('Game', back_populates='platforms')
    platform = db.relationship('Platform', back_populates='platforms')
    
    def __repr__(self):
        return f'Game: {self.game} \
                Platform: {self.platform}'
    
class ShoppingCart(db.Model):
    __tablename__ = 'shopping_cart'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', back_populates='user_shopping_cart')
    cart_items = db.relationship('CartItem', back_populates='shopping_cart')
    
    def __repr__(self):
        return f'ID: {self.id} \
                Created: {self.created_at} \
                User: {self.user} \
                Items: {self.cart_items}'

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    shopping_cart_id = db.Column(db.Integer, ForeignKey('shopping_cart.id'), nullable=False)
    game_id = db.Column(db.Integer, ForeignKey('games.id'), nullable=False)
    
    shopping_cart = db.relationship('ShoppingCart', back_populates='cart_items')
    game = db.relationship('Game', back_populates='cart_item')
    
    def __repr__(self):
        return f'ID: {self.id} \
                Shopping Cart: {self.shopping_cart} \
                Game: {self.game}'