# Allows python to import the random module, letting us 
# use the random.() feature
import random

def main():

    # Creates a line of the '*' characters 55 times
    separation = ("*" * 55)
    # Creates a list of words that the program and user will be bound to
    options = ("rock", "paper", "scissors")

    # Creates values to keep track of how many wins for either person 
    # or computer and the number of ties
    computerWin = 0
    userWin = 0
    tie = 0

    # Creates 3 blank new lines
    print("\n" * 3)

    # Welcome message
    print(separation)
    print("Hello! Welcome to the Rock, Paper, Scissors Program!\n")
    print("You have unlimited plays, so go as long as you want!\n")
    print("Let's get started!")
    print(separation)

    # A loop that allows the game to infinetely continue until the user
    # breaks the loop
    while True:

        # Input asking for the user's choice, ignoring any capital letters
        userInput = input("Please enter Rock, Paper, or Scissors: ").lower()

        # If statement checking if the user types "quit", and if so,
        # the loop breaks and the program ends
        if userInput.lower() == "quit":
            print("Thank's for playing!\n")
            quit()

        # If statement checking if the user's input comes from the 
        # "options" list, and if not, the loop breaks and the program ends
        if userInput not in options:
            print("Error: answer is not a correct choice.")
            print("Goodbye.\n")
            quit()

        # Allows the program to randomly choose from the list in 
        # the "options" variable
        computer = random.choice(options)
        print("The computer chose: ", computer)
        print(separation)

        # ------------------------------------------------
        # All non-nested if statements are same, just checks for different
        # strings (except the bottom statement where it checks if the user
        # and computer used the same string; ie tie)
        # ------------------------------------------------
        # All nested if statements do practically the same thing, they just
        # check for different strings
        # ------------------------------------------------
        # The "computerWin" and "userWin" varibles get a value of 1 added 
        # to them depending on which if statement was used
        #
        # This keeps track of all the user wins, computer wins, and ties 
        # throughout the entire game
            
        # If statements nested into eachother to check for the user's
        # input, then the 2 computer possibilities
        if userInput == "rock":
            if computer == "paper":
                print("You Lost :(\n")

                # Adds a value of 1 to the variable "computerWin"
                computerWin = computerWin + 1

                # Displays all computer wins, user wins, and ties 
                # after each round
                print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                      "Ties so Far: ", " ", tie)
                print(separation)
                print("~~~ Type 'quit' to exit the program ~~~")
                print(separation)

            if computer == "scissors":
                print("You Win!\n")

                # Adds a value of 1 to the variable "userWin"
                userWin = userWin + 1
                print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                      "Ties so Far: ", " ", tie)
                print(separation)
                print("~~~ Type 'quit' to exit the program ~~~")
                print(separation)

        if userInput == "paper":
            if computer == "scissors":
                print("You Lost :(\n")
                computerWin = computerWin + 1
                print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                      "Ties so Far: ", " ", tie)
                print(separation)
                print("~~~ Type 'quit' to exit the program ~~~")
                print(separation)
                
            if computer == "rock":
                print("You Win!\n")
                userWin = userWin + 1
                print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                      "Ties so Far: ", " ", tie)
                print(separation)
                print("~~~ Type 'quit' to exit the program ~~~")
                print(separation)

        if userInput == "scissors":
            if computer == "rock":
                print("You Lost :(\n")
                computerWin = computerWin + 1
                print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                      "Ties so Far: ", " ", tie)
                print(separation)
                print("~~~ Type 'quit' to exit the program ~~~")
                print(separation)

            if computer == "paper":
                print("You Win!\n")
                userWin = userWin + 1
                print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                      "Ties so Far: ", " ", tie)
                print(separation)
                print("~~~ Type 'quit' to exit the program ~~~")
                print(separation)

        if userInput == computer:
            print("It's a Tie!\n")

            # Adds a value of 1 to the variable "tie"
            tie = tie + 1
            print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                  "Ties so Far: ", " ", tie)
            print(separation)
            print("~~~ Type 'quit' to exit the program ~~~")
            print(separation)
            


main()