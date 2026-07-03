class Cinema():
    def show_movies(self):
        with open('movies.txt') as f:
            file=f.readlines()
            for line in file:
                print(line)

    def add_movie(self,new_mov_name):
        with open("movies.txt") as f:
            f.write(new_mov_name)
    
class movies():
    def __init__(self,movie,totalseats=20):
        self.movie=movie
        self.totalseats=totalseats
    def avail_seat(self):
        print(f"Movie : {self.movie}")
        print(f"Seat number : {self.totalseats}")
        self.totalseats-=1

    def show_details(self):
        print(f"seats booked : {20 - self.totalseats}")
    
    def saving_file(self):
        with open('file.txt','a') as file:
            file.write(f"Movie : {self.movie} \n seatbooked : {20-self.totalseats}")
        
class User():
    def __init__(self,name):
        self.name=name
        print(f"Name : {self.name}")

def back_up_plane():
    with open(movies.txt) as f:
        files=f.read()
        for line in files:
            l=line.split()
            if booking_movie not in l:
                print("please enter new movie its procceded :")
                break
                return False
            return True            

a=Cinema()
i=1
while i<=5:
    a.show_movies()
    booking_movie=input("Enter the movie name ,Available movies are above ")
    # back_up_plane()
    while True:
        name=input("enter your name here : ")
        b=User(name)
        c=movies(booking_movie)
        c.avail_seat()
        c.show_details()
        question=input(f"Is there anyone who will book seat in this move : {booking_movie}")
        
        if question!='yes':
            c.saving_file()
            break
    i+=1
q=input("Do you want to see the files : ")
if q!='no':
    with open('file.txt') as file:
            g=file.read()
            print(g)