def add_note():
    with open('messages.txt', 'a') as f:
        note_name=input("what is the note you want to add==> ")
        f.write(note_name + "\n")

def view():
    with open('messages.txt') as f:
        print(f.read())

def delete(x):
    file =view()
    for line in file :
        if x
            

def search(x):
    with open('messages.txt') as f:
        for line in f:
            found=False
            if x.lower() in line.lower():
                print(f"Match found: {line.strip()}")
                found=True
while True:
    purpose=input("what you want to do here ? \n")
    try:
        if purpose=='add':
            add_note()
        elif purpose=='view':
            view()
        elif purpose=='search':
            try:
                name=input("what is the name of note ?")
                search(name)
            except FileNotFoundError:
                print("that named note doesn't found ")
        elif purpose=='delete':
            try:
                name=input("what name you to delete : ")
                delete(name)
                view()
            except Exception as e:
                print(e)
        elif purpose=='exit':
            break
        else:
            pass
    except ValueError:
        print("invalid input please enter it again")
