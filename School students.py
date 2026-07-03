
class students():
    @staticmethod
    def valid_marks(marks):
        if 0<marks<100:
            return True
        print("marks are not valid")
        return False
    
    stud=0
    school='GBHSS NWM'
    topper_list=[]
    info_file="info of students.txt"
    def __init__(self ,name ,ruleno, marks,grade=None):
         
        if students.valid_marks(marks):
            self.marks = marks
            self.name = name
            self.ruleno=ruleno
            students.stud+=1
            if marks>=90:
                self.grade='A'
                students.topper_list.append(self.name+' with '+ str(self.marks))
            elif marks>=80:
                self.grade='B'
            elif marks>=70:
                self.grade='C'
            else:
                self.grade='FAIL'

    @classmethod
    def change_school(cls,new_name):
        cls.school=new_name

    def topper(self):
        print(f"these are all the topers : {students.toppers_list}")

    def show_details(self):
        print(f"Student : {self.name}")            
        print(f"Rule number : {self.ruleno}")            
        print(f"Marks : {self.marks}")            
        print(f"Grade : {self.grade}")            
        print(f"School : {students.school} \n\nNow {self.name} is the part of {students.stud} student school\n")
        return f"Student : {self.name}\nRule number : {self.ruleno}\nMarks : {self.marks}\nGrade : {self.grade}\nSchool : {students.school} \n"
    @staticmethod
    def file():
        with open(students.info_file,'w') as stinf:
            stinf.write(students.show_details())

    def st_delete(self,noun):
        with open(students.info_file) as f:
            lines=f.read()

        with open(students.info_file, 'w')  as wf:
            info_list=[]
            for line in lines:
                info_list=line.split()
                if noun in info_list:
                    print(f"{self.noun} found")
                    wf.write(" ")
                    print(f"{self.noun} deleted now")
                    break

    def search_student(self,s_name):
        with open(students.info_file) as f:
            inf=[]
            paras=f.read()
            for line in paras:
                list=line.split()
                if s_name in inf:
                    print(f"{inf} these was the details ")
                    break
                else:
                    print(f"s_name does not exit bro")
    @staticmethod
    def see_details():
        students.file()
        with open(students.info_file) as file:
            page=file.read()
            i=0
            for line in page:
                print(f"{i}: {line}")

st=students('kabeer',804,81)
st.show_details()
st1=students('habib',805,71)
st1.show_details()
st2=students('muneeb',806,91)
st2.show_details()
st3=students('zakir',786,82)
st3.show_details()

while True:
    ask=input("what would you prefer to know about \nAvailable options : \nSee details\nSearch\nDelete\nTopper\nChange school\n ==> ")
    if ask=='see details':
        students.see_details()

    elif ask=='search':
        name=input("what is the name of student about you want know ==> ")
        students.search(name)

    elif ask=='topper':
        students.topper()

    elif ask=='change school':
        new_school_name=input("Enter the name of new school ==> ")

    else:
        print("Okay Goodbye")


    