class Employee():

    company="Microorganism"
    num_employee=0
    
    @staticmethod
    def valid_salary(salary):
        if (salary>0):
            return True
        print(f"{salary} is not possible !")
        return False

    @classmethod
    def company_change(cls,new_name):
        cls.company=new_name

    def __init__(self,name,dpt,salary,upartment):
        if Employee.valid_salary(salary):
            self.name=name
            self.salary=salary
            self.dpt=dpt
            self.upt=upartment
            Employee.num_employee+=1
    def dec(fx):
        def inv(self):
            print("Wellcome")
            fx(self)
            print("Goodbye")
        return inv
    
    def interest(self):
        print(f"Your yearly interest is {self.salary/10} in this {Employee.num_employee}\n sized company\n")
    @dec
    def show_details(self):
        print(f"{self.name} | {self.dpt} | {self.upt} | {self.salary} | {self.company}")
    
ep1=Employee('zakir','AI',50,'husnains house')   
ep1.company='sarif'
ep1.show_details()
ep1.interest()

ep2=Employee('ali','graphicdesigner',5000,'Army')   
ep2.show_details()
ep2.interest()