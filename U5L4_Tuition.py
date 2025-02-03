def main():

    separation = "~" * 50
    # Starting year price
    year = 16000

    perc = 0
    date = 0

    print("\n" * 2)
    print("Starting Year Price: $ ", year)
    print("-" * 4)

    # For loop that loops 5 times
    for i in range(5):
        # Adds the value to the variable and then stores it back 
        # into the same variable
        date += 1
        perc += 0.03

        print("Year: ", date)
        print("Percent Increase: ", perc)

        # Finds the tuition increase
        tuitionInc = year * perc

        print(separation)

        # Finds the increased year's tuition
        yearInc = year + tuitionInc
        print("The total tuition for year", date, "is: $ ", yearInc)
        print("-" * 4)

        # Finds the price for each new semester
        sem = yearInc / 2
        print("The semester tuition for year", date, "is: $", sem)
        print("-" * 4)

        print("The increased tuition for year", date, "is: $ ", tuitionInc)
        print(separation)

        print(" ")

main()