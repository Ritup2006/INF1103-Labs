
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


# Section 6.2: Function accepting the parent Product type
def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


# Create both subclasses
laptop = PhysicalProduct("P001", "Laptop", 1500.0, 10, 2.5, None)
antivirus = DigitalProduct("D001", "Antivirus", 99.0, 50, 500.0, None)


# Test 1: Substitutability
print("=== Test 1: LSP Substitutability ===")

show_product_details(laptop)
print("--------------------")
show_product_details(antivirus)


# Test 2: Both subclasses inside Inventory
print("\n=== Test 2: Inventory with Product subclasses ===")

inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(antivirus)

for product in inventory.products:
    show_product_details(product)
    print("--------------------")


# Test 3: Common Product behaviour
print("\n=== Test 3: Stock Update ===")

laptop.update_stock(8)
antivirus.update_stock(20)

print("Laptop stock:", laptop.get_stock())
print("Antivirus stock:", antivirus.get_stock())
