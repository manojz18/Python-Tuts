# a = [["Manoj",100], 1, 5, 8, 0, 3]

# print(a[0])


################### Dictionary ###################

# Dictionary is Mutable is Indexed, it contain key value pair and remember key cannot duplicate 

# d = {} #Empty Dictionary
# print(type(d))

# dictionary = {"Manoj" : 100, "Aditya" : 80, "Parth" : 81}
# print(dictionary)
# print(dictionary["Manoj"])
# print(dictionary.items())
# print(dictionary.values())
# dictionary.update({"Manoj" : 99, "Aadesh" : 85})
# print(dictionary)

# print(dictionary.get("MJ")) #This line give None
# print(dictionary["MJ"]) #This line give Error

# print(dictionary.clear())

keys = [1, 2, 3, 4]
new_dict = dict.fromkeys(keys, 10)

# print(new_dict)
# print(keys)

# print(1 in new_dict)

# Retriving keys and values from new_dict

# print(new_dict.keys())
# print(new_dict.values())
# print(new_dict.items())

# print(len(new_dict))

# copyingdict = new_dict.copy()
# print(copyingdict)

# print(new_dict.pop(1, 10))
# print(new_dict)
# print(new_dict.popitem())