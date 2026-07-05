# wap to check amstrong number (a number where the sum of cubes of digit is equal to number itself)
x = int(input("enter a number "))
temp = x
n = 0
while x > 0:
    a = x % 10
    n = n + a ** 3
    x = x // 10
if temp == n :
    print("it is amstrong number")  
else:
    print("not a amstrong number")      
    