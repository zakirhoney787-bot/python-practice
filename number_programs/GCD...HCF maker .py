num1=int(input("enter the 1st number ==> "))
num2=int(input("enter the 2nd number ==> "))
commonf=[]
n1factors=[]
n2factors=[]

def gcd(x,y):
    j=2
    while True:
        if x % j == 0:
            y.append(j)
            x=x/j
            if x==1:
                break
        else:
            j+=1
def orgnr(l1,l2):
    for i in l1:
        for k in l2:
            if i==k:
                commonf.append(i)
gcd(num1,n1factors)
gcd(num2,n2factors)
orgnr(n1factors,n2factors)
max_num = max(commonf)
print(f"this is the GCD of your number {max_num}")
