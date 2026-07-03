import string as st
import random
def strong(x):
    y=x[:-1]
    x= y + random.choice(st.punctuation)
    return x

def passwordgen():
    stcomps=st.digits+st.punctuation+st.ascii_uppercase
    f1="".join(random.sample(stcomps,3))
    f2="".join(random.sample(stcomps,3))
    f3="".join(random.sample(stcomps,3))
    if any(char not in st.punctuation for char in f1):
        strong(f1)
    if any(char not in st.punctuation for char in f2):
        strong(f2)
    if any(char not in st.punctuation for char in f3):
        strong(f3)
    first=name+f1
    second=name+f2
    third=name + f3
    ask=input(f"which would you prefer to take your account password : available options: \n{first}\n{second}\n{third} ===> ")
    if ask=='first':
        print(f"this is your password now '{first}'\nand this is fully strong")
    elif ask=='second':
        print(f"this is your password now '{second}'\nand this is fully strong")
    if ask=='third':
        print(f"this is your password now '{third}'\nand this is fully strong")

name=input("enter your password having name please ...")

if len(name)>=8 and any(alph in st.punctuation for alph in name):
    print("your enter password is already strong")

else:
    print("your entered password is not strong sorry")
    passwordgen()
