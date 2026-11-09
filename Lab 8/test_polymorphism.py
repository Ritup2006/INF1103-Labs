from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

laptop = PhysicalProduct("P001", "Laptop", 1500.0, 10, 2.5, None)

antivirus = DigitalProduct("D001", "Antivirus", 99.0, 50, 500.0, None)
products: list[Product] = [laptop, antivirus]

for product in products:
    product.display_information()
    print("--------------------")
    