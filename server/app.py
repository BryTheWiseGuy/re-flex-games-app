from flask import request, session, redirect, url_for, render_template
from flask_restful import Resource
from flask_marshmallow import Marshmallow
from config import app, db, api
from models import User, Game, Platform, UserLibrary, ShoppingCart, CartItem, GamePlatform
ma = Marshmallow(app)

# Model Schemas

class User_Schema(ma.SQLAlchemySchema):   
    class Meta:
        model = User
    
    id = ma.auto_field()
    username = ma.auto_field()
    about_me = ma.auto_field()
    profile_image = ma.auto_field()
    email = ma.auto_field()
    library = ma.Pluck("User_Library_Schema", 'game', many=True)
    user_shopping_cart = ma.Pluck("Shopping_Cart_Schema", "cart_items", many=True)

singular_user_schema = User_Schema()
multiple_user_schema = User_Schema(many=True)

class Game_Schema(ma.SQLAlchemySchema):   
    class Meta:
        model = Game
    
    id = ma.auto_field()
    title = ma.auto_field()
    description = ma.auto_field()
    genre = ma.auto_field()
    release_date = ma.auto_field()
    publisher = ma.auto_field()
    game_image = ma.auto_field()
    carousel_image = ma.auto_field()
    game_trailer = ma.auto_field()
    price = ma.auto_field()
    platforms = ma.Pluck("Game_Platform_Schema", 'platform', many=True)
    
singular_game_schema = Game_Schema()
multiple_game_schema = Game_Schema(many=True)

class User_Library_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = UserLibrary
    
    id = ma.auto_field()
    game = ma.Nested(singular_game_schema)
    
user_library_schema = User_Library_Schema()

class Platform_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = Platform
        
    id = ma.auto_field()
    platform = ma.auto_field()
    
singular_platform_schema = Platform_Schema()
multiple_platform_schema = Platform_Schema(many=True)

class Game_Platform_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = GamePlatform
        
    id = ma.auto_field()
    game = ma.Nested(singular_game_schema)
    platform = ma.Nested(singular_platform_schema)

singular_game_platform_schema = Game_Platform_Schema()
multiple_game_platform_schema = Game_Platform_Schema(many=True)

class Shopping_Cart_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = ShoppingCart
    
    id = ma.auto_field()
    cart_items = ma.Nested("Cart_Item_Schema", many=True)

shopping_Cart_Schema = Shopping_Cart_Schema()

class Cart_Item_Schema(ma.SQLAlchemySchema):
    class Meta:
        model = CartItem
    
    id = ma.auto_field()
    shopping_cart_id = ma.auto_field()
    game = ma.Nested(singular_game_schema)

singular_cart_item_schema = Cart_Item_Schema()
multiple_cart_item_schema = Cart_Item_Schema(many=True)
    
# API Resources

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")

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
            return singular_user_schema.dump(user), 200
        else:
            return {"message": "401: Login failed"}, 401

class UserLogout(Resource):
    def delete(self):
        session['user_username'] = None
        return {"message": "204: Logout successful"}, 204

class UserSignUp(Resource):
    def post(self):
        json_data = request.get_json()

        if not json_data.get('username'):
            return {"error": "400: Bad Request",
                    "message": "Please provide a valid username"}, 400
        
        if not json_data.get("email"):
            return {"error": "400: Bad Request",
                    "message": "Please provide a valid email address."}, 400
            
        if not json_data.get('password'):
            return {"error": "400: Bad Request",
                    "message": "Please enter a valid password"}
        
        user = User(
            username = json_data.get('username'),
            email = json_data.get('email'),
        )
        
        if json_data.get('password') == json_data.get('confirmed_password'):
            user.password_hash = json_data.get('password')
        else:
            return {"error": "400: Bad Request",
                    "message": "Passwords Do Not Match"}  

        db.session.add(user)
        db.session.commit()
        
        user_shopping_cart = ShoppingCart(user_id=user.id)
        library = UserLibrary()
        
        db.session.add(user_shopping_cart)
        db.session.add(library)
        
        db.session.commit()
        
        session['user_username'] = user.username
        
        return singular_user_schema.dump(user), 201

class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.username == session.get('user_username')).first()
        if user:
            return singular_user_schema.dump(user), 200
        else:
            return {"message": "401: Unauthorized"}, 401

class GamesIndexResource(Resource):
    def get(self):
        games = Game.query.all()
        return multiple_game_schema.dump(games), 200
        
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
            return singular_game_schema.dump(game), 200
        else:
            return {"message": "404: Game Not Found"}, 404

