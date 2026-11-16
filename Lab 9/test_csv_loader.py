from csv_loader import load_products
from inventory import Inventory
from supplier import Supplier

inventory = Inventory()
supplier = Supplier("S001", "ABC Supplies", "abc@gmail.com")

load_products("products.csv", inventory, supplier)

print("\nLoaded products:")
inventory.display_all()