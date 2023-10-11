#!/usr/bin/env python3
from app import app
from datetime import datetime
from models import db, User, Game, UserLibrary, Platform, GamePlatform, ShoppingCart, CartItem

if __name__ == '__main__':
    
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
                description="An epic adventure awaits in the Legend of Zelda: Tears of the Kingdom game, only on the Nintendo Switch system. In this sequel to the Legend of Zelda: Breath of the Wild game, you'll decide your own path through the sprawling landscapes of Hyrule and the mysterious islands floating in the vast skies above. Can you harness the power of Link's new abilities to fight back against the malevolent forces that threaten the kingdom?",
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
                price=49.99
            ),
            Game(
                title="Dead Space",
                description="Isaac Clarke is an everyman engineer on a mission to repair a vast mining ship, the USG Ishimura, only to discover something has gone horribly wrong. The ship's crew has been slaughtered and Isaac's beloved partner, Nicole, is lost somewhere on board. Now alone and armed with only his engineering tools and skills, Isaac races to find Nicole as the nightmarish mystery of what happened aboard the Ishimura unravels around him. Trapped with hostile creatures called Necromorphs, Isaac faces a battle for survival, not only against the escalating terrors of the ship but against his own crumbling sanity.",
                genre="Survival Horror",
                release_date=datetime(
                    year=2023,
                    month=1,
                    day=27
                    ),
                publisher="Motive Studio",
                carousel_image='https://theplayeristhething.com/wp-content/uploads/2023/01/1277778-scaled.jpg',
                game_image="https://i0.wp.com/thepopbreak.com/wp-content/uploads/2023/03/FeK7GBvVUAA_OSE.jpg?ssl=1",
                game_trailer='https://www.youtube.com/embed/ctQl9wa3ydE',
                price=59.99
            ),
            Game(
                title="Diablo IV",
                description="The endless battle between the High Heavens and the Burning Hells rages on as chaos threatens to consume Sanctuary. With ceaseless demons to slaughter, countless Abilities to master, nightmarish Dungeons, and Legendary loot, this vast, open world brings the promise of adventure and devastation.",
                genre="Hack and Slash",
                release_date=datetime(
                    year=2023,
                    month=6,
                    day=5
                    ),
                publisher="Blizzard Entertainment",
                carousel_image='https://cdn.cloudflare.steamstatic.com/steam/apps/2344520/capsule_616x353.jpg?t=1696625409',
                game_image="https://upload.wikimedia.org/wikipedia/en/1/1c/Diablo_IV_cover_art.png",
                game_trailer='https://www.youtube.com/embed/tkzbNhdsQ_Y',
                price=59.99
            ),
            Game(
                title="Horizon: Forbidden West",
                description="The land is dying. Vicious storms and an unstoppable blight ravage the scattered remnants of humanity, while fearsome new machines prowl their borders. Life on Earth is hurtling towards another extinction, and no one knows why. It's up to Aloy to uncover the secrets behind these threats and restore order and balance to the world. Along the way, she must reunite with old friends, forge alliances with warring new factions and unravel the legacy of the ancient past - all the while trying to stay one step ahead of a seemingly undefeatable new enemy.",
                genre="Action Role Playing",
                release_date=datetime(
                    year=2022,
                    month=2,
                    day=18
                    ),
                publisher="Guerilla Games",
                carousel_image='https://gameranx.com/wp-content/uploads/2022/01/horizon-forbidden-west-1-1024x576.jpg',
                game_image="https://upload.wikimedia.org/wikipedia/en/6/69/Horizon_Forbidden_West_cover_art.jpg",
                game_trailer='https://www.youtube.com/embed/Lq594XmpPBg',
                price=59.99
            ),
            Game(
                title="Control",
                description="After a secretive agency in New York is invaded by an otherworldly threat, you become the new Director struggling to regain Control. This supernatural third-person action-adventure game will challenge you to master a combination of supernatural abilities, modifiable loadouts and reactive environments, while fighting through a deep and unpredictable world.",
                genre="Action Adventure",
                release_date=datetime(
                    year=2019,
                    month=8,
                    day=27
                    ),
                publisher="Remedy Entertainment",
                carousel_image='https://gaming-cdn.com/images/products/2692/orig/control-pc-game-epic-games-europe-cover.jpg?v=1668442766',
                game_image="https://cdn1.epicgames.com/offer/calluna/Control_Portrait_Storefront_1200X1600_1200x1600-456c920cae7a0aa9b36670cd5e1237a1",
                game_trailer='https://www.youtube.com/embed/uvKAHpIvbl8',
                price=59.99
            ),
        ]
        
        for game in games_data:
            db.session.add(game)
        
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
            GamePlatform(
                game_id=7,
                platform_id=1
            ),
            GamePlatform(
                game_id=7,
                platform_id=4
            ),
            GamePlatform(
                game_id=7,
                platform_id=5
            ),
            GamePlatform(
                game_id=7,
                platform_id=6
            ),
            GamePlatform(
                game_id=8,
                platform_id=1
            ),
            GamePlatform(
                game_id=8,
                platform_id=2
            ),
            GamePlatform(
                game_id=8,
                platform_id=3
            ),
            GamePlatform(
                game_id=8,
                platform_id=4
            ),
            GamePlatform(
                game_id=8,
                platform_id=5
            ),
            GamePlatform(
                game_id=8,
                platform_id=6
            ),
            GamePlatform(
                game_id=9,
                platform_id=1
            ),
            GamePlatform(
                game_id=9,
                platform_id=2
            ),
            GamePlatform(
                game_id=9,
                platform_id=6
            ),
            GamePlatform(
                game_id=10,
                platform_id=1
            ),
            GamePlatform(
                game_id=10,
                platform_id=2
            ),
            GamePlatform(
                game_id=10,
                platform_id=3
            ),
            GamePlatform(
                game_id=10,
                platform_id=4
            ),
            GamePlatform(
                game_id=10,
                platform_id=5
            ),
            GamePlatform(
                game_id=10,
                platform_id=6
            ),
            GamePlatform(
                game_id=10,
                platform_id=7
            ),
        ]
        
        for game_platform in game_platform_data:
            db.session.add(game_platform)
        
        db.session.commit()
        
        print("New database seed successful.")