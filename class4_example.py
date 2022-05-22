class Accoona:

    director = "John Lobo"

    #Constructor : when we assign value to object it will  pass through constructor  
    def __init__(self,fname,lname,age):
        self.first_name = fname
        self.last_name = lname
        self.age = age


    def printf(self):
        print(self.first_name,self.last_name,self.age)

    @staticmethod
    def scanf(input):
        ab = input
        print(ab)

    @classmethod
    def my_class(cls,ss):
        cls.ss = ss
        print(ss)
    
    @classmethod
    def alternate_constructor(cls,object_data):
        fname,lname,age = object_data.spilt(',')
        return cls(fname,lname,age)


class Global(Accoona):
    def director_name(self):
        print(f"Accoona Global director is {self.director}")


b = Accoona("Dev",'Satpue',25)
Accoona.printf(b)
b.printf()
Accoona.scanf('Data Analyst')
Accoona.my_class('Hi')
b.my_class('Hello')
Global.director_name(b)    
