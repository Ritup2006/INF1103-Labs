from product import Product

class Inventory:
    def __init__(self):
        self.products : list[Product] = []


    def add_product(self, product: Product, show_message: bool =True):
        if self.search_product(product.get_product_id()) is not None:
            if show_message:
                print("Product ID already exists!")
        else:
            self.products.append(product)
            if show_message:
                print("Product added successfully!")


    def search_product(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def find_product(self, product_id: str) -> Product | None:
     return self.search_product(product_id)

    def display_all(self):
        print("\nCurrent Inventory")
        for product in self.products:
            product.display_information()

    def remove_product(self, product_id: str) -> None:
        product = self.search_product(product_id)

        if product is not None:
            self.products.remove(product)
            print("Product removed successfully!")
        else:
            print("Product not found!")