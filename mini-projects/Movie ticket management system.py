class movies():
    def __init__(self, movname, totalseats=20):
        self.movname=movname 
        self.totalseats=20
        self.bookedseats=0
    

    def availseats(self,own):
        i=0
        while own>0:
            if own!=0:
                if self.totalseats-movies.bookedseats>0:
                    movies.bookedseats = movies.bookedseats+1
                    print(f"this is your seat {movies.bookedseats}")
                    i+=1
                    own-=1
                else:
                    print("no seats available more")
                    break

    def showdetails(self):
        print(f"The movie is {self.movname} and\nTotal seats booked are {movies.bookedseats} out of {self.totalseats}")

class User():
    def __init__(self, name):
        self.name=name

    def bookingperson(self):
        print(f"{self.name} has owned seat in {movies.movname}")

    def view_details(self):
        print(f"{20-movies.bookedseats} are available ")

class Cinema():
    def __init__(self,movnames="movies name.txt"):
        self.movnames=movnames  

    def show_movies(self):
        with open(self.movnames) as f:
            lines=f.read()
            print("Cinema\n-----\n|")
            for line in lines:
                print(f"|---{line}")

    def add_movie(self,addmovname):
        with open(self.movnames,'w') as f:
            f.write(addmovname+'\n')

name=input("Enter your name ==>")
a=User(name)
with open(a.movnames) as f:
    lines=f.read()
    for line in lines:
        cus=movies(line)
        while True:
            seat=20
            cus.showdetails()
            b=User()
            b.ticketavailable()
            ask=input("would you like to book seat ? ==> ")
            if ask=='yes':
                b.bookingperson(name)
                own=int(input("how many seats you want to book ==> "))
                cus.availseats(own)
                seat-=1
            else:
                break

question=input("Do you want to add movie ==>")
if question!='no':
    namem=input("what is the name of movie")
    a.add_movie(namem)
        