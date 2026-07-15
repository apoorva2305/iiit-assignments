# check weather a digit is divisible by 3
num = int(input("Enter a number: "))
last_digit = num % 10

if last_digit % 3 == 0:
    print("Yes, divisible by 3")
else:
    print("No, not divisible by 3")
