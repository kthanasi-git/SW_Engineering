class Payment():
    def __init__(self, kind):
        self.kind = kind

    def authorize(self, amount, driver_license_num: str="", card_number: str="", expiry_date: str=""):
        if self.kind == "check":
            print(f"Processing check for ${amount}, ${driver_license_num}")
        elif self.kind == "cash":
            print(f"Accepting ${amount} in cash")
        elif self.kind == "credit":
            print(f"Processing credit card for ${amount} ${card_number} ${expiry_date}")
        else:
            raise ValueError("Unknown payment type")

# Sale Class (Handles Business Logic)
class Sale:
    def make_check_payment(self, amount, driver_license_num: str):
        print("Sale: Creating Check Payment...")
        payment = Payment("check") # Sale owns the payment object
        payment.authorize(amount, driver_license_num=driver_license_num)

    def make_credit_payment(self, amount, card_number: str, expiry_date: str):
        print("Sale: Creating Credit Payment...")
        payment = Payment("credit") # Sale owns the payment object
        payment.authorize(amount, card_number=card_number, expiry_date=expiry_date)

    def make_cash_payment(self, amount):
        print("Sale: Creating Credit Payment...")
        payment = Payment("cash") # Sale owns the payment object
        payment.authorize(amount)


# POST Class (Acts as Both UI and Controller)
class POST:
    def __init__(self):
        self.sale = Sale()  # Composition: POST owns Sale

    def make_check_payment(self, amount, driver_license_num: str):
        print("POST: Delegating Check Payment to Sale...")
        self.sale.make_check_payment(amount, driver_license_num)

    def make_credit_payment(self, amount, card_number: str, expiry_date: str):
        print("POST: Delegating Credit Payment to Sale...")
        self.sale.make_credit_payment(amount, card_number, expiry_date)

    def make_cash_payment(self, amount):
        print("POST: Delegating Cash Payment to Sale...")
        self.sale.make_cash_payment(amount)

if __name__ == "__main__":
    pos_system = POST()  # The POS system (POST) serves as the Controller

    # Simulating user actions
    pos_system.make_check_payment(100.5, "D123456")
    print("---------------------------")
    pos_system.make_credit_payment(100.5, "4111-1111-1111-1111", "12/26")
    print("---------------------------")
    pos_system.make_cash_payment(100.5)

