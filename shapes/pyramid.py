num=int(input("enter the row number of the pyramid ==> "))
for row in range(num):
    for column in range(2*num-1):
        if (row+column)<(num-1) or (column-row)>(num-1):
            print(' ',end='')

        else:
            print("*", end="")

    print()