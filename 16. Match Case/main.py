
# like switch case statement
# No need of break statement in python
a = int(input("Enter your age: "))

match a:

    case 15: print("you can't vote")

    case 18: print("you can vote")

    case _ if(a <= 18  and a >= 0):
        print ("You are child")