a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

try:
    print(a/b)

except ZeroDivisionError as e:
    print(e)