class GamePlatformsResource(Resource):
    def get(self):
        platforms = Platform.query.all()
        
        return multiple_platform_schema.dump(platforms), 200

class GamePlatformsForGameResource(Resource):
    def get(self, id):
        games = GamePlatform.query.filter(GamePlatform.game_id == id).all()        
        
        return [singular_platform_schema.dump(game.platform) for game in games], 200

class GamesForPlatformResource(Resource):
    def get(self, id):
        games = Game.query.join(GamePlatform).join(Platform).filter(Platform.id == id).all()
        
        return [singular_game_schema.dump(game) for game in games], 200
    
class UsersResource(Resource):
    def get(self):
        if 'user_username' in session:
            users = User.query.all()
            return multiple_user_schema.dump(users), 200
        else:
            return {"message": "401: Unauthorized"}, 401

class UserByUsernameResource(Resource):
    def get(self):
        user = User.query.filter(User.username==session.get('user_username')).first()
        
        if user:
            return singular_user_schema.dump(user), 200
        else:
            response = {"message": "401: Unauthorized"}, 401
            response.headers['Location'] = '/login'        
            return response
    
    def patch(self, username):
        user = User.query.filter(User.username == username).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        allowed_attributes = ['email', 'about_me', 'username', 'profile_image']
        
        for attr in request.json:
            if attr in allowed_attributes:
                setattr(user, attr, request.json[attr])
            else:
                return {"message": f"400: Invalid Attribute"}, 400
        
        db.session.add(user)
        db.session.commit()
        
        return singular_user_schema.dump(user), 200
    
    def delete(self, username):
        user = User.query.filter(User.username == username).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        UserLibrary.query.filter(UserLibrary.user_id==user.id).delete()
        ShoppingCart.query.filter(ShoppingCart.user_id==user.id).delete()

        db.session.delete(user)
        
        db.session.commit()
        return {"message": f"200: Account successfully deleted"}, 200

class UserLibraryByUsernameResource(Resource):
    def get(self, username):
        user = User.query.filter(User.username == session.get('user_username')).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        if user:
            user_library = UserLibrary.query.join(Game).filter(UserLibrary.user_id == user.id).all()

            if user_library:
                return [singular_game_schema.dump(game.game) for game in user_library], 200
            else:
                return {"message": "404: Library Not Found."}, 404
        else:
            return {"message": "401: Unauthorized"}, 401
    
    def post(self, username):
        user = User.query.filter(User.username == session.get('user_username')).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        game_id = request.get_json()['game_id']
        game = Game.query.get(game_id)
        
        if user:
            if not UserLibrary.query.filter_by(user_id = user.id, game_id = game.id).first():
                user_library_entry = UserLibrary(user_id = user.id, game_id = game.id)
                db.session.add(user_library_entry)
                db.session.commit()
                return {"message": "201: Game successfully added to library"}, 201
            else:
                return {"message": "400: Game already in library"}, 400
        else:
            return {"message": "404: User not found"}, 404

class DeleteUserLibraryEntry(Resource):   
    def delete(self, username, game_id):       
        user = User.query.filter(User.username == session.get('user_username')).first()
        user_library_entry = UserLibrary.query.filter(UserLibrary.game_id == game_id).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        db.session.delete(user_library_entry)
        db.session.commit()
        
        return singular_user_schema.dump(user), 200

class UserShoppingCartResource(Resource):
    def get(self, username):
        user = User.query.filter(User.username == session.get('user_username')).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        user_shopping_cart = ShoppingCart.query.filter(ShoppingCart.user_id == user.id).first()
        
        if user_shopping_cart:
            return [singular_cart_item_schema.dump(item) for item in user_shopping_cart.cart_items], 200
        else:
            return {"message": "404: Cart Not Found"}, 404
    
    def post(self, username):
        user = User.query.filter(User.username == session.get('user_username')).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        game_id = request.get_json()['game_id']
        game = Game.query.get(game_id)
        user_shopping_cart = ShoppingCart.query.filter(ShoppingCart.user_id == user.id).first()
        
        if user_shopping_cart:
            new_cart_item = CartItem(shopping_cart_id=user_shopping_cart.id, game_id=game.id)
            db.session.add(new_cart_item)
            db.session.commit()
            return {"message": "200: OK"}, 201
        else:
            return {"message": "401: Unauthorized"}, 401

