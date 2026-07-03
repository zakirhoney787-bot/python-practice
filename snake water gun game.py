import random 
objects=['snake','water','gun']
def area_tri(x,y):
    print(f"this is the area of triangle {1/2*x*y}")

hight=int(input("triangle's hight ==> "))
width=int(input("triangle's width ==> "))
area_tri(hight,width)

while True:
    ch=random.choice(objects)
    my_obj=input("enter your subject to beat python ==> ")
    if ch==objects[0] and my_obj==objects[2]:
        print("' CONGRATS YOU WON '")
    elif ch==objects[1] and my_obj==objects[0]:
        print("' YOU WON '")
    elif ch==objects[2] and my_obj==objects[1]:
        print("' YOU WON '")
    elif ch==my_obj:
        print("' DRAW '")
    else:
        print("YOU LOSE")
    
    print(f"this was the choice of python {ch}\n")
    ask=input(f"enter your opinion do you wanna play again==> ")
    if ask!='yes':
        break