from random import shuffle

userinput = 0
while (userinput > 50 or userinput < 5):
    userinput = int(input("Please enter the size of deck: "))
    if (userinput > 50 or userinput < 5):
        print("Sorry, but the number you've entered is invalid. Please enter again")
    else:
        print("Your deck is of size " + str(userinput))


deck = list(range(userinput))
shuffle(deck)
for x in deck:
    print(x)

currentscore = 0
currentcard = deck.pop(0)
print("Current Score: 0" )

while (deck):
    decision = -1


    while(decision > 1 or decision < 0):
        print("The current card value is: " + str(currentcard))
        decision = input("Do you think the next card will be higher or lower? Pleas enter 1 for HIGHER and 0 for LOWER: ")
        decision = int(decision)
        if (decision > 1 or decision < 0):
            print("Sorry, that is an invalid option. Please enter 1 for HIGHER or 0 for LOWER")
        else:
            print("You've decided the next card will be" + ("HIGHER" if decision == 1 else "LOWER"))

    nextcard = deck.pop(0)
    if (nextcard > currentcard):
        if (decision == 1):
            print("You are correct, the card value is " + str(nextcard) + "which is indeed higher than " + str(currentcard))
            currentscore = int(currentscore) + 1
            print("Your current score is: " + str(currentscore))
        else:
            print("You are incorrect, please try again with the next card")
            currentscore = int(currentscore) - 1
            print("Your current score is: " + str(currentscore))
    else:
        if (decision == 0):
            print("You are correct, the card value is " + str(nextcard) + "which is indeed lower than " + str(currentcard))
            currentscore = int(currentscore) + 1
            print("Your current score is: " + str(currentscore))
        else:
            print("You are incorrect, please try again with the next card.")
            currentscore = int(currentscore) - 1
            print("Your current score is: " + str(currentscore))

    currentcard = nextcard

print("Your final score is: " + str(currentscore))
