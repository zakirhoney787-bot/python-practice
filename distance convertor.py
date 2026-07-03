#1.60934
def converter(x):
    if purpose=='miles':
        print(f"{x}kilometers in the miles are {(x/1.60934)}")
    else:
        print(f"{x} miles in the kilometers is equals to {(x*1.60934)}")
distance=int(input("how many distance quantity you have ?"))
while True:
    purpose=input("you wanna convert that quantity in miles or kilometers or stopa")
    if purpose=='miles' or purpose=='kilometers':
        converter(distance)
    elif purpose=='stop':
        break
    else:
        print("invalid input")