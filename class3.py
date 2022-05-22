# from ast import increment_lineno
# from curses.ascii import EM
# from sqlite3 import ProgrammingError


class Employee:
    increment = 0.10
    no_of_emp = 0

    #Constructor
    def __init__(self,fn,ln,s):
        self.fname = fn
        self.lname = ln
        self.salary = s
        self.increment = 0.05
        Employee.no_of_emp +=1
    
    def increment_by_boss(self):
        self.salary = self.salary + self.salary * Employee.increment
    
    def increment_by_hr(self):
        self.salary = self.salary + self.salary * self.increment

    @staticmethod
    def is_closed(day):
        return True if day=="Sunday" else False


    @classmethod
    def change_increment(cls,rate):
        Employee.increment += rate
        # increment = increment + rate
        

    # Alternate Constructor
    @classmethod
    def from_str(cls,str):
        fname,lname,salary = str.split("-")
        return cls(fname, lname,salary)


moshin = Employee("Moshin","Sheikh",40000)
apurva = Employee("Apurva","Matte",55000)
aashish =Employee.from_str("Aashish-Deshmukh-23000")

print(Employee.no_of_emp)
print(moshin.salary)
moshin.increment_by_hr()
print(int(moshin.salary))

print(apurva.salary)
apurva.increment_by_boss()
print(int(apurva.salary))

Employee.change_increment(0.5)

print(int(moshin.salary))
moshin.increment_by_hr()
print(int(moshin.salary))

rohit = Employee.from_str("Rohit-Sajdeh-48000")
print(rohit.fname,rohit.lname,rohit.salary)


print(int(apurva.salary))
apurva.increment_by_boss()
print(int(apurva.salary))

print(Employee.increment)
print(Employee.is_closed('Sunday'))


class Finance(Employee):
    def __init__(self, fn, ln, s,exp):
        super().__init__(fn, ln, s)
        self.experiance = exp

    def increment_by_boss(self):
        self.salary = self.salary + (self.salary * (0.02+self.increment))
        return

mohit = Finance("Mohit","Hiwase",55000,2)
print(mohit.salary)
mohit.increment_by_boss()
print(mohit.salary,mohit.fname,mohit.lname)

