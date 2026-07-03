import string

alphabets = list(string.ascii_lowercase+' ')

print(alphabets)

coded=''
def coder(name):
    global coded
    for j in name:
        for idx,i in enumerate(alphabets):
            if i==j:
                if i=='y' or i=='z':
                    coded = coded + i
                else:
                    coded = coded + alphabets[(idx+2) % len(alphabets)]
    print("this is your writen scentence :\n", coded)
    
decoded=''
def decoder(coded):
    '''
    this function is not applicable to decode scentences,  
    SORRy
    '''
    global decoded
    for j in coded:
        for idx,i in enumerate(alphabets):
            if i==j:
                if i=='y' or i=='z' or i==' ' or i=='b' or i=='a':
                    decoded = decoded + alphabets[idx]
                else:
                    decoded = decoded + alphabets[(idx-2) % len(alphabets)]

    print("this is the actual writen scentence :\n", decoded)

name=input("Enter your message scentence :\n")
name=list(name)
coder(name)
ask=input("do you want to decode your name ?\n")
if ask!='no':
    coded=list(coded)
    decoder(coded)
