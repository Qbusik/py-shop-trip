from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        prices: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.prices = prices

    def calculate_shopping_cost(
            self,
            customer: Customer
    ) -> float:
        result = 0
        result += self.prices["milk"] * customer.products["milk"]
        result += self.prices["bread"] * customer.products["bread"]
        result += self.prices["butter"] * customer.products["butter"]
        return result
