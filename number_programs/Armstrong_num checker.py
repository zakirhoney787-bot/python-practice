def cov_pow(p,s):
    sum=0
    for i in s:
        sum+=int(i)**p

    if int(number)==sum:
        print("the number is the armstrong number ")
    else:
        print("it is not a armstrong number !")
        
number=input("enter a number ==> ")
power=len(number)
cov_pow(power,number)
