# Using Walrus Operator

if(n := len([1, 5, 2, 3, 4])) >= 3:
    print(f"Expected Length is <= 3 but Length is {n}")
else:
    print("Length is <=3")