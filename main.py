import random
# It is a module, that will pick a random choice

def game():

    choices = ["Snake","Water","Gun"]
    # all available choices in a list

    computer = random.choice(choices)
    # is a function from the "Random" module of pyhton.

    player = input ("Choose: Water, Snake or Gun: (Dont capitalize) ").capitalize()
    # It will capitalize the first letter of inputted value

    print (f"Computer chose: {computer}")
    # It will print the choice of computer

    if player not in choices:
        print ("Invalid Choice.")
        return
    
    if player == computer:
        print ("Its a Draw!")
    elif (player == "Snake" and computer == "Water") or (player == "Water" and computer == "Gun") or (player == "Gun" and computer == "Snake"):
        print ("You Win!")
    else:
        print ("You lose!")


game()
# It will launch function: game.