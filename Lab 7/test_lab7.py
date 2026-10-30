from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P001", "Guitar", 499.99, 5, 3.2)
game = DigitalProduct("D001", "Space Game", 29.99, 100, 850.5)

guitar.display_information()
game.display_information()