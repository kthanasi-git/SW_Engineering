class OSModemAPI:
    """Simulated OS-level API for interacting with the modem device."""

    @staticmethod
    def os_dial(phone_number: str):
        print(f"OS: Dialing {phone_number}...")

    @staticmethod
    def os_send(data: str):
        print(f"OS: Sending data -> {data}")

    @staticmethod
    def os_receive() -> str:
        # For demonstration, we'll just return a fixed response
        response = "AUTH_OK"
        print(f"OS: Received response -> {response}")
        return response

    @staticmethod
    def os_hangup():
        print("OS: Hanging up the modem.")

class Comm:
    def connect(self):
        pass
    
    def send(self, data: str):
        pass

    def receive(self) -> str:
        pass

    def disconnect(self):
        pass

class Modem(Comm):
    """
    Indirection layer that provides a consistent interface for modem operations
    and hides OS-specific details from the domain classes.
    """
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def connect(self):
        OSModemAPI.os_dial(self.phone_number)

    def send(self, data: str):
        OSModemAPI.os_send(data)

    def receive(self) -> str:
        return OSModemAPI.os_receive()

    def disconnect(self):
        OSModemAPI.os_hangup()


class CreditAuthorizationService:
    """
    Domain class responsible for authorizing credit payments.
    It relies on the Modem interface rather than directly calling OS functions.
    """

    def __init__(self, modem: Comm):
        self._comm = modem  # Dependency injection

    def authorize_payment(self, amount: float) -> bool:
        # The domain class doesn't handle low-level modem details
        self._comm.connect()

        # Construct a simple payment message
        message = f"PAYMENT: {amount:.2f}"
        self._comm.send(message)

        # Get a response from the Modem (which delegates to the OS)
        response = self._comm.receive()

        # End the call
        self._comm.disconnect()

        # Interpret the response
        if response == "AUTH_OK":
            print(f"Payment of ${amount:.2f} authorized.")
            return True
        else:
            print(f"Payment of ${amount:.2f} NOT authorized.")
            return False


if __name__ == "__main__":
    # Create a Modem instance (our indirection layer)
    modem = Modem("1-800-CREDIT")

    # Create the domain service, injecting the Modem dependency
    auth_service = CreditAuthorizationService(modem)

    # Attempt to authorize a payment
    auth_service.authorize_payment(99.99)

