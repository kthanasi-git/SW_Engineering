class ProductSpecification:
    # Create new product specification
    def __init__(self, price, description="", upc=""):
        self.__price = price          # private (name mangling)
        self._description = description  # protected (by convention)
        self._upc = upc                # protected (by convention)

    # Get the product price
    def get_price(self):
        return self.__price


class SalesLineItem:
    # Store the quantity and product type for this line item
    def __init__(self, quantity, product: ProductSpecification):
        self.__quantity = quantity
        self.__product = product

    # Calculate the subtotal by multiplying quantity with item price
    def subtotal(self):
        return self.__quantity * self.__product.get_price()


class Sale:
    # Create container for list of items
    def __init__(self):
        self.__line_items = []

    # Create and add new item to the sale
    def add_line_item(self, quantity, product: ProductSpecification):
        lineitem = SalesLineItem(quantity, product)
        self.__line_items.append(lineitem)

    # Add a new item to the sale
    #def add_line_item(self, item: SalesLineItem):
    #    self.__line_items.append(item)

    # Produce the current total by summing the subtotals for each item
    def total(self):
        return sum(item.subtotal() for item in self.__line_items)


if __name__ == "__main__":
    # Create product specifications
    prod1 = ProductSpecification(25.0, "Book", "12345")
    prod2 = ProductSpecification(15.5, "Pen", "67890")

    # Create sale and add line items
    sale = Sale()
    sale.add_line_item(2, prod1)
    sale.add_line_item(5, prod2)

    # Calculate and display total
    print(f"Total sale amount: ${sale.total():.2f}")
