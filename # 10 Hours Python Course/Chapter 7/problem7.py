'''
        *
       ***
      *****

'''

n = int(input("Ente the number: "))

for i in range(0,n):
    print(" "*(n-i-1), end="")
    print("*"*(2*i+1), end="")
    print("")