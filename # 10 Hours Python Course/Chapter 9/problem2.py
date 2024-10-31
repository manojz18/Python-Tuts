import random

def game():
    score = random.randint(1, 62)

    with open("hiscore.txt") as f:
        hiscore = f.read()

        if(hiscore != ""):
            hiscore = int(hiscore)

        else:
            hiscore = 0

    print(f"your score is {score}")

    if(score > hiscore):
        with open("hiscore.txt", "w") as content:
            content.write(str(score))

    return score

game()