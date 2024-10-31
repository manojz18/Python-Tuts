# wheter the poem file contains the word twinkle

with open("poem.txt") as p:

    content = p.read()

if("Twinkle" in content):
    print("Twinkle is in the poem File")
else:
    print("Twinkle is not in the poem File")