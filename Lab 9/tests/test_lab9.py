
import unittest
import os
import tempfile

from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount
from product_factory import ProductFactory
from physical_product import PhysicalProduct
from order_line import OrderLine
from order import Order
from inventory import Inventory
from supplier import Supplier
from csv_loader import load_products


class TestLab9(unittest.TestCase):

    def setUp(self):
        # Runs before each test
        self.supplier = Supplier(
            "S001", "ABC Supplies", "abc@gmail.com"
        )

        self.product = PhysicalProduct(
            "P001", "Laptop", 100, 10, 2.5, self.supplier
        )

    # SECTION 2: STRATEGY PATTERN

    def test_no_discount(self):
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_percentage_discount(self):
        self.assertEqual(PercentageDiscount(10).apply(250), 225)

    def test_bulk_discount(self):
        self.assertEqual(BulkDiscount(200, 20).apply(250), 230)

    def test_bulk_discount_below_threshold(self):
        self.assertEqual(BulkDiscount(300, 20).apply(250), 250)

    def test_student_discount(self):
        self.assertEqual(StudentDiscount().apply(250), 237.5)

    def test_order_switch_discount(self):
        order = Order("ORD001")
        order.add_order_line(self.product, 1)

        self.assertEqual(order.calculate_total(), 100)

        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 90)

    # SECTION 3: FACTORY PATTERN

    def test_factory_physical(self):
        product = ProductFactory.create(
            "physical", "P002", "Mouse",
            50, 10, 0.2, self.supplier
        )
        self.assertIsInstance(product, PhysicalProduct)

    def test_factory_digital(self):
        from digital_product import DigitalProduct

        product = ProductFactory.create(
            "digital", "D001", "Software",
            80, 20, 500, self.supplier
        )
        self.assertIsInstance(product, DigitalProduct)

    def test_factory_invalid_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service", "S002", "Installation",
                30, 5, 1.0, self.supplier
            )

    # SECTION 4: VALIDATION

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P002", "Mouse", -50, 10, 0.2, self.supplier
            )

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P002", "Mouse", 0, 10, 0.2, self.supplier
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P002", "Mouse", 50, -5, 0.2, self.supplier
            )

    def test_negative_stock_update(self):
        with self.assertRaises(ValueError):
            self.product.update_stock(-10)

    def test_invalid_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)

    # SECTION 5: CSV EXCEPTION HANDLING

    def test_csv_invalid_rows(self):
        inventory = Inventory()

        csv_data = (
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P010,Desk Lamp,25,10\n"
            "service,S010,Installation,30,5\n"
            "physical,P011,Chair,abc,3\n"
            "digital,D010,Software,49.90,20\n"
        )

        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "test_products.csv")

            with open(path, "w", encoding="utf-8") as file:
                file.write(csv_data)

            load_products(path, inventory, self.supplier)

        # Only two valid products should be loaded
        self.assertEqual(len(inventory.products), 2)
        self.assertIsNotNone(inventory.search_product("P010"))
        self.assertIsNotNone(inventory.search_product("D010"))

    def test_csv_missing_file(self):
        inventory = Inventory()

        with tempfile.TemporaryDirectory() as folder:
            missing_path = os.path.join(folder, "missing.csv")
            load_products(missing_path, inventory, self.supplier)

        self.assertEqual(len(inventory.products), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
