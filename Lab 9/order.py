from order_line import OrderLine
from product import Product
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None=None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount = discount if discount is not None else NoDiscount()

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self.order_lines:
            total += order_line.calculate_subtotal()
        return self.discount.apply(total)

    def display_order(self) -> None:
        print(f"Order ID: {self.order_id}")

        for order_line in self.order_lines:
            print(
                f"{order_line.product.get_name()} x "
                f"{order_line.quantity} = "
                f"${order_line.calculate_subtotal():.2f}"
            )

        print(f"Order Total: ${self.calculate_total():.2f}")

    def remove_order_line(self, index: int) -> None:
        self.order_lines.pop(index)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount
    