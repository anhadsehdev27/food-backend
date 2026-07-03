from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

import schemas
import services

from database import get_db, create_table

app = FastAPI()

create_table()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Specifies allowed domains
    allow_credentials=True,           # Allows cookies and auth headers
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all request headers
)

#users

@app.post("/users", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)



@app.get("/list/users")
def get_users(db: Session = Depends(get_db)):
    return services.get_users(db)


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = services.get_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = services.delete_user(db, user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User Deleted"}


#menu


@app.post("/menu", response_model=schemas.Menu)
def add_menu(menu: schemas.MenuCreate, db: Session = Depends(get_db)):
    return services.create_menu(db, menu)


@app.get("/menu", response_model=list[schemas.Menu])
def get_all_menu(db: Session = Depends(get_db)):
    return services.get_menus(db)


@app.get("/menu/{menu_id}", response_model=schemas.Menu)
def get_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = services.get_menu(db, menu_id)

    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")

    return menu


@app.patch("/menu/{menu_id}", response_model=schemas.Menu)
def edit_menu(
    menu_id: int,
    menu: schemas.MenuUpdate,
    db: Session = Depends(get_db)
):
    updated = services.update_menu(db, menu_id, menu)

    if not updated:
        raise HTTPException(status_code=404, detail="Menu not found")

    return updated


@app.delete("/menu/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    deleted = services.delete_menu(db, menu_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Menu not found")

    return {"message": "Menu Deleted"}


#item


@app.post("/item", response_model=schemas.Item)
def add_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return services.create_item(db, item)


@app.get("/item", response_model=list[schemas.Item])
def get_all_items(db: Session = Depends(get_db)):
    return services.get_items(db)


@app.get("/item/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = services.get_item(db, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@app.put("/item/{item_id}", response_model=schemas.Item)
def edit_item(
    item_id: int,
    item: schemas.ItemUpdate,
    db: Session = Depends(get_db)
):
    updated = services.update_item(db, item_id, item)

    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")

    return updated


@app.delete("/item/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted = services.delete_item(db, item_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"message": "Item Deleted"}


#restaurant


@app.post("/restaurant", response_model=schemas.Restaurant)
def add_restaurant(
    restaurant: schemas.RestaurantCreate,
    db: Session = Depends(get_db)
):
    return services.create_restaurant(db, restaurant)


@app.get("/restaurant", response_model=list[schemas.Restaurant])
def get_all_restaurants(db: Session = Depends(get_db)):
    return services.get_restaurants(db)


@app.get("/restaurant/{restaurant_id}", response_model=schemas.Restaurant)
def get_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    restaurant = services.get_restaurant(db, restaurant_id)

    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return restaurant


@app.put("/restaurant/{restaurant_id}", response_model=schemas.Restaurant)
def edit_restaurant(
    restaurant_id: int,
    restaurant: schemas.RestaurantUpdate,
    db: Session = Depends(get_db)
):
    updated = services.update_restaurant(
        db,
        restaurant_id,
        restaurant
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return updated


@app.delete("/restaurant/{restaurant_id}")
def delete_restaurant(
    restaurant_id: int,
    db: Session = Depends(get_db)
):
    deleted = services.delete_restaurant(db, restaurant_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return {"message": "Restaurant Deleted"}


#restaurant menu


@app.post("/restaurant-menu", response_model=schemas.RestaurantMenu, status_code=201)
def add_restaurant_menu(
    data: schemas.RestaurantMenuCreate,
    db: Session = Depends(get_db)
):
    return services.create_restaurant_menu(db, data)

@app.get("/restaurant-menu", response_model=list[schemas.RestaurantMenu])
def get_all_restaurant_menus(db: Session = Depends(get_db)):
    return services.get_restaurant_menus(db)


@app.get("/restaurant-menu/{id}",
         response_model=schemas.RestaurantMenu)
def get_restaurant_menu(
    id: int,
    db: Session = Depends(get_db)
):
    restaurant_menu = services.get_restaurant_menu(
        db,
        id
    )

    if not restaurant_menu:
        raise HTTPException(
            status_code=404,
            detail="Restaurant Menu not found"
        )

    return restaurant_menu


@app.patch("/restaurant-menu/{id}",
         response_model=schemas.RestaurantMenu)
def edit_restaurant_menu(
    id: int,
    data: schemas.RestaurantMenuUpdate,
    db: Session = Depends(get_db)
):
    updated = services.update_restaurant_menu(
        db,
        id,
        data
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Restaurant Menu not found"
        )

    return updated


@app.delete("/restaurant-menu/{id}")
def delete_restaurant_menu(
    id: int,
    db: Session = Depends(get_db)
):
    deleted = services.delete_restaurant_menu(
        db,
        id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Restaurant Menu not found"
        )

    return {"message": "Restaurant Menu Deleted"}



#orders


@app.post("/orders", response_model=schemas.Order)
def add_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return services.create_order(db, order)


@app.get("/orders", response_model=list[schemas.Order])
def get_all_orders(db: Session = Depends(get_db)):
    return services.get_orders(db)


@app.get("/orders/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = services.get_order(db, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@app.patch("/orders/{order_id}")
def update_order_status(
    order_id: int,
    order: schemas.OrderUpdate,
    db: Session = Depends(get_db)
):
    updated = services.update_order(db, order_id, order)

    if not updated:
        raise HTTPException(status_code=404, detail="Order not found")

    return updated


@app.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    deleted = services.delete_order(db, order_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")

    return {"message": "Order Deleted"}


#order items

@app.post("/order-item", response_model=schemas.OrderItem)
def add_order_item(
    order_item: schemas.OrderItemCreate,
    db: Session = Depends(get_db)
):
    return services.create_order_item(db, order_item)


@app.get("/order-item", response_model=list[schemas.OrderItem])
def get_all_order_items(db: Session = Depends(get_db)):
    return services.get_order_items(db)


@app.get("/order-item/{order_item_id}",
         response_model=schemas.OrderItem)
def get_order_item(
    order_item_id: int,
    db: Session = Depends(get_db)
):
    order_item = services.get_order_item(
        db,
        order_item_id
    )

    if not order_item:
        raise HTTPException(
            status_code=404,
            detail="Order Item not found"
        )

    return order_item


@app.put("/order-item/{order_item_id}",
         response_model=schemas.OrderItem)
def edit_order_item(
    order_item_id: int,
    order_item: schemas.OrderItemUpdate,
    db: Session = Depends(get_db)
):
    updated = services.update_order_item(
        db,
        order_item_id,
        order_item
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Order Item not found"
        )

    return updated


@app.delete("/order-item/{order_item_id}")
def delete_order_item(
    order_item_id: int,
    db: Session = Depends(get_db)
):
    deleted = services.delete_order_item(
        db,
        order_item_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Order Item not found"
        )

    return {"message": "Order Item Deleted"}

#payment


@app.post("/payment", response_model=schemas.Payment)
def make_payment(
    payment: schemas.PaymentCreate,
    db: Session = Depends(get_db)
):
    return services.create_payment(db, payment)


@app.get("/payment", response_model=list[schemas.Payment])
def get_payments(db: Session = Depends(get_db)):
    return services.get_payments(db)


@app.get("/payment/{payment_id}", response_model=schemas.Payment)
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    payment = services.get_payment(db, payment_id)

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return payment


@app.patch("/payment/{payment_id}")
def update_payment_status(
    payment_id: int,
    payment: schemas.PaymentUpdate,
    db: Session = Depends(get_db)
):
    updated = services.update_payment(
        db,
        payment_id,
        payment
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return updated