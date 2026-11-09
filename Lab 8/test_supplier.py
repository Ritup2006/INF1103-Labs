from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# Create ONE supplier object
supplier1 = Supplier("S001", "Samsung", "contact@samsung.com")

# Create two products using the same supplier
physical_product = PhysicalProduct(
    "P001", "Laptop", 1500.0, 10, 2.5, supplier1
)

digital_product = DigitalProduct(
    "D001", "Antivirus Software", 99.0, 100, 500, supplier1
)

# Test association
print("Physical Product Supplier:")
physical_product.supplier.display_information()

print("\nDigital Product Supplier:")
digital_product.supplier.display_information()

del supplier1

print("After deleting supplier1:")
physical_product.supplier.display_information()
digital_product.supplier.display_information()