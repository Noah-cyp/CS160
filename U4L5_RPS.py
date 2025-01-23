import random

def main():

    separation = ("*" * 55)
    options = ("rock", "paper", "scissors")

    computerWin = 0
    userWin = 0
    tie = 0

    print("\n" * 3)

    print(separation)
    print("Hello! Welcome to the Rock, Paper, Scissors Program!\n")
    print("You have unlimited plays, so go as long as you want!\n")
    print("Let's get started!")
    print(separation)

    while True:

        userInput = input("Please enter Rock, Paper, or Scissors: ").lower()

        if userInput.lower() == "quit":
            print("Thank's for playing!\n")
            quit()

        if userInput not in options:
            print("Error: answer is not a correct choice.")
            print("Goodbye.\n")
            quit()

        computer = random.choice(options)
        print("The computer chose: ", computer)
        print(separation)
            
        if userInput == "rock":
            if computer == "paper":
                print("You Lost :(\n")
                computerWin = computerWin + 1
                print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                      "Ties so Far: ", " ", tie)
                print(separation)
                print("~~~ Type 'quit' to exit the program ~~~")
                print(separation)

            if computer == "scissors":
                print("You Win!\n")
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
            tie = tie + 1
            print("Computer Wins: ", computerWin, " " * 3, "User Wins: ", userWin, "\n"
                  "Ties so Far: ", " ", tie)
            print(separation)
            print("~~~ Type 'quit' to exit the program ~~~")
            print(separation)
            


main()