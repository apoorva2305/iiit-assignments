#init function
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
name = input("enter your name :")
age = int(input("enter your age "))   
p = person(name,age)
print("your name is :" ,p.name)
print("your age is :",p.age)       