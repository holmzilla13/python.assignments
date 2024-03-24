# Steven Holmes
# COP 2500
# April 9, 2023
# Airport Database

# Sets a dictionary named "airport_database"
airport_database = {}

# Defines a menu function.  This function is designed to interact with the main function in which the user will be presented a menu offering 5 options for what they would like to do.
# The menu will keep presenting itself to the user, until the user enters "5", promptint to Exit the loop
def menu(airport_list):
    print("Welcome to OIA!")
    option = 0
    while option != 5:
        option = int(input("What would you like to do?\n 1. Add airport\n 2. Remove airport\n 3. Access\n 4. List airports\n 5. Exit\n"))
        main(option, airport_list)
    return option

# This function does a variety of tasks.  For options 1-3 accesses the database when an airport is entered by the user.  It'll let the user know if it is already contained in the database, or if
# it is not there and can be added, or can't be deleted.  This function allows the user to add, remove items into the database, and also allows the database information to be viewed and printed.
def main(option, airport_list):
    while option != 5:
        if option == 1:
            airport_code = input("What is the airport's code?\n")
            if airport_code in airport_database:
                print("This airport is already in the database.\n")
            else:    
                airport_name = input("What is the airport's name?\n")
                distance = input("What is the distance of the airport from Orlando?\n")
                airport_list.append([airport_code,airport_name,distance])
                airport_database[airport_code] = (airport_name,distance)
        if option == 2:
            airport_code = input("What is the airport's code?\n")
            if airport_code in airport_database:
                airport_name, distance = airport_database[airport_code]
                airport_list.remove([airport_code,airport_name,distance])
                del airport_database[airport_code]
            else:
                print("This airport is not in the database.\n")
        if option == 3:
            code = input("What is the airport code you would like to access?\n")
            if code in airport_database:
                airport_name, distance = airport_database[code]
                print({airport_name, code})
            else:
                print("The airport is not in the database.")
        if option == 4:
             print(airport_list)
        option = menu(airport_list)
    if option == 5:
        print("Goodbye")
# Creates a list to store name and distance.
airport_list = []
option = menu(airport_list)
# Calls main function
main()

    