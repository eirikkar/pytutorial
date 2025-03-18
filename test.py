from user import user

# Python program to demonstrate
# main() function
GLOBAL_VARIABLE = 10


def example_function():
    local_variable = 5
    print(GLOBAL_VARIABLE + local_variable)


class BankAccount:
    def __init__(self, balance: int) -> None:
        self._balance = balance

    @property
    def balance(self) -> int:
        return self._balance

    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self._balance += amount


# Defining main function
def main() -> None:
    user1 = user(1, "johndoe", "John", "Doe", 25)
    user2 = user(2, "janedoe", "Jane", "Doe", 22)
    print(user1, user2)
    print(user1.username)
    example_function()
    account = BankAccount(100)
    account.deposit(50)
    print(f"Balance: {account.balance}")
    account.withdraw(150)
    print(f"Balance: {account.balance}")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
