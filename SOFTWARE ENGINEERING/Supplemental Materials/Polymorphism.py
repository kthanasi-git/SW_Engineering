from abc import ABC, abstractmethod


# Abstract Base Class (Polymorphism)
class Payment(ABC):
    @abstractmethod
    def authorize(self):
        pass


# Concrete Class: Check Payment
class CheckPayment(Payment):
    def __init__(self, driver_license_num: str):
        self.driver_license_num = driver_license_num
        print(f"Check Payment created with Driver's License: {self.driver_license_num}")

    def authorize(self):
        print(f"Authorizing Check Payment using Driver's License: {self.driver_license_num}")


# Concrete Class: Credit Payment
class CreditPayment(Payment):
    def __init__(self, card_number: str, expiry_date: str):
        self.card_number = card_number
        self.expiry_date = expiry_date
        print(f"Credit Payment created with Card Number: {self.card_number} and Expiry: {self.expiry_date}")

    def authorize(self):
        print(f"Authorizing Credit Payment using Card: {self.card_number} Expiry: {self.expiry_date}")


# Sale Class (Handles Business Logic)
class Sale:
    def make_check_payment(self, driver_license_num: str):
        print("Sale: Creating Check Payment...")
        payment = CheckPayment(driver_license_num)  # Sale owns the payment object
        payment.authorize()

    def make_credit_payment(self, card_number: str, expiry_date: str):
        print("Sale: Creating Credit Payment...")
        payment = CreditPayment(card_number, expiry_date)  # Sale owns the payment object
        payment.authorize()


# POST Class (Acts as Both UI and Controller)
class POST:
    def __init__(self):
        self.sale = Sale()  # Composition: POST owns Sale

    def make_check_payment(self, driver_license_num: str):
        print("POST: Delegating Check Payment to Sale...")
        self.sale.make_check_payment(driver_license_num)

    def make_credit_payment(self, card_number: str, expiry_date: str):
        print("POST: Delegating Credit Payment to Sale...")
        self.sale.make_credit_payment(card_number, expiry_date)


if __name__ == "__main__":
    pos_system = POST()  # The POS system (POST) serves as the Controller

    # Simulating user actions
    pos_system.make_check_payment("D123456")
    print("---------------------------")
    pos_system.make_credit_payment("4111-1111-1111-1111", "12/26")

