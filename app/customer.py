from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            milk_to_buy: int,
            bread_to_buy: int,
            butter_to_buy: int,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.milk_to_buy = milk_to_buy
        self.bread_to_buy = bread_to_buy
        self.butter_to_buy = butter_to_buy
        self.location = location
        self.money = money
        self.car = car
