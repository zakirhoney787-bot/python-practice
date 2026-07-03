def temp_converter(x,p):
    if p=='f':
        print(f"{x}F in celcius is = {(x-32)*5/9}")
    elif p=='c':
        print(f"{x}C in the farnhet is = {(9/5)*x+32}")
    else:
        print("invalid input")
    
while True:
    p=input("what  you wanna convert celcius(C) or farnhet(F) in eachother==>n ")
    num=int(input(f"enter the value of {p}  ==> "))
    temp_converter(num,p)

    ask=input("do you wanna continue ==> ")
    if ask!='yes':
        break