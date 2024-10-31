a = "Manoj, Zagade"

print(a.upper())
print(a.lower())

print(a.rstrip("e"))

print(a.replace("Manoj", "Zagade"))

print(a.split(","))

print(a. capitalize())
print(len(a))
print(len(a.center(50))) #It will add more blank spaces to make the string in middle with total 50

print(a.endswith("!")) 
print(a.endswith("oj", 3, 5))

print(a.count("a"))

print(a.find("Z"))

b = "Manoj\n"

print(a.isalnum())
print(a.isalpha())

print(a.islower())


print(b.isprintable())

print(a.istitle()) # true only if first character is capital
print(a.isspace())

print(a.swapcase())

print(a.title())