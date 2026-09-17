from database import Base
from sqlalchemy import Column,Text, Integer, String, DateTime, Boolean,JSON,Numeric, ForeignKey


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    email = Column(String(255), unique=True)
    mobile_no = Column(String(20))
    password_hash = Column(String)
    role_id=Column(Integer, ForeignKey("role.id"))

   

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    menu_id = Column(Integer, ForeignKey("menu.id"), nullable=False)
    item_name = Column(String, index=True)
    description = Column(Text, index=True)
    image_url = Column(Text, index=True)
    is_veg = Column(Boolean, index=True)
    status = Column(Integer, index=True)
    created_at = Column(DateTime )
    updated_at = Column(DateTime )


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    restaurant_name = Column(String,  index=True, )
    owner_name = Column(String, index=True)
    email = Column(String, index=True)
    mobile_no = Column(String, index=True)
    address = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    pincode = Column(String, index=True)
    gst_no = Column(String, index=True)
    logo_url = Column(String, index=True)
    status = Column(Integer, index=True)
    created_at = Column(DateTime , index=True)
    updated_at = Column(DateTime , index=True)

class Restaurant_Menu(Base):
    __tablename__ = "restaurant_menu"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"), nullable=False)
    description = Column(Text, index=True)
    price = Column(Numeric(10,2), index=True)
    is_available = Column(Boolean, index=True)
    created_at = Column(DateTime , index=True)
    discount = Column(Numeric(10,2), index=True)
    item_id = Column(Integer, ForeignKey("item.id"), index=True)
    menu_id = Column(Integer, ForeignKey("menu.id"), index=True)




class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_no = Column(String, index=True)
    users_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    restaurant_id = Column(Integer,ForeignKey("restaurant.id"),nullable=False)
    order_datetime = Column(DateTime , index=True)
    order_status = Column(String, index=True)
    remarks = Column(String, index=True)
    created_at = Column(DateTime , index=True)

class Order_Item(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer,ForeignKey("orders.id"),nullable=False)
    restaurant_menu_id = Column(Integer, nullable=False)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    quantity = Column(Integer, index=True)
    unit_price = Column(Numeric(10,2), index=True)
    total_price = Column(Numeric(10,2), index=True)

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    transaction_id = Column(String, index=True)
    payment_method = Column(String, index=True)
    amount = Column(Numeric(10,2), index=True)
    payment_status = Column(String, index=True)
    gateway_response = Column(JSON)
    paid_at = Column(DateTime , index=True)
    created_at = Column(DateTime , index=True)

class Role(Base):
    __tablename__ = "role"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role_name = Column(
        String,
        nullable=False,
        unique=True
    )


