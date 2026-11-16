from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class ProductFactory:

    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        extra_value: float,
        supplier: Supplier
    ) -> Product:

        if product_type == "physical":
            return PhysicalProduct(
                product_id, name, price, stock,
                extra_value, supplier
            )

        elif product_type == "digital":
            return DigitalProduct(
                product_id, name, price, stock,
                extra_value, supplier
            )

        else:
            raise ValueError(
                f"Unknown product type: {product_type}"
            )