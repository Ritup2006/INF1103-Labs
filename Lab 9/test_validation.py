from physical_product import PhysicalProduct
from order_line import OrderLine
from supplier import Supplier

supplier = Supplier("S001", "ABC Supplies", "abc@gmail.com")

# Test 1: Invalid price
try:
    product = PhysicalProduct("P001", "Laptop", -100, 10, 2.5, supplier)
except ValueError as error:
    print("Test 1:", error)

# Test 2: Negative stock
try:
    product = PhysicalProduct("P002", "Mouse", 50, -5, 0.2, supplier)
except ValueError as error:
    print("Test 2:", error)

# Create a valid product
product = PhysicalProduct("P003", "Keyboard", 80, 10, 1.0, supplier)

# Test 3: Invalid order quantity
try:
    line = OrderLine(product, 0)
except ValueError as error:
    print("Test 3:", error)

# Test 4: Invalid stock update
try:
    product.update_stock(-10)
except ValueError as error:
    print("Test 4:", error)