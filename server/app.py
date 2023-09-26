from flask import request, session, jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
# Add your model imports
from models import User, Game, Platform, UserLibrary, ShoppingCart, CartItem, GamePlatform

# Views go here!
class UserLogin(Resource):
    pass

class UserLogout(Resource):
    pass

class UserSignUp(Resource):
    pass

class CheckSession(Resource):
    pass

class GamesResource(Resource):
    pass

class GameByIDResource(Resource):
    pass

class GamePlatformsResource(Resource):
    pass

class GamePlatformsForGameResource(Resource):
    pass

class GamesForPlatformResource(Resource):
    pass

class UsersResource(Resource):
    pass

class UserByUsernameResource(Resource):
    pass

class UserLibraryByUsernameResource(Resource):
    pass

class UserShoppingCartResource(Resource):
    pass

class UserCartItemsResource(Resource):
    pass

api.add_resource(UserSignUp, '/account_signup', endpoint='/account_signup')
api.add_resource(UserLogin, '/login', endpoint='/login')
api.add_resource(UserLogout, '/logout', endpoint='/logout')
api.add_resource(CheckSession, '/check_session', endpoint='/check_session')
api.add_resource(UsersResource, '/users', endpoint='/users')
api.add_resource(UserByUsernameResource, '/users/<username>', endpoint='users/<username>')
api.add_resource(UserLibraryByUsernameResource, '/users/<username>/library', endpoint='/users/<username>/library')
api.add_resource(UserShoppingCartResource, '/users/<username>/shopping_cart', endpoint='/users/<username>/shopping_cart')
api.add_resource(UserCartItemsResource, '/users/<username>/shopping_cart/item/<int:id>', endpoint='/users/<username>/shopping_cart/item/<int:id>')
api.add_resource(GamesResource, '/games', endpoint='/games')
api.add_resource(GameByIDResource, '/games/<int:id>', endpoint='/games/<int:id>')
api.add_resource(GamePlatformsResource, '/platforms', endpoint='/platforms')
api.add_resource(GamePlatformsForGameResource, '/games/<int:id>/platforms', endpoint='/games/<int:id>/platforms')
api.add_resource(GamesForPlatformResource, '/platforms/<platform>/games', endpoint='/platforms/<platform>/games')

# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

