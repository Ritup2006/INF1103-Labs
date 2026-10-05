inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

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
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            total_units = int(lines[0])
            history = eval(lines[1])

            return total_units, history

    except FileNotFoundError:
        return 0, []


def save_inventory(total_units, history):
    with open("inventory.txt", "w") as file:
        file.write(str(total_units) + "\n")
        file.write(str(history) + "\n")


def main():
    display_all(inventory)
    display_all(inventory)
    display_all(inventory)
    search_product(inventory)



if __name__ == "__main__":
    main()