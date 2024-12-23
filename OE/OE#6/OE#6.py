class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0: self.__balance += amount
        else: print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance: self.__balance -= amount
        else: print("Invalid withdrawal amount.")

    def display_info(self):
        print(f"Account Number: {self.__account_number}\nCurrent Balance: {self.__balance}")

    def set_balance(self, balance):
        if balance >= 0: self.__balance = balance
        else: print("Invalid balance.")

account = BankAccount("123456789", 2000.00)
account.display_info()
account.deposit(float(input("Add Amount: ")))
account.display_info()
account.withdraw(float(input("Deduct Amount: ")))
account.display_info()
account.set_balance(float(input("Set Balance: ")))
account.display_info()
