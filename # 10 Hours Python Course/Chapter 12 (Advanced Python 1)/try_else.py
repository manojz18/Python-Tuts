try:
    n = int(input("Enter the number: "))
    print(n)

except ValueError as v: #specially fro ValueError
    print(v)
    print("Thank you")

else:
    print("Will go Inside the else block when try block donot contain any Error Or try block runs sucessfully")

