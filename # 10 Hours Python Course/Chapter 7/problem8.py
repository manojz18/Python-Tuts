'''

*
**
***

'''


n = int(input("Ente the number: "))

for i in range(0,n):
    print("*"*(i+1), end="")
    print(" "*(n-i-1), end="")
    print("")