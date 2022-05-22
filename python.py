# Comment
# comment are piece of text that live in your code but are ignored by the python interpreter
# This is a comment on its line
# inline comment should be less then 72 char


# variable
from ast import keyword


var = 'abc'
print(var)

# Keywords
# True False def class in None and not or as async await break continue
# import keyword
# keyword.kwlist

# help(keyword)

# lambda Function : Small anonymous function

x = lambda a: a +  10
print(x(2))

y = lambda w,x,z : w+x+z
print(y(2,3,5))

def my_fun(q):
    return lambda a: a * q

me = my_fun(2)
print(me(12))

class myclass():
    d = 18
    
p = myclass()
print(p.d)