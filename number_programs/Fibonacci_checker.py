num=int(input("enter the number till which you wanna make fibonacci ==>"))

def fibonacci(x):
    for i in range(1,x+1):
        if x==1:
            print(f"this is the {x}th term's value = " ,1)
        else:
            print( f"this is the {x}th term's value ={(x-1) + (x-2)}")
        x-=1
fibonacci(num)