# Payment class holds the amount tendered.
class Payment:
    def __init__(self, amount: float):
        self._amount_tendered = amount  # protected by convention

    def get_amount_tendered(self) -> float:
        return self._amount_tendered


# Sale class holds a reference to a Payment, but hides its details.
# It provides a method to retrieve the payment amount.
class Sale:
    def __init__(self, payment: Payment):
        self._payment = payment

    # Provides the payment amount without exposing the Payment object.
    def payment_amount(self) -> float:
        return self._payment.get_amount_tendered()


# POST class references a Sale.
class POST:
    def __init__(self):
        self._sale = None  # No sale assigned initially

    def set_sale(self, sale: Sale):
        self._sale = sale

    # GOOD DESIGN: POST only interacts with Sale, not directly with Payment.
    def payment_amount(self) -> float:
        if self._sale is not None:
            return self._sale.payment_amount()
        return 0.0


if __name__ == "__main__":
    # Create a Payment object.
    payment = Payment(50.0)

    # Create a Sale object that holds the Payment.
    sale = Sale(payment)

    # Create a POST object using the default constructor.
    post = POST()
    post.set_sale(sale)

    # Demonstrate the good design: POST doesn't directly access Payment.
    print(f"Payment Amount (Good Design): {post.payment_amount()}")

