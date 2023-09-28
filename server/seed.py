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
                game_image="Image here",
                price=49.99
            ),
            Game(
                title="Genshin Impact",
                description="It's a good game!",
                genre="Gacha Game",
                release_date=datetime(
                    year=2020,
                    month=9,
                    day=28
                    ),
                publisher="Mihoyo",
                game_image="Image here",
                price=0.00
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
            user.password_hash = f'{os.urandom(8)}'
            db.session.add(user)
        
        # UserLibrary Seed
        print("Seeding User Libraries...")
        
        user_library_data=[
            UserLibrary(user_id=1, game_id=1),
            UserLibrary(user_id=1, game_id=2)
        ]
        
        for library in user_library_data:
            db.session.add(library)
        
        # # Platform Seed
        # print("Seeding platforms...")
        
        # platform_data=[
        #     Platform(
        #         platform="PlayStation 5"
        #     ),
        #     Platform(
        #         platform="Xbox Series S"
        #     ),
        #     Platform(
        #         platform="Xbox Series X"
        #     ),
        #     Platform(
        #         platform="Nintendo Switch"
        #     ),
        #     Platform(
        #         platform="MacOS"
        #     ),
        #     Platform(
        #         platform="Microsoft Windows PC"
        #     ),
        #     Platform(
        #         platform="PlayStation 4"
        #     )
        # ]
        
        # for platform in platform_data:
        #     db.session.add(platform)
        
        # # GamePlatform Seed
        # print("Seeding Game Platform Data...")
        
        # game_platform_data = [
        #     GamePlatform(
        #         game_id=1,
        #         platform_id=1
        #     )
        # ]
        
        # for game_platform in game_platform_data:
        #     db.session.add(game_platform)
        
        # # ShoppingCart Seed
        # print("Seeding Shopping Carts...")
        
        # shopping_cart_data = [
        #     ShoppingCart(
        #         user_id=1
        #     )
        # ]
        
        # for shopping_cart in shopping_cart_data:
        #     db.session.add(shopping_cart)
        
        # # CartItem Seed
        # print("Seeding Cart Items...")
        # cart_item_data = [
        #     CartItem(
        #         shopping_cart_id=1,
        #         game_id=1
        #     )
        # ]
        
        # for item in cart_item_data:
        #     db.session.add(item)
        
        db.session.commit()
        
        print("New database seed successful.")