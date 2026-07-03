history=[]
while True:
    purpose=input("what you wanna do here in this calculator ==>")
    if purpose=='add':
        a=int(input("what is the value of a==> "))
        b=int(input("what is the value of b==> "))
         
        d=f"{a} + {b} = {(lambda x, y: x + y)(a, b)}"
        print(d)
        history.append(d)
        
    elif purpose=='sub' or purpose=='difference':
        a=int(input("what is the value of a==> "))
        b=int(input("what is the value of b==> "))
        d=f"{a} - {b} = {(lambda x, y: x - y)(a, b)}"
        print(d)
        history.append(d)
        
    elif purpose=='multiplication':
        a=int(input("what is the value if zero then resultant zero a==> "))
        b=int(input("what is the value if zero then resultant zero b==> "))
        d=f"{a} * {b} = {(lambda x, y: x * y)(a, b)}"
        print(d)
        history.append(d)
        
    elif purpose=='division':
        a=int(input("what is the value if zero then resultant zero a==> "))
        b=int(input("what is the value if zero then resultant zero b==> "))
        if b!=0:
            d=f"{a} / {b} = {(lambda x, y: x / y)(a, b)}"
            print(d)
            history.append(d)
        else:
            print('this is not possible due to b=0')

    elif purpose=='square':
        a=int(input("what is the value if zero then resultant zero a==> "))
        d=f"square of {a} = {(lambda x: x*x)(a)}"
        print(d)
        history.append(d)
    
    elif purpose=='sqrt':
        a=float(input("what is the value if zero then resultant zero a==> ")) 
        d=f"sqrt of {a} = {(lambda x: x**(1/2))(a)}"
        print(d)
        history.append(d)

    else:
        print("NOT OPTIONS LIKE THIS ARE AVAILAIBLE IN CALCULATOR")

    ask=input("do you wanna continue ?")
    if ask!='yes':
        break
q=input("do you wanna view history")
if q=='yes':
   print("\n".join(str(h) for h in history))

        
        