class UserCartItemsResource(Resource):

    def post(self, username):
        user = User.query.filter(User.username == session.get('user_username')).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        data = request.get_json()
        game_id = data.get('game_id')
        
        game = Game.query.get(game_id)
        if not game:
            return {"message": "404: Game not found"}, 404
        
        user_shopping_cart = ShoppingCart.query.filter(ShoppingCart.user_id == user.id).first()
        if not user_shopping_cart:
            return {"message": "404: Cart Not Found"}, 404
        if CartItem.query.filter_by(shopping_cart_id=user_shopping_cart.id, game_id=game.id).first():
            return {"message": "400: Game Already Exists"}, 400
        
        new_cart_item = CartItem(shopping_cart_id=user_shopping_cart.id, game_id=game.id)
        
        db.session.add(new_cart_item)
        db.session.commit()
        return {"message": "200: OK"}, 200
    
    def delete(self, username):
        user = User.query.filter(User.username == username).first()
        
        check_for_authorization_and_authentication(session, username, user)
        
        data = request.get_json()
        game_id = data.get('game_id')
        
        game = Game.query.get(game_id)
        if not game:
            return {"message": "404: Game Not Found"}, 404
        
        user_shopping_cart = ShoppingCart.query.filter(ShoppingCart.user_id == user.id).first()
        if not user_shopping_cart:
            return {"message": "404: Cart Not Found"}, 404
        if not CartItem.query.filter_by(shopping_cart_id=user_shopping_cart.id, game_id=game.id).first():
            return {"message": "404: Game Not Found"}, 404
        
        cart_item = CartItem.query.filter_by(shopping_cart_id=user_shopping_cart.id, game_id=game.id).first()
        
        db.session.delete(cart_item)
        db.session.commit()
        
        return singular_user_schema.dump(user), 200
    
@app.route('/checkout/<int:cart_id>')
def checkout(cart_id):
    shopping_cart = ShoppingCart.query.filter(ShoppingCart.id == cart_id).first()
    shopping_cart_items = shopping_cart.cart_items
    
    for item in shopping_cart_items:
        user_library_entry = UserLibrary(user_id = shopping_cart.user_id, game_id = item.game_id)
        db.session.add(user_library_entry)
        
        db.session.delete(item)
        db.session.commit()
    
    user = User.query.filter(User.id == shopping_cart.user_id).first()
    
    return singular_user_schema.dump(user), 200
            
# API Endpoints

api.add_resource(UserSignUp, '/api/account_signup', endpoint='account_signup')
api.add_resource(UserLogin, '/api/login', endpoint='login')
api.add_resource(UserLogout, '/api/logout', endpoint='logout')
api.add_resource(CheckSession, '/api/check_session', endpoint='check_session')
api.add_resource(UsersResource, '/api/users', endpoint='users')
api.add_resource(UserByUsernameResource, '/api/users/<username>')
api.add_resource(UserLibraryByUsernameResource, '/api/users/<username>/library')
api.add_resource(DeleteUserLibraryEntry, '/api/users/<username>/library/<int:game_id>')
api.add_resource(UserShoppingCartResource, '/api/users/<username>/shopping_cart')
api.add_resource(UserCartItemsResource, '/api/users/<username>/shopping_cart/items')
api.add_resource(GamesIndexResource, '/api/games', endpoint='games')
api.add_resource(GameByIDResource, '/api/games/<int:id>')
api.add_resource(GamePlatformsResource, '/api/platforms', endpoint='platforms')
api.add_resource(GamePlatformsForGameResource, '/api/games/<int:id>/platforms')
api.add_resource(GamesForPlatformResource, '/api/platforms/<int:id>/games')

# Authorization and Authentication Functions

def check_if_authorized(session):
    if 'user_username' not in session:
        return {"message": "401: Unauthorized"}, 401
    else:
        pass

def check_if_session_match(session, username):
    if session.get('user_username') != username:
        return {"message": "403: Forbidden"}, 403
    else:
        pass

def check_if_user(user):
    if not user:
        return {"message": "404: User not found"}, 404
    else:
        pass

def check_for_authorization_and_authentication(session, username, user):
    auth_response = check_if_authorized(session)
    if auth_response:
        return auth_response
    else:
        pass
    session_match_response = check_if_session_match(session, username)
    if session_match_response:
        return session_match_response
    else:
        pass
    check_if_user_response = check_if_user(user)
    if check_if_user_response:
        return check_if_user_response
    else:
        pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)

