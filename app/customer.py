from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car
