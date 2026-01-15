import random #importing module
playing = True #initialise
number = str(random.randint(10,20)) #random in built function

print("I will generate a number from 10 to 20 and you have to guess it one digit at a time.")
print("The game end when you guess the number correctly!")
#iteriate loop until condition is met
while playing:
    guess = input("Give me your best guess: ")
    if number == guess:
        print("You win the game!")
        print("The number was", number)
        break

    else:
        print("Your guess was not quite right, try again.")
