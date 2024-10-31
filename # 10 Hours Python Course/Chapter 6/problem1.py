a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
c = int(input("Enter the number 3: "))
d = int(input("Enter the number 4: "))

if(a > b and a > c and a > d):
    print("a is the greatest number")

if(b > a and b > c and b > d):
    print("b is the greatest number")

if(c > b and c > a and c > d):
    print("c is the greatest number")

if(d > b and d > c and d > a):
    print("d is the greatest number")