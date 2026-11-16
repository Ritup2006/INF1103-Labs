from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount

supplier1 = Supplier("S001", "Samsung", "contact@samsung.com")

laptop = PhysicalProduct("P001", "Laptop", 1500, 10, 2.5, supplier1)
antivirus = DigitalProduct("D001", "Antivirus", 99, 100, 500, supplier1)

order1 = Order("ORD001")

# Add 2 laptops to order1

order1.add_order_line(laptop, 2)

# Add 3 antivirus subscriptions to order1
order1.add_order_line(antivirus, 3)

# Print the total price of order1
total_price = order1.calculate_total()
print(total_price)

order2 = Order("ORD002")
order2.add_order_line(laptop, 1)

print(order1.order_lines[0] is order2.order_lines[0])
print(order1.order_lines[0].product is order2.order_lines[0].product)

order1.remove_order_line(0)
order1.display_order()


print("\n--- Testing Discount Strategies ---")

order3 = Order("ORD003")
order3.add_order_line(laptop, 1)

print("No discount:", order3.calculate_total())

order3.set_discount(PercentageDiscount(10))
print("10% discount:", order3.calculate_total())

order3.set_discount(BulkDiscount(200, 20))
print("Bulk discount:", order3.calculate_total())