'''
***
* *
***

'''

n = int(input("Ente the number: "))

for i in range(0,n):
    if (i == 0 or i == n-1):
        print("*"*(n), end="")
        
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print(" ")