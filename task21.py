#define a class that can add subctract two numbers
class calculation:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b) 
a = int(input("enter 1st number" ))
b = int(input("enter 2nd number")) 
c = calculation()
c.add(a,b)
c.sub(a,b)        