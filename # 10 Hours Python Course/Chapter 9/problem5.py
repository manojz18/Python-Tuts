word = ["Hello", "Donkey", "boy"]

with open("donkey.txt", "r") as f:
    content = f.read()

for words in word:
    content = content.replace(words, "#" * len(words))

with open("donkey.txt", "w") as file:
    file.write(content)