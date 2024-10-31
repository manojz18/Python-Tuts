s = set()

s.add(20)
s.add(20.0)
s.add("20")

print(s) #Here it prints only 20, '20'
print(len(s)) # length is 2
# Because python treats 20 and 20.0 as Same