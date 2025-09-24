class Sale:
    def __init__(self):
        self.line_items = []

    # Sale responsibilities
    def add_line_item(self, product, quantity):
        self.line_items.append((product, quantity))

    def get_total(self):
        return sum(p.price * q for p, q in self.line_items)

    def complete(self):
        self.is_complete = True

    # Payment processing (should belong to Payment)
    def process_credit_card(self, number, amount):
        print(f"Processing credit card {number} for ${amount}")

    # Printing (should belong to ReceiptPrinter)
    def print_receipt(self):
        print("Printing receipt...")

    # Inventory (should belong to InventorySystem)
    def decrement_inventory(self, product, quantity):
        print(f"Decrementing {quantity} units of {product.name}")

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

