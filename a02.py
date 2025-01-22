#******************************************************************************
# Author:                Noah Cyplik
# Lab:                   02
# Date:                  01/17/25
# Description:           This program prompts users for the average hours
#                        worked per week, as well as average wage. 
#                        The program then does simple calculations based on an 
#                        average wage of $21.00/ hr at 40 hours
#                        a week. It then shows the gross paycheck, how much is
#                        getting taken out and where, and the
#                        take-home pay. The program then says goodbye, and ends.
# Input:                 The user only inputs their average time worked per
#                        week,  and their average hourly wage.
# Output:                The outputs are the gross income, all basic taxes 
#                        taken out and how much, and the user's take-home pay.
# Sources:               Assignment 1 specifications and a  little prior 
#                        knowledge of the python language.
#******************************************************************************




def main():

    # Creates the separation lines to make text easier to read, as well as look
    # visually pleasing
    separation = ("-" * 55)

    # Prints 5 spaces above execution to separate function from terminal code
    print(" \n" * 5)

    print(separation)
    print("Hello! Welcome to your personal Income Tax Calculator.")
    print(separation)
    print("\n")

    # Gives explanation to the calculator and how it works
    print("This calculator takes an input hourly wage and \n"
          "the average hours worked per week, and automatically \n"
          "calculates the take-home paycheck with the inputs. \n")
    print("This calculator only calculates taxed income in \n"
          "the state of Oregon. All calculations are based on \n"
          "an average wage of $21.00 an hour at 40 hours a week. \n")
    print(separation)

    print("Please have your base hourly pay \n"
          "(including average tips if applicable), and \n"
          "average hours worked in one week.")
    print(separation)

    print(separation)

    # Asks for the user's hours per week as an integer
    userTime = float(input("On average, how many hours do you work per week? \n"
                          "Please answer in whole numbers: "))
    
    if not(userTime > 6):
      print("Please enter a realistic number next time.\n"
            "Try again, thank you.")
      exit()
    
    # Converts the user time to an integer just in case user entered a float
    integerTime = int(userTime)

    print(separation)

    # Asks the user's hourly wage as a float except tipped pay
    userWage = float(input("What is your hourly base pay? \n"
                           "Please include average tips (if applicable) \n"
                           "in hourly pay: "))
        
    print(separation)

    print(separation) 
    # -------------------------------------------------------

    # All veriables for tax rates converted to decimal values
    fedRate = 0.0708
    stateRate = 0.0679
    socialRate = 0.0620
    medRate = 0.0145
    compRate = 0.0476

    # Calculations for the hours per pay period and the gross income for 
    # that period
    userHours = round(integerTime * 2)
    grossPay = round(userHours * userWage, 2)

    # General tax calculations
    incomeFed = round(grossPay * fedRate, 2)
    incomeState = round(grossPay * stateRate, 2)

    # FICA tax calculations
    incomeSocial = float(round(grossPay * socialRate, 2))
    incomeMed = round(grossPay * medRate, 2)
    incomeComp = round(grossPay * compRate, 2)

    # Take home salary calculations
    mainTax = incomeFed + incomeState
    fica = incomeSocial + incomeMed + incomeComp
    allTax = mainTax + fica
    takeHome = grossPay - allTax
    
    # -------------------------------------------------------
    # All displayed outputs for the user
    print('\n' * 4)

    # Many if elif else statements are used in all of the displayed outputs
    # This is to counteract any joke answers so that the spacing stays the same
    # This allows for an input as low as 1 hour a week and 0.01 per hour
    if grossPay >= 1000.00: 
      print("Gross Paycheck", " " * 29, "$ ", format(grossPay, '.2f'))
    elif grossPay >= 100.00:
      print("Gross Paycheck", " " * 30, "$ ", format(grossPay, '.2f'))
    elif grossPay >= 10.00:
      print("Gross Paycheck", " " * 31, "$ ", format(grossPay, '.2f'))
    else:
      print("Gross Paycheck", " " * 32, "$ ", format(grossPay, '.2f'))

    print(separation)

    if incomeFed >= 100.00:
      print("Federal Income", " " * 30, "$ ", format(incomeFed, '.2f'))
    elif incomeFed >= 10.00:
      print("Federal Income", " " * 31, "$ ", format(incomeFed, '.2f'))
    else:
      print("Federal Income", " " * 32, "$ ", format(incomeFed, '.2f'))

    if incomeState >= 100.00:
      print("State Income", " " * 32, "$ ", format(incomeState, '.2f'), "\n")
    elif incomeState >= 10.00:
      print("State Income", " " * 33, "$ ", format(incomeState, '.2f'), "\n")
    else:
      print("State Income", " " * 34, "$ ", format(incomeState, '.2f'), "\n")

    print(separation)

    if fica >= 100.00:
      print("FICA Taxes", " " * 34, "$ ", format(fica, '.2f'))
    elif fica >= 10.00:
      print("FICA Taxes", " " * 35, "$ ", format(fica, '.2f'))
    else:
      print("FICA Taxes", " " * 36, "$ ", format(fica, '.2f'))

    # Prints a down arrow to indicate to the user that the next prints are 
    # coming from the top print
    print(" " * 3, "|")
    print(" " * 3, "|")
    print(" " * 3, "V")

    if incomeSocial >= 100.00:
      print("Social Security", " " * 29, "$ ", format(incomeSocial, '.2f'))
    elif incomeSocial >= 10.00:
      print("Social Security", " " * 30, "$ ", format(incomeSocial, '.2f'))
    else:
      print("Social Security", " " * 31, "$ ", format(incomeSocial, '.2f'))

    if incomeMed >= 10.00:
      print("Medicare", " " * 37, "$ ", format(incomeMed, '.2f'))
    else:
      print("Medicare", " " * 38, "$ ", format(incomeMed, '.2f'))

    if incomeComp >= 10.00:
      print("State Workers Compensation", " " * 19, "$ ", format(incomeComp, '.2f'), "\n")
    else:
      print("State Workers Compensation", " " * 20, "$ ", format(incomeComp, '.2f'), "\n")

    print(separation)

    if takeHome >= 1000.00:
      print("Take Home Salary", " " * 27, "$ ", format(takeHome, '.2f'), "\n")
    elif takeHome >= 100.00:
      print("Take Home Salary", " " * 28, "$ ", format(takeHome, '.2f'), "\n")
    elif takeHome >= 10.00:
      print("Take Home Salary", " " * 29, "$ ", format(takeHome, '.2f'), "\n")
    else:
      print("Take Home Salary", " " * 30, "$ ", format(takeHome, '.2f'), "\n")

    print(separation)

    # ------------------------------------------------------------------
    # Thanking the user, then ending the program

    print("Thank you for using the Income Tax Calculator.\n"
          "Goodbye.")
    print('\n' * 2)

main()