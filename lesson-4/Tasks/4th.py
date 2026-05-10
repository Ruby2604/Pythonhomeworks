# Number Guessing Game**
#Create a simple number guessing game.
#- The computer randomly selects a number between 1 and 100. 
#- If the guess is high, print "Too high!". 
#- If the guess is low, print "Too low!". 
#- If they guess correctly, print "You guessed it right!" and exit the loop.
#- The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, 
# print "You lost. Want to play again? ".
#- If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.



import random
random_number = random.randint(1, 100)
attempts = 10
while True:
    for i in range(attempts):
        number = int(input(f"{i + 1} - attempt. Guess the number: "))

        if number == random_number:
            print("You guessed it right!")
            break
        if number > random_number:
            print("Too high!")
        else:
            print("Too low!")
    else:
        a = input("You lost. Want to play again? ")
        if a in ['Y', 'YES', 'y', 'yes', 'ok']:
            continue
        else:
            break