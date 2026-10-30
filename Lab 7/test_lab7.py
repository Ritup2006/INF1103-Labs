from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P001", "Guitar", 499.99, 5, 3.2)
game = DigitalProduct("D001", "Space Game", 29.99, 100, 850.5)

guitar.display_information()
print(guitar.get_fulfilment_info())

game.display_information()
print(game.get_fulfilment_info())

# This should fail, because Product is abstract
try:
    item = Product("X001", "Thing", 1.0, 1)
except TypeError as e:
    print("Blocked as expected:", e)

light = PhysicalProduct("P002", "Book", 15.00, 20, 0.5)
heavy = PhysicalProduct("P003", "Amplifier", 350.00, 3, 12.0)

print("Book shipping:", light.calculate_shipping_cost())
print("Amplifier shipping:", heavy.calculate_shipping_cost())

print(guitar.to_dict())
print(game.to_dict())