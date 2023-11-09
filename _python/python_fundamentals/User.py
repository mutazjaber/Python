class User :
    def __init__(self,name,balance= 0) :
        self.name = name
        self.balance =balance
        
    def make_withdrawal(self,value):
        self.balance -= value
        
    def display_user_balance(self):
        print(self.name, self.balance)
        
    def make_deposit(self,value):
        self.balance += value
    
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance +=amount


user1 = User("mutaz",5000)
user1.make_withdrawal(300)
user1.make_deposit(200)
user1.make_deposit(500)
user1.make_deposit(700)
user1.display_user_balance()
user2 =User("khaled",2000)
user2.make_withdrawal(100)
user2.make_withdrawal(200)
user2.make_deposit(100)
user2.make_deposit(300)
user2.display_user_balance()
user2.transfer_money(user1,amount=100)
user1.display_user_balance()
user2.display_user_balance()
# user3
# print(user1.balance,user2.balance)
# user1.display_user_balance()

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's 
# balance by the amount and add that 
# amount to other other_user's balance