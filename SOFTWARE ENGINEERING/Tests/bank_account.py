class BankAccount:
    """A simple bank account class for demonstration."""

    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """Add money to the account and return the new balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += (amount)
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraw money from the account and return the new balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def is_overdrawn(self) -> bool:
        """Return True if the account is overdrawn (balance < 0)."""
        return self.balance < 0

