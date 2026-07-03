password=input("enter your password :\n")
i=0
for char in password:
    if char.isdigit():
        i+=1
    else:
        pass
if i>0 and len(password) >7:
    print('your password good to be secure')
else:
    print('your password not good to be secure !')