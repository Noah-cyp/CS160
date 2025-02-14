#******************************************************************************
# Author:                Noah Cyplik
# Lab:                   03
# Date:                  02/14/25
# Description:           This program takes the user's input of a specific 
#                        grocery item, the quantity, the cost, and then 
#                        calculates the total of all 
#                        data added. The program then takes a few more 
#                        user inputs to create more 
# personalization.
# Input:                 The user inputs a grocery item, the quantity and 
#                        price of the item, and a few personalization fuctions 
#                        such as, coupon 
#                        codes and payment with either card or cash.
# Output:                The outputs are the current date and time, all items 
#                        listed, their quantity and price, along with the total 
#                        of the item. Other outputs include formatting and 
#                        making the program visually appealing.
# Sources:               Assignment 3 specifications and a  little prior 
#                        knowledge of the python language.
#******************************************************************************

import os
import math
import datetime
import random
from random import randint

# Clears the terminal before running the program
os.system("clear")

# Allows for a determined number of integers to be randomized
def randomDigits(n):
    start = 10 ** (n-1)
    end = (10 ** n) -1
    return randint(start, end)

def main():

    items = []
    cost = []
    amount = []
    index = 0
    total = 0
    length = 0
    amountSum = 0
    question = "y"
    paymentVar = ["card", "cash"]
    cardType = ["Credit: ", "Debit: "]
    separation = "-" * 60
    lineSep = "=" * 60
    cardNum = ("*" * 4 + " ") * 3

    # Allows for the display of the current date and time
    today = datetime.datetime.now()
    currentTime = today.strftime("%H:%M:%S")

    print(lineSep)
    print("Welcome to the Christmas Island Supermarket!")
    print(separation)
    print("To start shopping, just enter the items you want to buy one\n"
          "by one, the quantity of the item, \n"
          "and how much per item.\n"
          "Get going!")
    print(lineSep)

    # Loop for entering item, quantity, cost, and keep going
    while question.lower() == "y":
        aItem = input("Enter an item: ")
        if aItem == "":
            print("Invalid Item")
            aItem = input("Enter an item: ")
        items.append(aItem)

        aCost = float(input("Enter the cost of one: "))
        if aCost < 0.01:
            print("Invalid number")
            aCost = float(input("Enter the cost of one: "))
        cost.append(aCost)

        aAmount = int(input("Enter the quantity: "))
        if aAmount < 1:
            print("Invalid amount")
            aAmount = int(input("Enter the quantity: "))
        amount.append(aAmount)
        amountSum += aAmount

        question = input("Add more items? Y/N: ")
        print("\n")

    print("\n" * 2)
    print(lineSep)
    print("{:^60}".format("Christmas Island Supermarket\n"))
    print("{:^60}".format("9 Gaze Rd, Christmas Island Shire of Christmas Island\n"))
    print("{:^60}".format("6798 Christmas Island\n"))
    print(lineSep)

    # Displays the current date
    print("{:^60}".format(today.strftime("%b, %d, %Y")))

    print(separation)
    print("Recipt:\n")
    print("{:<20}{:<15}{:<15}{:<15}\n".format("Item", "Cost", "Qty", "Total"))

    length = len(items)

    # Displays all of the added array information
    for index in range(length):
        print("{:<20}{:<15}{:<15}{:<15}".format(items[index], format(cost[index], '.2f'), amount[index], format((amount[index] * cost[index]), '.2f')))
        total += cost[index] * amount[index]
    print(separation)

    while True:
        payment = input("How will you be paying? Cash or Card? ")
        if payment.lower() in paymentVar:
            break
        else:
            print("Invalid payment; Try again")
    
    couponCode = input("Do you have a coupon code? ")
    if couponCode == "M11L10N2":
        total *= 1000000
        print(lineSep)
        print("Total: $ ", format(total, '.2f'))
        print("\n")
    elif couponCode == "PR0GR44M3R":
        total -= total
        print(lineSep)
        print("Total: $ ", format(total, '.2f'))
        print("\n")
    else:
        print(lineSep)
        print("Total: $ ", format(total, '.2f'))
        print("\n")

   
    print("\nPaid with:  \t", payment.capitalize())
    print("Cashier: \t Admin")

    # Creates a random transaction ID and random card number
    print("{:<17}{:<15}".format("Trans ID: ", randomDigits(15)))
    if payment.lower() == "card":
        print("{:<17}{:<15}{:<5}".format(random.choice(cardType), cardNum, randomDigits(4), sep = ""))

    print("\n")
    print("{:<17}{:<9}".format("Terminal # ", randomDigits(8)))
    print("*Signature Verified*\n")
    print(lineSep)
    print("{:>28}".format(today.strftime("%m-%d-%Y")), "  ", "{:<17}".format(currentTime))
    print("{:>35}{:^3}".format("# of items sold ", amountSum, sep = ""))
    print("\n")

    print("{:^60}".format("Thank You for Shopping"))
    print("{:>40}".format("Please Come Again!\n"))
    print(separation)

    print("{:^60}".format("Coupon Codes\n"))
    print("{:^60}".format("M11L10N2\n"))
    print("{:^60}".format("PR0GR44M3R\n"))
    print(lineSep)
    print("\n")

main()