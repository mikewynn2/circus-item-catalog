from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem, User

# Create database and shortcut
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create the user
User1 = User(name="Mike Wynn", email="mikewynn@email.com")
session.add(User1)
session.commit()

# Create category 1
category1 = Category(user_id=1, name="Aerial Equipment")
session.add(category1)
session.commit()

# Create category 2
category2 = Category(user_id=1, name="Ground Equipment")
session.add(category2)
session.commit()

# Create category 3
category3 = Category(user_id=1, name="Accessories")
session.add(category3)
session.commit()

# Add Aerial Equipment
categoryItem1 = CatalogItem(user_id=1, name="Aerial Hoop",
                            description="Our Aerial Hoops are custom size made to order. Made of solid steel.",
                            price="300.00",
                            category=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CatalogItem(user_id=1, name="Rope",
                            description="Our Aerial Ropes come in 3 sizes, 3M-6M-9M. Braided Cotton or Spanish web.",
                            price="250.00",
                            category=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CatalogItem(user_id=1, name="Silks",
                            description="Silks are cut to length desired, That is if you actually desire to do silks.",
                            price="200.00",
                            category=category1)
session.add(categoryItem1)
session.commit()


# Add Ground Equipment
categoryItem1 = CatalogItem(user_id=1, name="Chinese Pole",
                            description="Chinese Poles come wrapped in rubber, final diameter of 2 and 1/8th inch.",
                            price="2500.00",
                            category=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CatalogItem(user_id=1, name="Handstand Canes",
                            description="Become the master of a One Arm Handstand with our pro level handstand pegs.",
                            price="350.00",
                            category=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CatalogItem(user_id=1, name="Cyr Wheel",
                            description="Invented by Neanderthals, perfected by Canadians, our cyr wheels are best",
                            price="3000.00",
                            category=category2)
session.add(categoryItem1)
session.commit()


# Add Accesories
categoryItem1 = CatalogItem(user_id=1, name="Carabiner",
                            description="Best in the business Carabiners. Never second guess your rigging again.",
                            price="25.00",
                            category=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CatalogItem(user_id=1, name="Hand Loop",
                            description="Safety First with these hand loops with leather safety. Cotton for comfort",
                            price="15.00",
                            category=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CatalogItem(user_id=1, name="Harness",
                            description="High Grade Kevlar bungee harness. One size only, you dont fit, you dont fly.",
                            price="100.00",
                            category=category3)
session.add(categoryItem1)
session.commit()


print("added all items into categories!")
