import csv
from product_factory import ProductFactory


def load_products(path, inventory, supplier):
    try:
        file = open(path, "r", newline="", encoding="utf-8")

    except FileNotFoundError:
        print("CSV file not found.")

    else:
        with file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    product = ProductFactory.create(
                        row["product_type"],
                        row["product_id"],
                        row["name"],
                        float(row["price"]),
                        int(row["stock_quantity"]),
                        1.0,
                        supplier
                    )

                    inventory.add_product(product)

                except (ValueError, KeyError) as error:
                    print(f"Skipping invalid row: {error}")

    finally:
        print("Load attempt finished.")