class library():
    def __init__(self, books):
        self.books=books

    def search(self,search):
        for book in self.books:
            if (book==search):
                print(f"this is your books {book}")
                break
        else:
            print("your typed book doesn't found")
    def view(self):
        for book in self.books:
            print(book)
    def length(self):
        print(f"okay this is the length of the library books {len(self.books)}")

    def add(self,addname):
        self.books.append(addname)
        print(self.books)

books=['richdad' ,'poor dad','think and grow' ,'atomichabits']

a=library(books)
while True:
    ask=input("what do you want to do here ?")
    if ask=='search':
        searched=input("enter the name of the book ==> ")
        a.search(searched)
    elif ask=='add':
        name=input("enter the name of the book :")
        a.add(name)
    elif ask=='view':
        a.view()

    elif ask=='length':
        a.length()
    elif ask=='exit':
        break
    else:
        print("invalid input")