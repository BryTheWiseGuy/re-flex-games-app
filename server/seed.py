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
                description="THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
                genre="Action Role-Playing",
                release_date=datetime(
                    year=2022,
                    month=2,
                    day=25
                    ),
                publisher="FromSoftware",
                game_image="https://images.launchbox-app.com/fbd5b4e4-6bce-4f6c-8837-56e109c45349.jpg",
                carousel_image='https://www.magneticmag.com/.image/t_share/MTg5MzAyODE3NjMzMDg1NDA4/thumb-1920-1151249.jpg',
                game_trailer='https://www.youtube.com/embed/qqiC88f9ogU',
                price=69.99
            ),
            Game(
                title="Final Fantasy XVI",
                description="An epic dark fantasy world where the fate of the land is decided by the mighty Eikons and the Dominants who wield them. This is the tale of Clive Rosfield, a warrior granted the title “First Shield of Rosaria” and sworn to protect his younger brother Joshua, the dominant of the Phoenix. Before long, Clive will be caught up in a great tragedy and swear revenge on the Dark Eikon Ifrit, a mysterious entity that brings calamity in its wake.",
                genre="Action Role Playing",
                release_date=datetime(
                    year=2023,
                    month=6,
                    day=22
                    ),
                publisher="Square Enix",
                game_image="https://cdn11.bigcommerce.com/s-6rs11v9w2d/images/stencil/1280x1280/products/2752/13555/FFXVI_Packshot_SQ-500x718_US__23623.1694706908.jpg?c=1",
                carousel_image='https://image.api.playstation.com/vulcan/ap/rnd/202211/3007/JnzRCl2Yj208yuJoSfoGXMGt.jpg',
                game_trailer='https://www.youtube.com/embed/ofWtkPs92Nc?si=IcaBMt5oVDPZqWaV',
                price=69.99
            ),
            Game(
                title="Cyberpunk 2077",
                description="Cyberpunk 2077 is an open-world, action-adventure RPG set in the megalopolis of Night City, where you play as a cyberpunk mercenary wrapped-up in a do-or-die fight for survival. Explore the dark future, now upgraded with next-gen in mind and featuring free additional content!",
                genre="Action Role Playing",
                release_date=datetime(
                    year=2020,
                    month=12,
                    day=10
                    ),
                publisher="CD Projekt Red",
                carousel_image='https://images.gog-statics.com/c75e674590b8947542c809924df30bbef2190341163dd08668e243c266be70c5.jpg',
                game_image="https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Cyberpunk_2077_box_art.jpg/220px-Cyberpunk_2077_box_art.jpg",
                game_trailer='https://www.youtube.com/embed/nLhWWoAaZ0Q?si=yZQT87BLdxeapbF1',
                price=59.99
            ),
            Game(
                title="Starfield",
                description="In this next generation role-playing game set amongst the stars, create any character you want and explore with unparalleled freedom as you embark on an epic journey to answer humanity's greatest mystery.\nIn the year 2330, humanity has ventured beyond our solar system, settling new planets, and living as a spacefaring people. You will join Constellation - the last group of space explorers seeking rare artifacts throughout the galaxy - and navigate the vast expanse of space in Bethesda Game Studios' biggest and most ambitious game.",
                genre="Action Adventure",
                release_date=datetime(
                    year=2023,
                    month=9,
                    day=6
                    ),
                publisher="Bethesda Game Studios",
                carousel_image='https://cdn.mos.cms.futurecdn.net/ijyHy7Lc9shyoJKNSYwN6E.jpg',
                game_image="https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/Bethesda_Starfield.jpg/220px-Bethesda_Starfield.jpg",
                game_trailer='https://www.youtube.com/embed/RDEU8SOtHAI?si=LxBYhvPkd_0uBBrO',
                price=69.99
            ),
            Game(
                title="Baldur's Gate 3",
                description="Gather your party and return to the Forgotten Realms in a tale of fellowship and betrayal, sacrifice and survival, and the lure of absolute power.\nMysterious abilities are awakening inside you, drawn from a mind flayer parasite planted in your brain. Resist, and turn darkness against itself. Or embrace corruption, and become ultimate evil.\nFrom the creators of Divinity: Original Sin 2 comes a next-generation RPG, set in the world of Dungeons & Dragons.",
                genre="Tactical RPG",
                release_date=datetime(
                    year=2023,
                    month=8,
                    day=3
                    ),
                publisher="Larian Studios",
                carousel_image='https://baldursgate3.game/share-page2.jpg',
                game_image="https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Baldur%27s_Gate_3_cover_art.jpg/220px-Baldur%27s_Gate_3_cover_art.jpg",
                game_trailer='https://www.youtube.com/embed/XuCfkgaaa08?si=pUpp2IimPY0oirxa',
                price=59.99
            ),
            Game(
                title="Tears of the Kingdom",
                description="It's a Zelda game!",
                genre="Action Adventure",
                release_date=datetime(
                    year=2023,
                    month=5,
                    day=12
                    ),
                publisher="Nintendo",
                carousel_image='https://images.alphacoders.com/127/1272163.jpg',
                game_image="https://upload.wikimedia.org/wikipedia/en/f/fb/The_Legend_of_Zelda_Tears_of_the_Kingdom_cover.jpg",
                game_trailer='https://www.youtube.com/embed/SSVYVgm4tH4?si=AfSROHeX0TLU_CYE',
                price=59.99
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
        
        db.session.commit()
        print(users_data[0])
        
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
                platform="PlayStation 4"
            ),
            Platform(
                platform="Xbox One"
            ),
            Platform(
                platform="Xbox Series S"
            ),
            Platform(
                platform="Xbox Series X"
            ),
            Platform(
                platform="Microsoft Windows PC"
            ),
            Platform(
                platform="Nintendo Switch"
            ),
            Platform(
                platform="MacOS"
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
                platform_id=2
            ),
            GamePlatform(
                game_id=1,
                platform_id=3
            ),
            GamePlatform(
                game_id=1,
                platform_id=4
            ),
            GamePlatform(
                game_id=1,
                platform_id=5
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
                platform_id=2
            ),
            GamePlatform(
                game_id=3,
                platform_id=1
            ),
            GamePlatform(
                game_id=3,
                platform_id=2
            ),
            GamePlatform(
                game_id=3,
                platform_id=3
            ),
            GamePlatform(
                game_id=3,
                platform_id=4
            ),
            GamePlatform(
                game_id=3,
                platform_id=5
            ),
            GamePlatform(
                game_id=3,
                platform_id=6
            ),
            GamePlatform(
                game_id=4,
                platform_id=1
            ),
            GamePlatform(
                game_id=4,
                platform_id=2
            ),
            GamePlatform(
                game_id=4,
                platform_id=3
            ),
            GamePlatform(
                game_id=4,
                platform_id=4
            ),
            GamePlatform(
                game_id=4,
                platform_id=5
            ),
            GamePlatform(
                game_id=4,
                platform_id=6
            ),
            GamePlatform(
                game_id=5,
                platform_id=1
            ),
            GamePlatform(
                game_id=5,
                platform_id=4
            ),
            GamePlatform(
                game_id=5,
                platform_id=5
            ),
            GamePlatform(
                game_id=5,
                platform_id=6
            ),
            GamePlatform(
                game_id=5,
                platform_id=8
            ),
            GamePlatform(
                game_id=6,
                platform_id=7
            ),
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