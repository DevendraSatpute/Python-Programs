# class company:
    # pass
'''class employee:
    pass

suresh = employee()
swati = employee()

suresh.fname = "Suresh"
suresh.lname = "Bhakte"
suresh.salary =  20000

swati.fname = "Swati"
swati.lname = "Indurkar"
swati.salary = 20000

print(suresh.salary)
'''
# from typing_extensions import Self


class Company:
    i = 1.5
    no_of_emp = 0
    
    #constructor
    def __init__(self,f,l,s):
        self.salary = s
        self.fname = f
        self.lname = l
        self.i = 1.3
        Company.no_of_emp +=1
    
    def increment_by_boss(self):
        self.salary = self.salary * Company.i

    def increment_by_hr(self):
        self.salary = self.salary * self.i

    @classmethod
    def change_increment(cls,rate):
        Company.i = rate 

    #Alternate Constructor
    @classmethod
    def from_str(cls,obj):
        fname,lname,salary = obj.split("-")
        return cls(fname,lname,salary)
    
    @staticmethod
    def is_open(day):   
        return True if day=="Sunday" else False


harsh = Company('Harsh','Alone',55000)
print(harsh.is_open('Sunday'))
print(Company.is_open('Monday'))
    
print(Company.no_of_emp)
suresh = Company("Suresh","Bhakte",23000)
print(Company.no_of_emp)
swati = Company("Swati","Indurkar",22000)
print(Company.no_of_emp)

print(suresh.salary,swati.lname)

print(swati.salary)
swati.increment_by_boss()
print(swati.salary)
swati.increment_by_hr()
print(swati.salary)
Company.change_increment(2)
swati.increment_by_boss()
print(swati.salary)

# print(swati.__dict__)  # to check out swati's variable
# print(Company.__dict__) # to check all the variable
print(Company.no_of_emp)

abhijit = Company.from_str("Abhijit-Patil-60000")

print(abhijit.salary,abhijit.fname,abhijit.lname)
