# Sale Class (Handles Business Logic)
class Sale:
    def make_line_item(self, upc: str, qty: int):
        print(f"Sale: Adding item with UPC {upc} and quantity {qty}.")


# Controller Class (GOOD DESIGN: Separates UI from Business Logic)
class Controller:
    def __init__(self):
        self.sale = Sale()  # Controller owns business logic

    def enter_item(self, upc: str, qty: int):
        print("Controller: Processing user request.")
        self.sale.make_line_item(upc, qty)  # Delegates to Sale (Domain Layer)


# UI Class (Only Talks to Controller)
class POSTApplet:
    def __init__(self, controller: Controller):
        self.controller = controller

    def on_enter_item(self, upc: str, qty: int):
        print("POSTApplet: User pressed Enter Item button.")
        self.controller.enter_item(upc, qty)  # UI delegates to Controller


if __name__ == "__main__":
    controller = Controller()
    ui = POSTApplet(controller)

    ui.on_enter_item("123456", 2)  # UI calls Controller instead of Sale directly

