# Payment Class
class Payment:
    def __init__(self, amount: float):
        self.amount = amount
        print(f"Payment of ${amount:.2f} created.")

    def process(self):
        print(f"Processing payment of ${self.amount:.2f}.")


# Sale Class (Receives a Payment Object)
class Sale:
    def __init__(self):
        self.payment = None

    def add_payment(self, payment: Payment):
        print("Sale received the payment.")
        self.payment = payment
        self.payment.process()


# Register Class (BAD DESIGN: It creates Payment)
class Register:
    def make_payment_for_sale(self, sale: Sale, amount: float):
        print("Register creates the Payment (BAD DESIGN!)")
        payment = Payment(amount)   # Register is responsible for creating Payment (bad)
        sale.add_payment(payment)   # Register passes it to Sale
        # No explicit delete needed in Python (garbage collector handles it)


if __name__ == "__main__":
    register_obj = Register()
    sale_obj = Sale()

    register_obj.make_payment_for_sale(sale_obj, 100.50)  # Register initiates the payment process

