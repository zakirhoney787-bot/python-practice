f_task=int(input("how many works/tasks you have to do :\n"))
list=[]

def adder(x):
    for i in range(x):
        name=input(f"what is the {i+1} task :=>")
        list.append(name)
    
    return list

def remover(x):
    
    for i in range(x):
        name=input("what is thats name  :=> ")
        for j in list:
            if name == j:
                list.remove(j)

    return list
print(adder(f_task))


while True:
    purpose=input("what do you wanna do add/remove/no :=>").lower()
    if purpose=='add':
        how_many=int(input("how many tasks you wanna add :=>"))
        print(adder(how_many))
    elif purpose=='remove':
        how_many=int(input("how many tasks you wanna remove :=>"))
        print(remover(how_many))
    elif purpose=='no':
        print("okay goodbye")
        break
    else:
        print("invalid input")