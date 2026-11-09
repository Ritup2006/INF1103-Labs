from inventory import Inventory
from supplier import Supplier
from physical_product import PhysicalProduct

supplier1 = Supplier("S001", "Samsung", "contact@samsung.com")

laptop = PhysicalProduct("P001", "Laptop", 1500.0, 10, 2.5, supplier1)

inventory_a = Inventory()
inventory_b = Inventory()

# Step 1: Add laptop to Inventory A
inventory_a.add_product(laptop)

# Step 2: Remove laptop from Inventory A
inventory_a.remove_product("P001")

# Step 3: Add laptop to Inventory B
inventory_b.add_product(laptop)

print("\nInventory A:")
inventory_a.display_all()

print("\nInventory B:")
inventory_b.display_all()

print("\nDoes the laptop still exist?")
laptop.display_information()