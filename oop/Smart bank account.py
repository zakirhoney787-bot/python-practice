history=[]

class Bankaccount():
    def __init__(self ,name, balance):
        self.__balance=balance
        self.__name=name

    @property
    def name_balance(self):
        return self.__name,self.__balance
    
    @name_balance.setter
    def change(self, new_name,new_balance):
        self.__name=new_name
        self.__balance=new_balance

    @staticmethod
    def validity(fx):
        def vmfd():
            if (fx.amount>0):
                print("Okay, it's proceeding")
                fx()
                print("Thanks for using /visiting our bank")
            else:
                return
        return vmfd()
    @staticmethod
    def dec(fz):
        def f():
            print("You are really rich ")
            fz()
            print("Thanks")
        return f()
    @staticmethod
    def validity_w(fy):
        def vmfw():
            if (amount>1 and Bankaccount.__balance>=amount ):
                print("your transaction is proceeding ")
                fy()
                print("Transaction completed !")
        return vmfw()
    
    def list_maker(self,n,b):
        names.append(self.n)
        balances.append(self.b)

    def history_maker(self,x):
        history.append(self.x)


    #searcher and send functions remains to made
    
    def sub_searcher(self,names,balances):
        name=input("what is his name ? ==>")
        index=0
        for i,idx in enumerate(self.names):
            if i==name:
                idx=index
                break
        if name not in names:
            print(f"no man found with name {name}")
            q=input("do you want to create his name's account yes | no ==>")
            global n,b
            if q=='yes':
                n=name
                b=0
            else:
                return
        else:
            n=name
            b=balances[index]
        
    def send(self):
        Bankaccount.sub_searcher()
        amount=int(input(f"how much amount you want to send to {name} ==> "))
        reciever=Bankaccount(n,b)
        reciever.__balance+=amount
        print("The transaction successfully completed ")
        Bankaccount.list_maker(n,b)
        info=f"{self.name} | sent = {self.amount}"
        self.history_maker(info)

    @validity
    def deposit(self, amount):
        self.__balance+=amount
        print(f"this is your balance now {self.__balance}")
        print(f"your {self.amount} is in your account ")
        info=f"{self.name} | deposited = {self.amount}"
        self.history_maker(info)

    @validity_w
    def widraw(self ,amount):
        self.__balance-=amount
        print(f"{self.name} : these are your {self.amount} Dollars")
        info=f"{self.name} | widrawn = {self.amount}"
        self.history_maker(info)

names=[]
balances=[]

while True:
    name=input("what is your name ? ==> ")
    balance=int(input("please enter your balance ==>"))
    human=Bankaccount(name,balance)
    ask=input("waht do you want to do here | widraw | deposit | send | exit ")

    if ask=='widraw':
        amount=int(input("how much amount you want to widraw ==> "))
        human.widraw(amount)

    elif ask=='deposit':
        amount=int(input("how much amount you want to deposit ==>"))
        human.deposit(amount)
    
    elif ask=='send':
        call=Bankaccount.send()
        Bankaccount.dec(call)

    elif ask=='exit':
        q=input("Do your want the history of humans yes | no ==> ")
        if q!='no':
            for file in history:
                print(file)
        break
    