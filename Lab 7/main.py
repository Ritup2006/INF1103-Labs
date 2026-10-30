import json
from product import Product
from inventory import Inventory


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
            inventory.add_product(product, show_message=False)

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