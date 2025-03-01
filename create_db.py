from datetime import datetime
from ext import app, db
from models import Product, Users

products = [
    {
        "name": "FC25",
        "image": "https://gamezone.ge/images/thumbnails/1715/1500/detailed/18/81nHs9ITdnL._AC_SL1500__cujh-3f.jpg",
        "title": "PS5 EA Sports FC 25",
        "condition": "New",
        "platform": "PS5",
        "date": "27.09.24",
        "price": "70",
        "category": "Disc"
    },
    {
        "name": "PS5",
        "image": "https://gamezone.ge/images/thumbnails/400/350/detailed/20/1_ethl-2d.png",
        "title": "PlayStation®5 Slim Disc Version 1TB",
        "condition": "New",
        "platform": "PS5",
        "date": "15.11.23",
        "price": "300",
        "category": "Console",
    },

    {
        "name": "Retro Console",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/24/anbernic_rg35xx_retro_handheld_emulator_gaming_console_fjwe-21.jpg",
        "title": "Retro console Anbernic RG35XX White",
        "condition": "New",
        "platform": "PS5",
        "date": "15.11.23",
        "price": "300",
        "category": "Console",
    },

    {
        "name": "NBA 2K25",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/23/PS5_NBA_2K25.jpg",
        "title": "PS5 NBA 2K25",
        "condition": "New",
        "platform": "PS5",
        "date": "15.11.23",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "CYBERPUNK 2077",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/20/Untitled-1_npka-gh.jpg",
        "title": "PS5 CYBERPUNK 2077: ULTIMATE EDITION",
        "condition": "New",
        "platform": "PS5",
        "date": "15.11.23",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "MARVEL'S SPIDER-MAN 2",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/19/PS5-MARVEL%E2%80%99S-SPIDER-MAN-2_6atg-4n.jpg",
        "title": "PS5 MARVEL'S SPIDER-MAN 2",
        "condition": "New",
        "platform": "PS5",
        "date": "15.11.23",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "GOD OF WAR RAGNAROK",
        "image": "https://gamezone.ge/images/thumbnails/1715/1500/detailed/14/817y77i7EFL._SL1500__uz7j-gh.jpg",
        "title": "PS5 GOD OF WAR RAGNAROK",
        "condition": "New",
        "platform": "PS5",
        "date": "15.11.23",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "FORZA HORIZON 5",
        "image": "https://gamezone.ge/images/thumbnails/1715/1500/detailed/10/71LSwnEXpXL._SL1500_.jpg",
        "title": "Xbox One FORZA HORIZON 5",
        "condition": "New",
        "platform": "Xbox",
        "date": "15.11.23",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": " RED DEAD REDEMPTION 2",
        "image": "https://i5.walmartimages.com/asr/a2b7bc50-bd11-46e2-971d-681fcd405b4c.34a3dcea5ca05bf78e2db3727b1be961.jpeg",
        "title": "XBOX ONE RED DEAD REDEMPTION 2",
        "condition": "New",
        "platform": "Xbox",
        "date": "15.11.23",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "Nintendo Switch",
        "image": "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/My%20Nintendo%20Store/EN-US/Hardware/nintendo-switch-oled-model-mario-red-edition-112872/112872-nintendo-switch-oled-model-mario-red-edition-package-1200x675",
        "title": "Nintendo Switch - OLED Model MARIO RED EDITION",
        "condition": "New",
        "platform": "Nintendo Switch",
        "date": "15.11.23",
        "price": "150",
        "category": "Console",
    },

    {
        "name": "Nintendo Switch",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/18/Untitled-1.jpg",
        "title": "NINTENDO SWITCH CONTROLLER SPLIT PAD PRO (LUCARIO and PIKACHU)",
        "condition": "New",
        "platform": "Nintendo Switch",
        "date": "15.11.20",
        "price": "100",
        "category": "Console",
    },

    {
        "name": "Mortal Kombat 11",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/8/mortal11111111.png",
        "title": "PS5 Mortal Kombat 11 ULTIMATE (RUS/ENG)",
        "condition": "New",
        "platform": "PS5",
        "date": "17.3.18",
        "price": "40",
        "category": "Disc",
    },

    {
        "name": "Ghost Of Tsushima",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/9/7755_lypd-e6.png",
        "title": "PS5 Ghost Of Tsushima Director's Cut (RUS/ENG)",
        "condition": "New",
        "platform": "PS5",
        "date": "17.3.19",
        "price": "60",
        "category": "Disc",
    },


    {
        "name": "Mortal Kombat 1",
        "image": "https://gamezone.ge/images/thumbnails/1715/1500/detailed/18/819SHNH35RL._SL1500__2yx5-2l.jpg",
        "title": "PS5 Mortal Kombat 1",
        "condition": "New",
        "platform": "PS5",
        "date": "17.3.23",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "GRAN TURISMO 7",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/20/Untitled-1_oqyh-iu.jpg",
        "title": "PS5 GRAN TURISMO 7 (ENG)",
        "condition": "New",
        "platform": "PS5",
        "date": "17.3.24",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "F1 24",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/23/PS5_F1_24_tx7r-wr.jpg",
        "title": "PS5 F1 24",
        "condition": "New",
        "platform": "PS5",
        "date": "17.3.24",
        "price": "70",
        "category": "Disc",
    },

    {
        "name": "ELDEN RING",
        "image": "https://gamezone.ge/images/thumbnails/1143/1000/detailed/23/PS5_ELDEN_RING_SHADOW_OF_THE_ERDTREE.jpg",
        "title": "PS5 ELDEN RING SHADOW OF THE ERDTREE",
        "condition": "New",
        "platform": "PS5",
        "date": "6.21.24",
        "price": "70",
        "category": "Disc",
    },

]




for product in products:
    try:
        product["date"] = datetime.strptime(product["date"], "%d.%m.%y").date()
    except ValueError:
        # If it fails, try another format
        product["date"] = datetime.strptime(product["date"], "%m.%d.%y").date()



admin_user = {
    "username": "admin",
    "password": "admin123!",
    "role": "Admin",
}

with app.app_context():

    db.create_all()

    for product in products:

        existing_product = Product.query.filter_by(name=product["name"]).first()
        if not existing_product:
            new_product = Product(
                name=product["name"],
                title=product["title"],
                platform=product["platform"],
                condition=product["condition"],
                price=product["price"],
                date=product["date"],
                img=product["image"],
                category=product["category"]
            )
            db.session.add(new_product)


    existing_admin = Users.query.filter_by(username=admin_user["username"]).first()
    if not existing_admin:
        new_admin = Users(
            username=admin_user["username"],
            password=admin_user["password"],
            role=admin_user["role"]
        )
        db.session.add(new_admin)
        print("Admin user created successfully.")
    else:
        print("Admin user already exists.")


    db.session.commit()
    print("Database initialized successfully.")

    admin_user_to_delete = Users.query.filter_by(username="admin").first()
    if admin_user_to_delete:
        db.session.delete(admin_user_to_delete)
        db.session.commit()
        print("Default admin user deleted.")

