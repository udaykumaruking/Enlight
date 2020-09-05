import random
numberOfGuesses = 0
number = random.randint(1,50)
name = input("Hello! What is your name?")
print(name + ", I am thinking of a whole number between 1 and 50. Can you guess what it is?")

while numberOfGuesses < 8:
    guess = int(input("Take a guess"))
    numberOfGuesses = numberOfGuesses + 1
    guessesLeft = 8 - numberOfGuesses

    if guessesLeft == 0:
            print("sorry, the number i was thinking is " + str(number) + ": )")
    elif guess < number:
        guessesLeft = str(guessesLeft)
        print("your guess is too low! You have " + guessesLeft + " guesses left")
    elif guess > number:
        guessesLeft = str(guessesLeft)
        print("your guess is too high! You have " + guessesLeft + " guesses left")
        
    elif guess == number:
        print("good Job! You guessed the number in " + str(numberOfGuesses) + " tries :)")
        break
    