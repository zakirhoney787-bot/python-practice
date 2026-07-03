students=int(input('how many student are in your class :\n'))
a=0
info={}

while True:
    if a < students:
        name=input("what is the name of student :")
        marks=int(input("what is the marks of student :"))
        info.update({name:marks})
        a=a+1
    else:
        break

print(f"the full list is this {info}")
mark=list(info.values())
names=list(info.keys())

for i in range(len(mark)):
    if mark[i]>=80:
        print(f"{names[i]} got the A grade bravo ")
    elif mark[i]>=60:
        print(f"{names[i]} got the B grade good ")
    elif mark[i]>=40:
        print(f"{names[i]} got the C grade ")
    else:
        print(f"{names[i]} , you should be proud yourself!")
        