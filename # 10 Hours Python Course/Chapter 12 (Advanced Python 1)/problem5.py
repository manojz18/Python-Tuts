n = int(input("Enter the table no. you want: "))

tables = [n*i for i in range(1, 11)]

with open("tables.txt", "a") as t:
    t.write(f" Table of {n}: {str(tables)} \n ")