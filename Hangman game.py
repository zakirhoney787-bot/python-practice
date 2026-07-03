import random

l_words=['apple','ball','cat','doll','elephant']
a_place=[]
alpha_list=[]
word=random.choice(l_words)

for i in range(len(word)):
    a_place.append('_')

for a in word:
    alpha_list.append(a)

chance=6
while chance>=1:
    print(a_place)
    guessed_alpha=input("Enter your guessed alphabet ==> ")

    for j in range(len(word)):
        if alpha_list[j]==guessed_alpha:
            a_place[j]=guessed_alpha
            print("\nYou entered the correct alphabet")
            print(a_place)
            continue
            if a_place==alpha_list:
                print("' YOU WON '")
        chance-=1
        print(a_place)
        elif chance==5:
            print("""
                    +-------+---
                    |       |
                    |       O
                    |
                    |
                    |
                    |
                    +=========
""")

            
        elif chance==4:
            print("""
                    +-------+---
                    |       |
                    |       O
                    |       |
                    |
                    |
                    |
                    +=========
""")
        elif chance==3:
            print("""
                    +-------+---
                    |       |
                    |       O
                    |      /|
                    |
                    |
                    |
                    +=========
""")
        elif chance==2:
            print("""
                    +-------+---
                    |       |
                    |       O
                    |      /|\
                    |
                    |
                    |
                    +=========
""")

        elif chance==1:
            print("""
                    +-------+---
                    |       |
                    |       O
                    |      /|\
                    |      /
                    |
                    |
                    +=========
""")
    

        elif chance==0:
            print("""
                    +-------+---
                    |       |
                    |       O
                    |      /|\
                    |      / \
                    |
                    |
                    +=========
""")
   
        else:
            pass
    print("\nyour guessed alphabet is incorrect")

    print(f"your remaining chances are {chance}")