
# try:
#     n = int(input("Enter the number: "))
#     print(n)

# except ValueError as v: #specially fro ValueError
#     print(v)
#     print("Thank you")

# except ZeroDivisionError as z:
#     print(z)

# except Exception as e: #default Exception
#     print(e)

# print("Thanks")


# Raising an error

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

if(b == 0):
    raise ZeroDivisionError("The Number cannot be divided by 0")
else:
    print(f"The division of a/b is {a/b}")