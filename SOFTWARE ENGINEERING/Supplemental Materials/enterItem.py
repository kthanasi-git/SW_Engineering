from typing import Dict, List


class ProductSpecification:
    """
    Represents product details (UPC, name, price).
    """
    def __init__(self, upc: int = 0, name: str = "", price: float = 0.0):
        self._upc = upc
        self._name = name
        self._price = price

    def get_upc(self) -> int:
        return self._upc

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price


class ProductCatalog:
    """
    Holds a collection of product specifications.
    In a real system, this might do a database lookup.
    """
    def __init__(self):
        self._products: Dict[int, ProductSpecification] = {
            12345: ProductSpecification(12345, "Apple", 0.50),
            67890: ProductSpecification(67890, "Banana", 0.30),
        }

    def specification(self, upc: int) -> ProductSpecification:
        # Return a valid product if found, else a dummy placeholder
        return self._products.get(upc, ProductSpecification(upc, "UnknownProduct", 0.0))


class SalesLineItem:
    """
    Represents a single line item in a sale (one product + quantity).
    """
    def __init__(self, spec: ProductSpecification, qty: int):
        self._spec = spec
        self._quantity = qty

    def display(self):
        subtotal = self._spec.get_price() * self._quantity
        print(
            f"Item: {self._spec.get_name()}, "
            f"UPC: {self._spec.get_upc()}, "
            f"Qty: {self._quantity}, "
            f"UnitPrice: {self._spec.get_price():.2f}, "
            f"Subtotal: {subtotal:.2f}"
        )


class Sale:
    """
    Represents an entire sale, containing multiple line items.
    """
    def __init__(self):
        self._line_items: List[SalesLineItem] = []

    def make_line_item(self, spec: ProductSpecification, qty: int):
        sli = SalesLineItem(spec, qty)
        self._line_items.append(sli)

    def display_line_items(self):
        for item in self._line_items:
            item.display()


class POST:
    """
    The 'POST' (Point Of Sale Terminal).
    Receives the 'enter_item' message and coordinates with Sale and ProductCatalog.
    """
    def __init__(self):
        self._sale: Sale | None = None
        self._prod_catalog = ProductCatalog()
        self._new_sale = True

    def is_new_sale(self) -> bool:
        return self._new_sale

    def enter_item(self, upc: int, qty: int):
        if self.is_new_sale():
            self._sale = Sale()
            self._new_sale = False
        spec = self._prod_catalog.specification(upc)
        self._sale.make_line_item(spec, qty)

    def display_sale(self):
        if self._sale is not None:
            self._sale.display_line_items()
        else:
            print("No sale in progress.")


if __name__ == "__main__":
    post = POST()

    # Simulate entering two products
    post.enter_item(12345, 2)  # 2 Apples
    post.enter_item(67890, 3)  # 3 Bananas

    # Show the resulting sale items
    post.display_sale()

