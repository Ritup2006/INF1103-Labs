class Inventory:
    def __init__(self):
        self.products = []


    def add_product(self, product, show_message=True):
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

    def display_all(self):
        print("\nCurrent Inventory")
        for product in self.products:
            product.display_information()
