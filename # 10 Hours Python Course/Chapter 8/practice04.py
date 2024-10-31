# using recursion calc sum of n

def calcSum(n):
    # Base Case
    if(n == 1):
        return 1
    return n + calcSum(n-1)


print(f"{calcSum(5)}")