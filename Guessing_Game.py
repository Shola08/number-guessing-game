from pickle import NONE
import random
print('Can you guess correctly in 10 attempts or less?')
while True :
    won = False

    secretNumber = random.randint(1,100)
    attempts = 0
    print("Press enter to begin.")
    input('')
    print("Good luck.")
    print("I'm thinking of a number between 1 and 100.")

    validGuess= NONE

    while True :#validGuess != secretNumber:
        if attempts >= 10 :
            print ("Oops, you have used up all your attempts.")
            print(f"The number was {secretNumber}.")
            print("Better luck next time. \n")
            break
        guess=input('Take a guess: ')
        # attempts += 1, was here at first
   
        if guess.isdigit():
            validGuess= int(guess)
            # attempts += 1, then was later here
        else:
            print("Plese enter a valid number. \n")
            continue

        if not 1 <= validGuess <= 100 :
            print("Out of range (1-100) \n")
            continue
        attempts += 1       

        if abs(secretNumber - validGuess) <= 5 and validGuess != secretNumber :
            print("Ooo, you're close!")

        if validGuess < secretNumber :
            print(f"Too low!  ({10 - attempts} left). \n")
        elif validGuess > secretNumber :
            print(f"Too high   ({10 - attempts} left). \n")
        else :
            print(f"Correct! You guessed it in {attempts} tries." )
            # The above code is the same as 'print("Correct! You guessed it in %d tries." %attempts )'
            # It makes use of the 'f-string' 
            won = True
            break
    if won :
        if attempts <=5  :
            print("Amazing!!")
        elif attempts >5 and attempts <10 :
            print("Well done.")
        if attempts == 10 :
            print("Way to make your last shot count.")
        print('\n')

    playAgain =''

    while playAgain not in ['y', 'n', 'yes', 'no'] : # Means while the value for playAgain is not a value in the list
        playAgain = input('Would you like to play again? Enter (y) for yes or (n) for no. \n').lower()
        if playAgain not in ['y', 'n', 'yes', 'no']:
            print("Please enter a valid response \n")

    if playAgain in ['n', 'no'] :
        print('See you next time!')
        break
    else :
        print("Wonderful! \n")
        continue
        
        
