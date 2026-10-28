
import json

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock:int):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity: int):
        self.__stock = quantity

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

    def get_product_id(self):
            return self.__product_id

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
        


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists!")
        else:
            self.products.append(product)
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





def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"])
            )
            inventory.add_product(product)

    except FileNotFoundError:
        pass

    return inventory


def save_inventory(inventory):
    data = []

    for product in inventory.products:
        data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully!")

def main():
    inventory = load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Product ID: ")
            name = input("Product Name: ")

            while True:
                try:
                    price = float(input("Product Price: "))

                    if price < 0:
                        print("Price cannot be negative!")
                    else:
                        break

                except ValueError:
                    print("Invalid price! Please enter a number.")

            while True:
                try:
                    stock = int(input("Product Stock: "))

                    if stock < 0:
                        print("Stock cannot be negative!")
                    else:
                        break

                except ValueError:
                    print("Invalid stock! Please enter a whole number.")

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

        elif choice == "3":
            product_id = input("Enter Product ID: ")
            product = inventory.search_product(product_id)

            if product is not None:
                while True:
                    try:
                        quantity = int(input("Enter new stock quantity: "))

                        if quantity < 0:
                            print("Stock cannot be negative!")
                        else:
                            break

                    except ValueError:
                        print("Invalid stock! Please enter a whole number.")

                product.update_stock(quantity)
                print("Stock updated successfully!")

            else:
                print("Product not found!")

        elif choice == "4":
            product_id = input("Enter Product ID: ")

            product = inventory.search_product(product_id)

            if product is not None:
                product.display_information()
            else:
                print("Product not found!")

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid Option. Please enter 1 to 6.")



if __name__ == "__main__":
    main()