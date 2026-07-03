dict={'zakir':77,
        'ishfaque': 78 ,
        'mumtaz':65,
        'muhammad':70,
        'huzaifa':76,
        'bakht':60,
        'nasir':45,
        'fakir':39}
def add_st():
    name=input("what is his name you wanna add \n==>")
    marks=int(input("how marks he got \n ==>"))
    dict.update[name]=marks

def view():
    print(dict)

def ubdate_marks():
    name=input("whose marks you want to change \n==> ")
    marks=int(input("okay, how much marks he got \n ==>"))
    dict[name]=marks

def delete_st():
    name=input("which student's history you wanna delete \n==> ")
    del dict[name]

marks=dict.values()
A_grade=[]
def grade_sys():
    for m in marks:
        if m>=80:
            print(f"{dict.keys[m]} got the 'A1' grade with {marks[m]}")
            A_grade.append(dict[m])
        elif m>=60:
            print(f"{dict.keys[m]} got the A grade with {dict[m]}")
        elif m>40:
            print(f"{dict.keys(m)} got B grade with {dict[m]}")
        else:
            print(f"{dict.keys(m)} has failed ")

def topper():
    for k in A_grade:
        for l in dict:
            print(l)