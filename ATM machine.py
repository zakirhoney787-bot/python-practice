balance=0
def ask_amount():
    return int(input("how much you want to \n"))

money=ask_amount()
d=balance+money
c=balance-money

def check():
    print(f"your balance is {balance}dollars\n")

def dpst():
    print(f"now you've {d}dollars\n")

def wdr():
    print(f"your rest balance is {c}dollars\n")



while True:
    

    purpose=input("what is your purpose in zakir's bank :\n")

    if purpose=='widraw':

        if balance>1000:

            if money<=balance:
                wdr()

            else:
                print("you don't have the enough blance now please try again ;\n")
                continue

        else:
            print("less than 1000dollars balance having person are not applicable to widraw  ! ")

    elif purpose=='deposit':
        
        if money > 1000:
            dpst()

        else:
            print("this amount is very less than expected (1000) \n")
            continue

    elif purpose=='check':
        check()

    else:
        break