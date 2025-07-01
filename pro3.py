a = float(input("enter first number:"))
b = float(input("enter second number:"))
print("select operation: +, -, *, /")
op = input("enter operation:")

if op == '+':
    print("result:", a + b)
elif op == '-':
    print("result:", a - b)
elif op == '*':
    print("result:", a * b)
elif op == '/':
    if  b != 0:
        print("result:", a / b)
    else:
        print("cannot divide by zero")
else:
    print("invalid operation")


