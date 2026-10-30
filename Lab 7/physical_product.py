from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

        