class Sale:
    def __init__(self):
        self.line_items = []
        self.is_complete = False

    def add_line_item(self, product, quantity):
        self.line_items.append(SaleLineItem(product, quantity))

    def get_total(self):
        return sum(item.get_subtotal() for item in self.line_items)

    def complete(self):
        self.is_complete = True


class SaleLineItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self):
        return self.product.price * self.quantity


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

