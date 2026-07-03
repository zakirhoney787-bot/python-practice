def fib_maker(x):
    if x==1:
        print(x)
        return
    y=(x-1)+(x-2)
    print(y)
    return fib_maker(x-1)
num=int(input("enter a number ==> "))
fib_maker(num)

a=5
b=10

c=a
a=b
b=c

print(a,b)