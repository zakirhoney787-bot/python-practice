Q1=input("sublimation is ____ process :\na)Endothermic \nb)exothermic \nc)Thermal\n")
Q2=input("bionomial theorem has ____ terms :\na)2 \nb)3 \nc)1\n")
Q3=input("which part of human balance body wrt gravity :\na)nose \nb)brain \nc)ear\n")
i=0
if Q1=='a':
    i+=1
if Q2=='a':
    i+=1
if Q3=='c':
    i+=1

print(f"this is your score :{i}/3")

if i==3:
    print("great work")