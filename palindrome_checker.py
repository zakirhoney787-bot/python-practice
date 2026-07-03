def palindrome_checker(name):
    cleaned = name.lower().replace(" ", "")

    if name[::-1]==cleaned:
        print("it is a palindrome !")
    else:
        print("it is a not palindrme ")

name=input("enter the thing name whose you wanna know \n whether is it a palindrome or not : ")
palindrome_checker(name)