print("WELLCOME TO OUR MARKET")
c=0
while True:
    money=int(input("Enter the item's price ==> "))
    d=lambda x,y:x+y
    c =d(c,money)
    ask=input("do wanna continue ...")
    if ask!='yes':
        print(f"this is the total amount {c} Dollars \n Okay goodbye")
        break