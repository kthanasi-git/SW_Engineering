# Sale Class (Handles Business Logic)
class Sale:
    def make_line_item(self, upc: str, qty: int):
        print(f"Sale: Adding item with UPC {upc} and quantity {qty}.")


# UI Class (BAD DESIGN: Directly Calls Business Logic)
class POSTApplet:
    def on_enter_item(self, upc: str, qty: int):
        print("POSTApplet: Handling user input (BAD DESIGN!)")
        sale = Sale()  # UI directly interacts with domain logic (bad practice)
        sale.make_line_item(upc, qty)


if __name__ == "__main__":
    ui = POSTApplet()
    ui.on_enter_item("123456", 2)  # UI directly calls Sale

