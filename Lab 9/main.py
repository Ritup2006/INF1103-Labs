import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product_type = item.get("type")

            supplier_data = item.get("supplier")

            if supplier_data is not None:
                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )
            else:
                supplier = None

            if product_type == "physical":
                extra_value = float(item["weight"])

            elif product_type == "digital":
                extra_value = float(item["download_size"])

            else:
                print(f"Skipping unknown product type: {product_type}")
                continue

            product = ProductFactory.create(
                product_type,
                item["id"],
                item["name"],
                float(item["price"]),
                int(item["stock"]),
                extra_value,
                supplier
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

            supplier_id = input("Supplier ID: ")
            supplier_name = input("Supplier Name: ")
            supplier_email = input("Supplier Email: ")

            supplier = Supplier(
                supplier_id,
                supplier_name,
                supplier_email
            )

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

            while True:
                print("Product type:")
                print("1. Physical")
                print("2. Digital")

                type_choice = input("Choose type (1 or 2): ")

                if type_choice in ("1", "2"):
                    break
                print("Invalid choice! Please enter 1 or 2.")

            if type_choice == "1":
                while True:
                    try:
                        weight = float(input("Weight (kg): "))

                        if weight < 0:
                            print("Weight cannot be negative!")
                        else:
                            break

                    except ValueError:
                        print("Invalid weight! Please enter a number.")

                product = ProductFactory.create( "physical", product_id, name, price, stock, weight, supplier)

            else:
                while True:
                    try:
                        download_size = float(input("Download size (MB): "))

                        if download_size < 0:
                            print("Download size cannot be negative!")
                        else:
                            break

                    except ValueError:
                        print("Invalid size! Please enter a number.")

                product = ProductFactory.create(
                    "digital",
                    product_id,
                    name,
                    price,
                    stock,
                    download_size,
                    supplier
                )

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