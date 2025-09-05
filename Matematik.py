num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Saskaitīt, atņemt, dalīt, vai reizināt?")
ch = input("Enter any of these for  operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, "=", result)