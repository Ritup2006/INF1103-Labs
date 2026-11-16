from product_factory import ProductFactory

try:
    product = ProductFactory.create(
        "service", "S001", "Installation",
        30.0, 5, 0.0, None
    )

except ValueError as error:
    print(error)