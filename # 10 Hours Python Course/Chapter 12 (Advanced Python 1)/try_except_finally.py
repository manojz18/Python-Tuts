# try:
#     n = int(input("Enter the number: "))
#     print(n)

# except ValueError as v: #specially fro ValueError
#     print(v)
#     print("Thank you")

# finally:
#     print("I am Inside Finally")

#                 VS

# print("Without finally can also run this that what is difference, the difference lies in function")


def solve():
    try:
        n = int(input("Enter the number: "))
        print(n)
        return n

    except ValueError as v: #specially fro ValueError
        print(v)
        print("Thank you")
        return n

    finally:
        print("I am Inside Finally")


print(solve())