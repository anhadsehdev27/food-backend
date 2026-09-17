from sqlalchemy.orm import Session
from model import ( Users , Menu, Item, Restaurant, Restaurant_Menu, Orders, Order_Item, Payment,Role)
from schemas import (
    UserCreate, UserUpdate,
    MenuCreate, MenuUpdate,
    ItemCreate, ItemUpdate,
    RestaurantCreate, RestaurantUpdate,
    RestaurantMenuCreate, RestaurantMenuUpdate,
    OrderCreate, OrderUpdate,
    OrderItemCreate, OrderItemUpdate,
    PaymentCreate, PaymentUpdate,
    RoleCreate, RoleUpdate
    
)
from security import hash_password
from security import verify_password

def login_user(db: Session, email: str, password: str):
    print("Email:", email)

    user = db.query(Users).filter(Users.email == email).first()

    print("User:", user)

    if not user:
        print("User not found")
        return None

    print("Stored Hash:", user.password_hash)

    result = verify_password(password, user.password_hash)

    print("Password Match:", result)

    if not result:
        return None

    return user

def create_user(db: Session, data: UserCreate):
    user = Users(
        full_name=data.full_name,
        email=data.email,
        mobile_no=data.mobile_no,
        password_hash=hash_password(data.password),
        role_id=data.role_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session):
    return db.query(Users).all()


def get_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()


def update_user(db: Session, user_id: int, data: UserUpdate):
    user = get_user(db, user_id)
    if not user:
        return None

    for field, value in data.model_dump().items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True


def create_menu(db: Session, data: MenuCreate):
    menu = Menu(**data.model_dump())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


def get_menus(db: Session):
    return db.query(Menu).all()


def get_menu(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()


def update_menu(db: Session, menu_id: int, data: MenuUpdate):
    menu = get_menu(db, menu_id)
    if not menu:
        return None

    for field, value in data.model_dump().items():
        setattr(menu, field, value)

    db.commit()
    db.refresh(menu)
    return menu


def delete_menu(db: Session, menu_id: int):
    menu = get_menu(db, menu_id)
    if not menu:
        return False

    db.delete(menu)
    db.commit()
    return True



def create_item(db: Session, data: ItemCreate):
    item = Item(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_items(db: Session):
    return (
        db.query(
            Item.id,
            Item.menu_id,
            Item.item_name,
            Item.description,
            Item.image_url,
            Item.is_veg,
            Item.status,
            Restaurant_Menu.price,
            Restaurant_Menu.id.label("restaurant_menu_id")
        )
       
    )

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def update_item(db: Session, item_id: int, data: ItemUpdate):
    item = get_item(db, item_id)
    if not item:
        return None

    for field, value in data.model_dump().items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: int):
    item = get_item(db, item_id)
    if not item:
        return False

    db.delete(item)
    db.commit()
    return True



def create_restaurant(db: Session, data: RestaurantCreate):
    restaurant = Restaurant(**data.model_dump())
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


def get_restaurants(db: Session):
    return db.query(Restaurant).all()


def get_restaurant(db: Session, restaurant_id: int):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()


def update_restaurant(db: Session, restaurant_id: int, data: RestaurantUpdate):
    restaurant = get_restaurant(db, restaurant_id)
    if not restaurant:
        return None

    for field, value in data.model_dump().items():
        setattr(restaurant, field, value)

    db.commit()
    db.refresh(restaurant)
    return restaurant


def delete_restaurant(db: Session, restaurant_id: int):
    restaurant = get_restaurant(db, restaurant_id)
    if not restaurant:
        return False

    db.delete(restaurant)
    db.commit()
    return True


def create_restaurant_menu(db: Session, data: RestaurantMenuCreate):
    restaurant_menu = Restaurant_Menu(**data.model_dump())
    db.add(restaurant_menu)
    db.commit()
    db.refresh(restaurant_menu)
    return restaurant_menu


def get_restaurant_menus(db: Session):
    return db.query(Restaurant_Menu).all()


def get_restaurant_menu(db: Session, rest_menu_id: int):
    return db.query(Restaurant_Menu).filter(Restaurant_Menu.id == rest_menu_id).first()


def update_restaurant_menu(db: Session, rest_menu_id: int, data: RestaurantMenuUpdate):
    restaurant_menu = get_restaurant_menu(db, rest_menu_id)
    if not restaurant_menu:
        return None

    for field, value in data.model_dump().items():
        setattr(restaurant_menu, field, value)

    db.commit()
    db.refresh(restaurant_menu)
    return restaurant_menu


def delete_restaurant_menu(db: Session, rest_menu_id: int):
    restaurant_menu = get_restaurant_menu(db, rest_menu_id)
    if not restaurant_menu:
        return False

    db.delete(restaurant_menu)
    db.commit()
    return True



def create_order(db: Session, data: OrderCreate):
    order = Orders(**data.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def get_orders(db: Session):
    return db.query(Orders).all()


def get_order(db: Session, order_id: int):
    return db.query(Orders).filter(Orders.id == order_id).first()


def update_order(db: Session, order_id: int, data: OrderUpdate):
    order = get_order(db, order_id)
    if not order:
        return None

    for field, value in data.model_dump().items():
        setattr(order, field, value)

    db.commit()
    db.refresh(order)
    return order


def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    if not order:
        return False

    db.delete(order)
    db.commit()
    return True


def create_order_item(db: Session, data: OrderItemCreate):
    order_item = Order_Item(**data.model_dump())
    db.add(order_item)
    db.commit()
    db.refresh(order_item)
    return order_item


def get_order_items(db: Session):
    return db.query(Order_Item).all()


def get_order_item(db: Session, order_item_id: int):
    return db.query(Order_Item).filter(Order_Item.id == order_item_id).first()


def update_order_item(db: Session, order_item_id: int, data: OrderItemUpdate):
    order_item = get_order_item(db, order_item_id)
    if not order_item:
        return None

    for field, value in data.model_dump().items():
        setattr(order_item, field, value)

    db.commit()
    db.refresh(order_item)
    return order_item


def delete_order_item(db: Session, order_item_id: int):
    order_item = get_order_item(db, order_item_id)
    if not order_item:
        return False

    db.delete(order_item)
    db.commit()
    return True



def create_payment(db: Session, data: PaymentCreate):
    payment = Payment(**data.model_dump())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment


def get_payments(db: Session):
    return db.query(Payment).all()


def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()


def update_payment(db: Session, payment_id: int, data: PaymentUpdate):
    payment = get_payment(db, payment_id)
    if not payment:
        return None

    for field, value in data.model_dump().items():
        setattr(payment, field, value)

    db.commit()
    db.refresh(payment)
    return payment


def delete_payment(db: Session, payment_id: int):
    payment = get_payment(db, payment_id)
    if not payment:
        return False

    db.delete(payment)
    db.commit()
    return True

# ============================
# ROLE
# ============================


def create_role(db: Session, data: RoleCreate):

    role = Role(
        role_name=data.role_name
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role


def get_roles(db: Session):

    return db.query(Role).all()


def get_role(db: Session, role_id: int):

    return db.query(Role).filter(
        Role.id == role_id
    ).first()


def update_role(db: Session, role_id: int, data: RoleUpdate):

    role = get_role(db, role_id)

    if not role:
        return None

    role.role_name = data.role_name

    db.commit()
    db.refresh(role)

    return role


def delete_role(db: Session, role_id: int):

    role = get_role(db, role_id)

    if not role:
        return False

    db.delete(role)
    db.commit()

    return True