# Domain class representing a sale
class Sale:
    def __init__(self, item_name: str, price: float):
        self._item_name = item_name
        self._price = price

    def get_item_name(self) -> str:
        return self._item_name

    def get_price(self) -> float:
        return self._price


# "Pure Fabrication" class responsible for storing Sale objects
class SaleStorage:
    @staticmethod
    def save_sale(sale: Sale):
        # For demonstration, we'll just print out the sale details.
        # In a real application, this might connect to a database or write to a file.
        print(f"Saving sale for item: {sale.get_item_name()} with price: ${sale.get_price():.2f}")


if __name__ == "__main__":
    # Create a Sale object
    my_sale = Sale("Laptop", 999.99)

    # Use the fabricated SaleStorage class to save the Sale
    SaleStorage.save_sale(my_sale)

