from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime



class UsersBase(BaseModel):
    full_name: str
    email: str
    mobile_no: str
    password_hash: str


class UserCreate(UsersBase):
    pass

class UserUpdate(UsersBase):
    pass


class User(UsersBase):
    id: int

    class Config:
        from_attributes = True



class MenuBase(BaseModel):
    name: str


class MenuCreate(MenuBase):
    pass


class MenuUpdate(MenuBase):
    pass


class Menu(MenuBase):
    id: int

    class Config:
        from_attributes = True



class ItemBase(BaseModel):
    menu_id: int
    item_name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    is_veg: bool = True
    status: int = 1


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True



class RestaurantBase(BaseModel):
    restaurant_name: Optional[str] = None
    owner_name: str
    email: str
    mobile_no: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    gst_no: Optional[str] = None
    logo_url: Optional[str] = None
    status: int = 1


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantUpdate(RestaurantBase):
    pass


class Restaurant(RestaurantBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True



class RestaurantMenuBase(BaseModel):
    restaurant_id: int
    menu_id: int
    item_id: int

    description: Optional[str] = None

    price: float

    discount: Optional[float] = None

    is_available: bool = True


class RestaurantMenuCreate(RestaurantMenuBase):
    pass


class RestaurantMenuUpdate(RestaurantMenuBase):
    pass


class RestaurantMenu(RestaurantMenuBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True




class OrderBase(BaseModel):
    order_no: str
    users_id: int
    restaurant_id: int
    order_status: str
    remark: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    order_status: str


class Order(OrderBase):
    id: int
    order_datetime: Optional[datetime] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True



class OrderItemBase(BaseModel):
    order_id: int
    restaurant_menu_id: int
    item_name: int
    quantity: int
    unit_price: float
    total_price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int

    class Config:
        from_attributes = True



class PaymentBase(BaseModel):
    order_id: int
    transaction_id: Optional[str] = None
    payment_method: Optional[str] = None
    amount: float
    payment_status: str
    gateway_response: Optional[Dict[str, Any]] = None


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    payment_status: str


class Payment(PaymentBase):
    id: int
    paid_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True