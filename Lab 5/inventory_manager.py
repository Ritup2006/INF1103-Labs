
import json

def display_all(inventory):
    print("\nCurrent Inventory")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}")

def add_product(inventory):
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)
    print("Product added successfully!")
    

def update_stock(inventory):
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")

            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")

def search_product(inventory):
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            return

    print("Product not found.")



def get_valid_input():
    stock_quantity = input("Enter Stock Quantity (Type 'quit' to quit): ")

    if stock_quantity.lower() == "quit": 
        return "quit"

    if not stock_quantity.isdigit():
        print("This number is rejected.")
        return None

    stock_actual = int(stock_quantity)

    if stock_actual < 0:
        print("Negative number rejected")
        return None
    
    return stock_actual


def process_delivery(current_total, new_value):
    new_total = current_total + new_value

    return new_total


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, history, failed_attempts, deliveries_processed):
    print("Total Units:", total_units)
    print("Transaction History:", history)
    print("Total Deliveries Processed:", deliveries_processed)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    except FileNotFoundError:
        print("No inventory file found. Starting with an empty inventory.")
        return []


def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully.")

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
            display_all(inventory)

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            break

        else:
            print("Invalid option. Please enter 1 to 6.")



if __name__ == "__main__":
    main()