#!/usr/bin/env python3

import os
from random import randint, choice as rc
from faker import Faker
from app import app
from datetime import datetime
from models import db, User, Game, UserLibrary, Platform, GamePlatform, ShoppingCart, CartItem

if __name__ == '__main__':
    fake = Faker()
    
    with app.app_context():
        print("Deleting previous seeds...")
        
        Game.query.delete()
        User.query.delete()
        UserLibrary.query.delete()
        Platform.query.delete()
        GamePlatform.query.delete()
        ShoppingCart.query.delete()
        CartItem.query.delete()
        
        print("Running new database seed...")
        
        # Game Seed
        print("Seeding games...")
        games_data=[
            Game(
                title="Elden Ring",
                description="It's a good game!",
                genre="Action Role-Playing",
                release_date=datetime(
                    year=2022,
                    month=2,
                    day=25
                    ),
                publisher="FromSoftware",
                game_image="https://images.launchbox-app.com/fbd5b4e4-6bce-4f6c-8837-56e109c45349.jpg",
                price=69.99
            ),
            Game(
                title="Final Fantasy XVI",
                description="It's a fantasy game!",
                genre="Action Role Playing",
                release_date=datetime(
                    year=2023,
                    month=6,
                    day=22
                    ),
                publisher="Square Enix",
                game_image="https://cdn11.bigcommerce.com/s-6rs11v9w2d/images/stencil/1280x1280/products/2752/13555/FFXVI_Packshot_SQ-500x718_US__23623.1694706908.jpg?c=1",
                price=69.99
            ),
            Game(
                title="Cyberpunk 2077",
                description="It's an action game!",
                genre="Action Role Playing",
                release_date=datetime(
                    year=2020,
                    month=12,
                    day=10
                    ),
                publisher="CD Projekt Red",
                game_image="https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Cyberpunk_2077_box_art.jpg/220px-Cyberpunk_2077_box_art.jpg",
                price=59.99
            ),
            Game(
                title="Starfield",
                description="It's a space game!",
                genre="Action Adventure Space Shooter",
                release_date=datetime(
                    year=2023,
                    month=9,
                    day=6
                    ),
                publisher="Bethesda Game Studios",
                game_image="https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Bethesda_Starfield.jpg/220px-Bethesda_Starfield.jpg",
                price=69.99
            )
        ]
        
        for game in games_data:
            db.session.add(game)
        
        # User Seed
        print("Seeding Users...")
        users_data=[
            User(
                username="gamergirl22",
                email="gamergirl22@gmail.com",
                about_me="I love video games more than anything in the world!!",
                profile_image="https://tinyurl.com/3ue72h4r",
            )
        ]
        
        for user in users_data:
            user.password_hash = 'password'
            db.session.add(user)
        
        # UserLibrary Seed
        print("Seeding User Libraries...")
        
        user_library_data=[
            UserLibrary(user_id=1, game_id=1),
            UserLibrary(user_id=1, game_id=2)
        ]
        
        for library in user_library_data:
            db.session.add(library)
        
        # Platform Seed
        print("Seeding platforms...")
        
        platform_data=[
            Platform(
                platform="PlayStation 5"
            ),
            Platform(
                platform="Xbox Series S"
            ),
            Platform(
                platform="Xbox Series X"
            ),
            Platform(
                platform="Nintendo Switch"
            ),
            Platform(
                platform="MacOS"
            ),
            Platform(
                platform="Microsoft Windows PC"
            ),
            Platform(
                platform="PlayStation 4"
            )
        ]
        
        for platform in platform_data:
            db.session.add(platform)
        
        # GamePlatform Seed
        print("Seeding Game Platform Data...")
        
        game_platform_data = [
            GamePlatform(
                game_id=1,
                platform_id=1
            ),
            GamePlatform(
                game_id=1,
                platform_id=6
            ),
            GamePlatform(
                game_id=2,
                platform_id=1
            ),
            GamePlatform(
                game_id=2,
                platform_id=6
            ),
            GamePlatform(
                game_id=3,
                platform_id=1
            ),GamePlatform(
                game_id=3,
                platform_id=2
            )
        ]
        
        for game_platform in game_platform_data:
            db.session.add(game_platform)
        
        # ShoppingCart Seed
        print("Seeding Shopping Carts...")
        
        shopping_cart_data = [
            ShoppingCart(
                user_id=1,
            )
        ]
        
        for shopping_cart in shopping_cart_data:
            db.session.add(shopping_cart)
        
        # CartItem Seed
        print("Seeding Cart Items...")
        cart_item_data = [
            CartItem(
                shopping_cart_id=1,
                game_id=1
            ),
            CartItem(
                shopping_cart_id=1,
                game_id=3
            )
        ]
        
        for item in cart_item_data:
            db.session.add(item)
        
        db.session.commit()
        
        print("New database seed successful.")