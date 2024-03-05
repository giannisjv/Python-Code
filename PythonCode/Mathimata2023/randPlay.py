import random

numberOfGuesses = 15
found = False
level = 0 

while (numberOfGuesses != -1):
    level += 1 
    print("\tLets Play a game!")
    print("\tI will chose a Number between 1 and 100\n\tand you will try to find it.")

    print("\n")








































    randNum = random.randint(1, 100)
    counter = 0
    guess = 0


    while (counter > numberOfGuesses or guess != randNum or found == False):
        
        guess = int(input("\tGuess the number i Randomly choose!!!"))
        counter += 1
        if(guess < randNum):
            print("\tThe number you have choose is lesser. Try again!!!")
            print("\tThis was attemt no " ,counter)
            print("\tRemaining guesses ", numberOfGuesses - counter)
        elif (guess > randNum):
            print("\tThe number you have choose is greater. Try again!!!")
            print("\tThis was attemt no " ,counter)
            print("\tRemaining guesses ", numberOfGuesses - counter)
        elif(guess == randNum):
            print("\tCongrats You found it with ", counter , "out of ", numberOfGuesses)
            found == True 
        print("\n")




















    if(found == True):
        numberOfGuesses -= 2
    elif(found == False):
        print("\tYou reached level ", level)
        print("\tThe random number was " ,randNum)


