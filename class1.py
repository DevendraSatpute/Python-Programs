# help(str)
# What is OOPS
# It Is use for compleax program 
# Object Oriented Programming is a programming paradiagram that provide a means of structuring program.
# So that properties and behaviour are bundled into individual objects.
# Polymorphism
# Data Encapsulation
#

# Class
# All classes have a function called __init__(), which is always executed when the class is being initiated.

count = 0

class men:
    def __init__(self,n,a):
        self.name = n
        self.age = a

emp = men('john',37)
print(emp.name)
print(emp.age)


class person:
    def __init__(self,n,a):
        self.na = n
        self.ag = a
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.


    def my_fun(any_name):
        print("Hello, My name is "+ any_name.na)

obj = person('Dev','25')
obj.my_fun()
print(obj.ag)
# del obj
# print(obj.ag)# NameError: name 'obj' is not defined
obj.ag = 28
obj.na = "Devid"
print(obj.my_fun(),obj.ag)

# del obj.na # AttributeError: 'person' object has no attribute 'na'
print(obj.my_fun())

# if We don't know the how many paramater will going pass
def my_name(*kid):
    print('The older kid is '+ kid[2])

my_name("Dev","devid",'Olly')

# if we don't know how many
def your_fun(**kids):
    print('Youger kid is '+ kids["child1"])

your_fun(child1='jai',child2='dev')

def my_country(contry="India"):
    print('My country is '+ contry)

my_country('America')
my_country()

