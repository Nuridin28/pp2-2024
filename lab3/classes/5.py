class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        cash_in = int(input())
        self.balance += cash_in
    def withdraw(self):
        cash_out = int(input())
        if self.balance < cash_out :
            print("Not enough money")
        else:
            self.balance -= cash_out
    def show_balance(self):
        print(self.owner, "balance's", self.balance)

e1 = Account("Me", 1000)
e1.deposit()
e1.withdraw()
        
e1.show_balance()
