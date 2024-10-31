#  prime number or not

n = int (input("Enter the number: "))

for i in range(2, n):
    if((n%i) == 0):
        print("Not prime Number")
        break
else:
    print("Is prime Number")

    