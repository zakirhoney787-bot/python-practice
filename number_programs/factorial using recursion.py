factorial=1
def fact(x):
    global factorial
    if x==1:
        return 1
    factorial*=x
    return fact(x-1)

num=int(input("enter a number ==>"))
fact(num)
print(f" the factorial is {factorial}")
i=0
while True:
    if factorial%10==0:
        i+=1
        factorial=factorial/10
    else:
        break

print(f"\n there were {i} trailing zeros in factorial")
