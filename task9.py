# wap to count the total digits of a number
x = int(input("enter a number to count the digits "))
count = 0
while x > 0:
    x = x // 10
    count = count + 1
print(count)    