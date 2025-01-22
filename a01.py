def main():

    # Creates a line separation with the "~" character
    separation = ("~" * 55)

    # All measurement variables
    foot = int(12)
    yard = int(foot * 3)
    mile = int(foot * 440)

    # Prints separating spaces from lines in the console
    print("\n" * 5)

    # Welcome message
    print(separation)
    print("Hello, welcome to the Inches Conversion Calculator. \n"
          "This calculator converts inches to feet, yards, and \n"
          "miles. Just type as many inches you want to convert \n"
          "and the calculator does all the work.")
    
    print(separation)
    print(separation)

    print("Please only use whole numbers when entering inches.\n"
          "If decimals are used, the number will be rounded.")
    
    print(separation)

    # Asking user the number of inches they want to input
    userInput = float(input("How many inches would you like to convert? "))

    print(separation)

    # Converts the user input to an integer
    userLength = int(userInput)

    # All conversion calculations
    userFoot = round(userLength / foot, 2)
    userYard = round(userLength / yard, 2)
    userMile = round(userLength / mile, 2)

    # Printing all calculations, all formatted to 2 decimal places
    print("You have: \n")
    print("Inches", " ", "-" * 4, " ", format(userLength, '.2f'))
    print("Feet ", " " * 2, "-" * 4, " ", format(userFoot, '.2f'))
    print("Yards ", " ", "-" * 4, " ", format(userYard, '.2f'))

    # If Else statment used in case the "userMile" variable would only 
    # display 0.00, instead displaying "Near Zero"
    if userMile <= 0.00:
        print("Miles ", " ", "-" * 4, " ", "Near Zero")
    else:
        print("Miles ", " ", "-" * 4, " ", format(userMile, '.2f'))

    print(separation)

    # Ending message
    print("Thank you for using the conversion calculator.",
          "Goodbye.")
    print(separation)

    print("\n")

main()