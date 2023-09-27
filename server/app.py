from flask import request, session, send_from_directory, redirect, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api
# Add your model imports
from models import User, Game, Platform, UserLibrary, ShoppingCart, CartItem, GamePlatform

# Views go here!
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        password = data.get('password')
        username = data.get('username')
        
        if 'username' not in data or 'password' not in data:
            return {"message": "400: Bad Request - Missing username or password"}, 400
        
        user = User.query.filter(User.username == username).first()
        if user and user.authenticate(password):
            session['user_username'] = user.username
            return user.to_dict(), 200
        else:
            return {"message": "401: Login failed"}, 401

class UserLogout(Resource):
    def delete(self):
        session['user_username'] = None
        return {"message": "204: Logout successful"}, 204

class UserSignUp(Resource):
    def post(self):
        json_data = request.get_json()

        user = User(
            username = json_data.get('username'),
            email = json_data.get('email'),
            about_me = json_data.get('about_me'),
            profile_image = json_data.get('profile_image')
        )

        user.password_hash = json_data.get('password')
        db.session.add(user)
        
        try:
            db.session.commit()
            return {"message": "201: Account created"}, 201
        except IntegrityError as e:
            db.session.rollback()
            return {"message": "422: Unprocessable Entity"}, 422

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.username == session.get('user_username')).first()
        if user:
            return user.to_dict(), 200
        else:
            return {"message": "401: Unauthorized"}, 401

class HomePageResource(Resource):
    def server_react_app():
        return send_from_directory('/client/public', 'index.html')


class GamesIndexResource(Resource):
    def get(self):
        games = [game.to_dict() for game in Game.query.all()]
        return games, 200
        
@app.before_request
def check_if_member():
    def increment_games_counter():
        session['games_viewed'] = session.get('games_viewed', 0) + 1
    if not session.get('user_username') \
        and request.endpoint in ['/games/<int:id']:
            increment_games_counter()
            if session['games_viewed'] > 5:
                return redirect(url_for('account_signup'))

class GameByIDResource(Resource):
    def get(self, id):
        game = Game.query.filter(Game.id == id).first()       
        if game:
            return game.to_dict(), 200
        else:
            return {"message": "404: Game not found"}, 404

class GamePlatformsResource(Resource):
    def get(self):
        platforms = [platform.to_dict() for platform in Platform.query.all()]
        
        return platforms, 200

class GamePlatformsForGameResource(Resource):
    def get(self, game_id):
        platforms = Platform.query.join(GamePlatform).filter(GamePlatform.game_id == game_id).all()        
        platform_dict = [platform.to_dict for platform in platforms]
        
        return platform_dict, 200                  

class GamesForPlatformResource(Resource):
    def get(self, platform):
        games = Game.query.join(GamePlatform).join(Platform).filter(Platform.platform == platform).all()
        game_dict = [game.to_dict() for game in games]
        
        return game_dict, 200

class UsersResource(Resource):
    def get(self):
        if 'user_username' in session:
            users = [user.to_dict() for user in User.query.all()]
            return users, 200
        else:
            return {"message": "401: Unauthorized"}, 401

class UserByUsernameResource(Resource):
    def get(self, username):
        if 'user_username' in session:
            logged_in_username = session['user_username']
            if logged_in_username == username:
                user = User.query.filter_by(username=username).first()
                if user:
                    return user.to_dict(), 200
            else:
                user = User.query.filter_by(username=username).first()
                if user:
                    profile_data = {
                        "username": user.username,
                        "about_me": user.about_me,
                        "profile_image": user.profile_image
                    }
                    return profile_data, 200
        else:        
            return {"message": "401: Unauthorized"}, 401
    
    def patch(self, username):
        if 'user_username' not in session:
            return {"message": "401: Unauthorized"}, 401
        
        if session.get('username') != username:
            return {"message": "403: Forbidden"}, 403
        
        user = User.query.filter(User.username == username).first()
        
        if not user:
            return {"message": "404: User not found"}, 404
        
        allowed_attributes = ['email', 'about_me', 'username', 'profile_image']
        
        for attr in request.form:
            if attr in allowed_attributes:
                setattr(user, attr, request.form(attr))
            else:
                return {"message": f"400: Attribute '{attr}' cannot be changed"}, 400
        
        db.session.add(user)
        
        try:
            db.session.commit()
            return {"message": f"200: '{attr}' successfully updated"}, 200
        except IntegrityError as e:
            db.session.rollback()
            return {"message": "422: Change Unsuccessful"}, 422
    
    def delete(self, username):
        if 'user_username' not in session:
            return {"message": "401: Unauthorized"}, 401
        
        if session.get('username') != username:
            return {"message": "403: Forbidden"}, 403
        
        user = User.query.filter(User.username == username).first()
        
        if not user:
            return {"message": "404: User not found"}, 404
        
        db.session.delete(user)
        
        try:
            db.session.commit()
            return {"message": f"200: Account successfully deleted"}, 200
        except IntegrityError as e:
            db.session.rollback()
            return {"message": "500: Internal Server Error"}, 500

