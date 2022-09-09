x = int(input("First Number: "))
y = int(input("Second Number: "))

op = input("Choose Operation ([+] [-] [*] [/]): ")

if op == '+':
    ans = x + y
elif op == '-':
    ans = x - y
elif op == '*':
    ans = x * y
elif op == '/':
    ans = x / y

print(f"Your ans: {ans}")