con_dict={'zakir':3453751794,
    'zakir_z':3213724696,
    'azhar':3128602418,
    'dad': 3043548586 ,
    'bablo':3454692158,
    'zebra':4345566997     }
def search():
    name=input("search.... ")
    if name in con_dict:
        print(f"this is the number {con_dict[name]} of {name}")
    else:
        print("not found !")

def delete():
    name=input("what is name of the contact, which contact you wanna delete... ")
    if name in con_dict:
        del con_dict[name]
        print(f"{name} has deleted from contacts")
    else:
        print("Contact not found")
def add():
    name=input("what is name of the contact... ")
    num=int(input(f"what is the contact number of {name}... "))
    con_dict[name]=num

def view():
    print(con_dict)

while True:
    purpose=input("what would you like to do in our app ==>")
    if purpose=='search':
        search()

    elif purpose=='delete':
        how_many=int(input("how many contacts you want to delete ==>"))
        for i in range(how_many):
            delete()
    elif purpose=='add':
        how_many=int(input("how many contacts you want to add ==>"))
        for i in range(how_many):
            add()

    elif purpose=='view':
        view()

    elif purpose=='exit':
        print("okay goodbye ")
        break

    else:
        print("invalid input ! ")

