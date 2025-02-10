def main():

    hobbies = []
    ahobby = ""
    index = 0
    separation = "~" * 45

    print(separation)
    print("Hello!")
    print(separation)

    ahobby = input("Enter a hobby or your favorite activity: ")

    while ahobby != "":
        hobbies.append(ahobby)
        ahobby = input("Enter a hobby or your favorite activity: ")

    print(separation)

    print("Your favorite hobbies/ activities are: \n")

    while index < len(hobbies) - 1:
        print(hobbies[index], ", ", sep = "", end = "")
        index += 1
    else:
        print("and ", hobbies[index], ".", sep = "")

    print(separation)

main()