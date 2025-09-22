# Payment class holds the amount tendered.
class Payment:
    def __init__(self, amount: float):
        self._amount_tendered = amount  # protected by convention

    def get_amount_tendered(self) -> float:
        return self._amount_tendered


# Sale class has a reference to a Payment.
class Sale:
    def __init__(self, payment: Payment):
        self._payment = payment

    # Exposes the Payment object directly (bad design).
    def get_payment(self) -> Payment:
        return self._payment


# POST class references a Sale.
class POST:
    def __init__(self):
        self._sale = None  # No sale assigned initially

    def set_sale(self, sale: Sale):
        self._sale = sale

    # BAD DESIGN: Directly accessing Payment through Sale.
    def payment_amount(self) -> float:
        if self._sale is not None:
            # "POST" -> "Sale" -> "Payment" -> "amountTendered"
            return self._sale.get_payment().get_amount_tendered()
        return 0.0


if __name__ == "__main__":
    # Create a Payment object.
    payment = Payment(50.0)

    # Create a Sale object that refers to the Payment.
    sale = Sale(payment)

    # Create a POST object using the default constructor (no parameters).
    post = POST()
    post.set_sale(sale)

    # Demonstrate the violation of "Don't Talk to Strangers".
    print(f"Payment Amount (Bad Design): {post.payment_amount()}")

