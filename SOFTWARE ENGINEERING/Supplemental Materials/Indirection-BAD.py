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


class CreditAuthorizationService:
    """Domain class directly calling the OS-level API, without indirection."""

    def authorize_payment(self, amount: float) -> bool:
        # Directly calling the OS-level modem functions
        OSModemAPI.os_dial("1-800-CREDIT")

        # Construct a simple payment message
        message = f"PAYMENT: {amount:.2f}"
        OSModemAPI.os_send(message)

        # Get a response from the OS API
        response = OSModemAPI.os_receive()

        # End the call
        OSModemAPI.os_hangup()

        # Interpret the response
        if response == "AUTH_OK":
            print(f"Payment of ${amount:.2f} authorized.")
            return True
        else:
            print(f"Payment of ${amount:.2f} NOT authorized.")
            return False


if __name__ == "__main__":
    # Create the domain service and directly call the OS API
    auth_service = CreditAuthorizationService()

    # Attempt to authorize a payment
    auth_service.authorize_payment(99.99)

