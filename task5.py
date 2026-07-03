#sum of digits
x= int(input("Enter the number "))
sum = 0
while x > 0:
    sum = sum +( x % 10)
    x = x // 10
print(sum )