class UserLibraryByUsernameResource(Resource):
    def get(self):
        user = User.query.filter(User.username == session.get('user_username')).first()
        
        if user:
            user_library = UserLibrary.query.filter(UserLibrary.user_id == user.id).first()
            
            if user_library:
                user_library_games = [game.to_dict() for game in user_library]
                return user_library_games, 200
            else:
                return {"message": "404: User library not found."}, 404
        else:
            return {"message": "401: Unauthorized"}, 401
    
    def post(self, username):
        user = User.query.filter(User.username == username).first()
        game_id = request.get_json()['game_id']
        game = Game.query.get(game_id)
        
        if user:
            if not UserLibrary.query.filter_by(user_id = user.id, game_id = game.id).first():
                user_library_entry = UserLibrary(user_id = user.id, game_id = game.id)
                db.session.add(user_library_entry)
                db.session.commit()
                return {"message": "201: Game successfully added to library"}, 201
            else:
                return {"message": "400: Game currently in library"}, 400
        else:
            return {"message": "401: Unauthorized"}, 404
    
    def delete(self):
        user = User.query.filter(User.username == session.get('user_username')).first()
        game_id = request.get_json()['game_id']        
        game = Game.query.get(game_id)
        
        if user:
            user_library_entry = UserLibrary.query.filter_by(user_id = user.id, game_id = game.id).first()
            
            if user_library_entry:
                db.session.delete(user_library_entry)
                db.session.commit()
                return {"message": "Game successfully deleted from library"}, 204
            else:
                return {"message": "404: Unable to locate game in library"}, 404
        else:
            return {"message": "401: Unauthorized."}, 401

class UserShoppingCartResource(Resource):
    def get(self):
        user = User.query.filter(User.username == session.get('user_username')).first()
        user_shopping_cart = ShoppingCart.query.filter(ShoppingCart.user_id == user.id).first()
        
        if user_shopping_cart:
            shopping_cart_items = [item.to_dict() for item in user_shopping_cart.cart_items]
            return shopping_cart_items, 200
        else:
            return {"message": "404: Shopping cart not found"}, 404
    
    def post(self):
        user = User.query.filter(User.username == session.get('user_username')).first()
        game_id = request.get_json()['game_id']
        game = Game.query.get(game_id)
        user_shopping_cart = ShoppingCart.query.filter(ShoppingCart.user_id == user.id).first()
        
        if user_shopping_cart:
            new_cart_item = CartItem(shopping_cart_id=user_shopping_cart.id, game_id=game.id)
            db.session.add(new_cart_item)
            db.session.commit()
            return {"message": "200: Item successfully added to cart"}, 201
        else:
            return {"message": "401: Unauthorized"}, 401
    
    def delete(self):
        user = User.query.filter(User.username == session.get('user_username')).first()
        game_id = request.get_json()['game_id']
        game = Game.query.get(game_id)
        user_shopping_cart = ShoppingCart.query.filter(ShoppingCart.user_id == user.id).first()
        
        if user_shopping_cart:
            cart_item = CartItem.query.filter(CartItem.game_id == game.id).first()
            db.session.delete(cart_item)
            db.session.commit()
            return {"message": "204: Item successfully removed from shopping cart"}, 204
        else:
            return {"message": "401: Unauthorized"}, 401

class UserCartItemsResource(Resource):
    pass

api.add_resource(HomePageResource, '/')
api.add_resource(UserSignUp, '/account_signup', endpoint='/account_signup')
api.add_resource(UserLogin, '/login', endpoint='/login')
api.add_resource(UserLogout, '/logout', endpoint='/logout')
api.add_resource(CheckSession, '/check_session', endpoint='/check_session')
api.add_resource(UsersResource, '/users', endpoint='/users')
api.add_resource(UserByUsernameResource, '/users/<username>', endpoint='users/<username>')
api.add_resource(UserLibraryByUsernameResource, '/users/<username>/library', endpoint='/users/<username>/library')
api.add_resource(UserShoppingCartResource, '/users/<username>/shopping_cart', endpoint='/users/<username>/shopping_cart')
api.add_resource(UserCartItemsResource, '/users/<username>/shopping_cart/item/<int:id>', endpoint='/users/<username>/shopping_cart/item/<int:id>')
api.add_resource(GamesIndexResource, '/games', endpoint='/games')
api.add_resource(GameByIDResource, '/games/<int:id>', endpoint='/games/<int:id>')
api.add_resource(GamePlatformsResource, '/platforms', endpoint='/platforms')
api.add_resource(GamePlatformsForGameResource, '/games/<int:id>/platforms', endpoint='/games/<int:id>/platforms')
api.add_resource(GamesForPlatformResource, '/platforms/<string:platform>/games', endpoint='/platforms/<platform>/games')

# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

