class Shop:
    def __init__(
        self,
        name: str,
        location: list[int],
        milk_price: float | int,
        bread_price: float | int,
        butter_price: float | int,
    ) -> None:
        self.name = name
        self.location = location
        self.milk_price = milk_price
        self.bread_price = bread_price
        self.butter_price = butter_price
