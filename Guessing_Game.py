import random

secretNumber = random.randint(1,100)
attempts = 0
print("Press enter to begin")
input('')
print("I'm thinking of a number between 1 and 100.")

validGuess=0

while True :#validGuess != secretNumber:
    guess=input('Take a guess: ')
    attempts += 1
       
    if guess.isdigit():
        validGuess= int(guess)
    else:
        print("Plese enter a valid number. ")
        continue

    if validGuess > 100 :
        print("Out of range (1-100)")
    elif validGuess < 1 :
        print("Out of range (1-100)")
    else :

        if validGuess < secretNumber :
            print("Too low!")
        elif validGuess > secretNumber :
            print("Too high")
        else :
            print(f"Correct! You guessed it in {attempts} tries." )
            # The above code is the same as 'print("Correct! You guessed it in %d tries." %attempts )'
            # It makes use of the 'f-string' 
            break
if attempts <5  :
    print("Amazing!!")
elif attempts >5 <=10 :
    print("Well done.")
else:
    print("Better luck next time")

