# Payment Class
class Payment:
    def __init__(self, amount: float):
        self.amount = amount
        print(f"Payment of ${amount:.2f} created.")

    def process(self):
        print(f"Processing payment of ${self.amount:.2f}.")


# Sale Class (Internally Creates Payment)
class Sale:
    def __init__(self, total: float):
        self.total_amount = total
        self.payment = None

    def make_payment(self):
        print("Sale creates the Payment (GOOD DESIGN!)")
        self.payment = Payment(self.total_amount)  # Sale is responsible for Payment creation
        self.payment.process()


# Register Class (Delegates to Sale)
class Register:
    def make_payment_for_sale(self, sale: Sale):
        print("Register delegates payment creation to Sale.")
        sale.make_payment()


if __name__ == "__main__":
    register_obj = Register()
    sale_obj = Sale(100.50)  # Sale of $100.50

    register_obj.make_payment_for_sale(sale_obj)  # Register initiates the payment process

