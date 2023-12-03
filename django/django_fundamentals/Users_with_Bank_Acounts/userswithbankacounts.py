class User :
    def __init__(self,name) :
        self.name = name
        self.account = BankAccount(balance = 0,interest_rate = 0.01)
    
    def make_deposit(self,value):
        self.account.balance += value
        return self
        
    def make_withdrawal(self,value):
        self.account.balance -= value
        return self
        
    def display_user_balance(self):
        print(self.name, self.account.balance)
        return self
    def transfer_money(self,other_user,amount):
        self.account.balance -= amount
        other_user.account.balance += amount

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
            self.balance += self.balance*self.interest_rate
        else:
            print("Insufficient Current Balance, Yield Interest is not Applicable")
        return self

# Test the code