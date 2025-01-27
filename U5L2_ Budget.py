def main():

    # Creates a number variable to keep track of the input expenses
    totalExpenses = 0

    # Gives the while loop a variable
    question = "yes"

    print("Hello!")
    budget = float(input("Enter the amount that you have budgeted for the month: "))

    # Creates a loop based on the user's answer of yes or no
    while question.lower() == "yes":
        expenses = float(input("Enter each expense's value one at a time: "))

        # Keeps track of the user's inputs, adding them together and keeping them in 
        # the same variable
        totalExpenses += expenses

        question = input("Would you like to enter more? (Enter yes or no) ")

    # If statement using the conditional that if the expenses are higher than the 
    # budget, or not higher, it will print the correct statment for the condition
    if totalExpenses >= budget:
        print("You are $", abs(budget - totalExpenses), "over your set budget.")
    else:
        print("You are $", abs(budget - totalExpenses), "under your set budget.")

main()