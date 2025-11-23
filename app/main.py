import json
import datetime
from math import sqrt

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:

    def calculate_distance(
            customer_location: list[int],
            shop_location: list[int]
    ) -> float:
        return sqrt((customer_location[0] - shop_location[0]) ** 2
                    + (customer_location[1] - shop_location[1]) ** 2)

    with open("app/config.json", "r") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    customers = []
    shops = []
    for customer in config["customers"]:
        customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
        ))
    for shop in config["shops"]:
        shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs_to_drive = []
        costs_of_goods = []
        costs_of_all = []
        for shop in shops:
            one_way_cost =\
                (calculate_distance(customer.location, shop.location)
                 * (customer.car.fuel_consumption / 100) * fuel_price)
            costs_to_drive.append(one_way_cost)
            costs_of_products = shop.calculate_shopping_cost(customer)
            costs_of_goods.append(costs_of_products)
            full_cost = round((one_way_cost * 2 + costs_of_products), 2)
            costs_of_all.append(full_cost)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {full_cost}")
        shop_chosen = costs_of_all.index(min(costs_of_all))
        if customer.money < min(costs_of_all):
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
            continue
        print(f"{customer.name} rides to {shops[shop_chosen].name}\n")
        customer_home = customer.location.copy()
        customer.money -= costs_to_drive[shop_chosen]
        customer.location = shops[shop_chosen].location
        customer.money -= costs_of_goods[shop_chosen]
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product in ["milk", "bread", "butter"]:
            print(f"{customer.products[product]} {product}s for"
                  f"{customer.products[product] * shops[shop_chosen].prices[product]: g}"
                  f" dollars")
        print(f"Total cost is {costs_of_goods[shop_chosen]} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        customer.money -= costs_to_drive[shop_chosen]
        customer.location = customer_home
        print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
