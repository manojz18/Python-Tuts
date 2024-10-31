n = int(input("Ente the number: "))
product = 1
for i in range(1, n+1):
    product *= i 

print(f"The Factorial of {n} is {product}")