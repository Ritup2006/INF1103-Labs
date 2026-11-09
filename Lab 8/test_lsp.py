
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order


def display_product_price(product: Product) -> None:
    print(product.get_price())


# Create products
# Adjust these constructor arguments to match your classes.
laptop = PhysicalProduct("P001", "Laptop", 1500.0, 10, None, 2.5)
antivirus = DigitalProduct("D001", "Antivirus", 99.0, 50, None, "DOWNLOAD-001")


# Test 1: LSP with a common function
print("=== Test 1: Product Substitution ===")
display_product_price(laptop)
display_product_price(antivirus)


# Test 2: LSP with Order
print("\n=== Test 2: Order Substitution ===")

order = Order("ORD003")

order.add_order_line(laptop, 1)
order.add_order_line(antivirus, 2)

order.display_order()


# Test 3: Check that both are Product subclasses
print("\n=== Test 3: Inheritance Check ===")

print(isinstance(laptop, Product))
print(isinstance(antivirus, Product))
