class BankAccount:
    def __init__(self,balance = 0,interest_rate = 0.01):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
             self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.interest_rat
        else:
            print("Insufficient Current Balance, Yield Interest is not Applicable")
        return self

account1 = BankAccount()
account2 = BankAccount()

account1.deposit(100).deposit(100).deposit(100).withdraw(300).yield_interest().display_account_info()
account2.deposit(50).deposit(50).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()
