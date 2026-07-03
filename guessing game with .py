import random as rn
num=rn.randint(1,10)

while True:
    Gnum=int(input("what you guessed about that number it is between 1 and 20 \n enter it ==> "))
    if num==Gnum:
        print("YOU ARE DONE !")
        break

    elif Gnum>(num-3) and Gnum <num:
        print("you are close but low ")

    elif Gnum <num+3 and Gnum > num :
        print("you are close but high ")

    elif Gnum<num:
            print("too low ")

    elif Gnum>num :
        print("too high ") 

    else:
        print("it is out of range ")