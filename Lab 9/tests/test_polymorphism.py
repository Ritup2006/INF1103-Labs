from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

laptop = PhysicalProduct("P001", "Laptop", 1500.0, 10, 2.5, None)

antivirus = DigitalProduct("D001", "Antivirus", 99.0, 50, 500.0, None)

products: list[Product] = [laptop, antivirus]

for product in products:
    product.display_information()
    print("--------------------")


from inventory import Inventory

inventory = Inventory()

inventory.add_product(laptop)
inventory.add_product(antivirus)

for product in inventory.products:
    product.display_information()
    print(product.get_fulfilment_info())
    print("--------------------")