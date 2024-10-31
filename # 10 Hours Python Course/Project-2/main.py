from random import randint

n = randint(1, 100)

guesses = 1

a = -1

while(a != n):
    a = int(input("Guess the Number: "))
    if(a > n):
        print("Lower Number Please")
        guesses += 1

    elif (a < n):
        print("Higher Number Please")
        guesses += 1


print(f"You Have guessed the number {n} in {guesses} attempt.")