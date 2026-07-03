cards=[]
for item in range(4):
    cards.append(1)


def flipper(x):
    if x==0:
        x+=1
    else:
        x-=1
    return x

while sum(cards)!=0:
    print(cards)
    cardnum=int(input("which card you want to flip \n 1 means are downsided and 0 means they are upsided ==> "))
    cardnum-=1
    if cards[cardnum]==0:
        print("only you can flip one down sided !")
    if cards[cardnum]!=0:
        a=flipper(cards[cardnum])
        cards[cardnum]=a
        
        b=flipper(cards[cardnum+1])
        cards[cardnum+1]=b
        
print(f"the all cards has been upsided \n{cards}")