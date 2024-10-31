
# e = set() #Empty set
# print(type(e))

# # Set dont have repeated values
# s = {1, 2, 3, 10}
# print(s)

# print(type(s))
# print(s)
# The output is unordered bcoz sets are unordered
# sets are not indexed
# we cannot change items in sets 

s1 = {1, 2, 5, 10, 8}
s2 = {2, 9, 7, 10, 4}
print(s1)
print(s2)

print(s1.union(s2))
print(s1.intersection(s2))

print(s1-s2)