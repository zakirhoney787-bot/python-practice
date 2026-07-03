with open('currency.txt') as f:
    lines = f.readlines()

currencydict={}
for line in lines:
    parsed=line.split()
    currencydict[parsed[0]]=float(parsed[1])

def currency_convertor():
    amount=int(input("Enter your amount you wanna convert ==> "))
    in_what=input(f"in which currency you wanna convert ,Available options ={currencydict}\n\n==> ")
    converted=float(amount*currencydict[in_what])
    print(f"this {amount} in {in_what} is {converted} {in_what}")

currency_convertor()