class bankaccount():
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        print(f"{self.name} : Your balance is {self.balance}")

    def show_balance(self):
        print(f"{self.name}this is your balance now {self.balance}")

    def deposit(self ,amount):
        self.balance+=amount
        self.show_balance()
    def widraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"this is your {amount} dollars")
        self.show_balance()

p1=bankaccount('zakir',1000)
p2=bankaccount('ishfaque', 500)

while True:
    ask=input(f"{p1.name} ,What do you want to do here ? \n")
    if ask=='deposit':
        amount=int(input("how much amount you want to deposit in your account ==>"))
        p1.deposit(amount)
    elif ask=='send money':
        amount=int(input("enter the amount please : "))
        p2.deposit(amount)
        p1.widraw(amount)

    elif ask=='widraw':
        amount=int(input("how much amount you want to widraw in your account ==>"))
        p1.widraw(amount)

    elif ask=='exit':
        print("Okay Goodbye")
        break
    else:
        print("invalid input")
