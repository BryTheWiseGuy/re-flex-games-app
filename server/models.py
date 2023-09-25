from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import ForeignKey, CheckConstraint, ARRAY, DECIMAL
from sqlalchemy.orm import validates

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    about_me = db.Column(db.String)
    profile_image = db.Column(db.String)
    _password_hash = db.Column(db.String, unique=True, nullable=False)
    
    # user_library = db.relationship('UserLibrary', backpopulates='user')
    
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

class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    game_image = db.Column(db.String, nullable=False)
    price = db.Column(DECIMAL(precision=10, scale=2), nullable=False)
    
    # user_library = db.relationship('UserLibrary', back_populates='game')
    # game_platform = db.relationship('GamePlatform', back_populates='game' )
    
    def __repr__(self):
        return f'id: {self.id}, \
                title: {self.title}, \
                desacription: {self.description}, \
                genre: {self.genre}, \
                release_date: {self.release_date}, \
                publisher: {self.publisher}, \
                game_image: {self.game_image}, \
                price: {self.price}'

# class Platform(db.Model, SerializerMixin):
#     __tablename__ = 'platforms'
    
#     id = db.Column(db.Integer, primary_key=True)
#     platform = db.Column(db.String, nullable=False)
    
#     game_platform = db.relationship('GamePlatform', back_populates='platform')
    
# class GamePlatform(db.Model, SerializerMixin):
#     __tablename__ = 'game_platform'
    
#     id = db.Column(db.Integer, primary_key=True)
#     platform_id = db.Column(db.Integer, ForeignKey('platforms.id'), nullable=False)
#     game_id = db.Column(db.Integer, ForeignKey('games.id'), nullable=False)
    
    # game = db.relationship('Game', back_populates='game_platform')
    # platform = db.relationship('Platform', back_populates='game_platform')
    

# class UserLibrary(db.Model, SerializerMixin):
#     __tablename__ = 'user_library'
    
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
#     game_id = db.Column(db.Integer, ForeignKey('games.id'), nullable=False)
    
#     user = db.relationship('User', back_populates='user_library')
#     game = db.relationship('Game', back_populates='user_library')
    
#     def __repr__(self):
#         return f'id: {self.id}, user: {self.user}, games: {self.games}'
    
# class ShoppingCart(db.Model, SerializerMixin):
#     pass

# class CartGame(db.Model, SerializerMixin):
#     pass

# class LibraryGame(db.Model, SerializerMixin):
#     pass

# # Stretch Goal Models

# class Order(db.Model, SerializerMixin):
#     pass

# class Review(db.Model, SerializerMixin):
    # pass