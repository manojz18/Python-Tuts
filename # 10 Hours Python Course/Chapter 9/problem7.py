

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Python in line num: {lineno}")
        break
    lineno += 1

else:
    print(f"Python not in lines")