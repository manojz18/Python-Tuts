# remove the specific part from the list and return the list

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["manoj", "mayank", "suraj"]

print(rem(l, 'j'))