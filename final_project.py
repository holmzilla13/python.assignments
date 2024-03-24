# Steven Holmes
# COP 2500
# April 14, 2023
# Final Project

# Imports turtle and creates a turtle drawing of the words UCF.  This is printed as a form of welcome screen before the menu is accessed.
# It is designed to terminate itself as soon as the logo draws out.
import turtle
def UCF(posX,posY):

    posX = -100
    posY = 0

    turtle.penup()
    turtle.goto(posX,posY)
    turtle.color("#FFD700")
    turtle.pendown()
    turtle.right(90)
    turtle.forward(60)
    turtle.circle(50, 180)
    turtle.forward(60)

    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(25)
    turtle.circle(55,180)
    turtle.forward(25)

    turtle.penup()
    turtle.forward(40)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(45)
    turtle.right(180)
    turtle.forward(45)
    turtle.right(90)
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(65)
    turtle.penup()


    turtle.getscreen().bye()

# This establishes a list and a dictionary for storage of the course and materials for the program.
material_list = []
material_database = {}
# This block sets a menu in which the UCF function is called so that it runs prior to going into the options provided for the user to select.
def menu(materials_list, material_database):
    answer = UCF(posX=-100,posY=0)

    print("Welcome to UCF's Course Materials Database!")
    option = 0
    while option != 4:
        option = int(input("From the list below, which options best describes you?\n 1. Student\n 2. Instructor\n 3. Office Assistance\n 4. Exit\n"))
        main(option, material_database, materials_list,option)
    return option and answer

# This code calls the menu function in which accesses the first menu in which depending on what the user selects, they will be entered into a sub menu.
# The sub menu provides different options for the different people involved.  Students, instructors, or office assistants.  The instructors and officed assitants have 
# access to the same information and abilities to adjust it.  Students can only view the information.
def main(option, material_database, material_list, option_1):
    while option_1 !=4:
        if option == 1:
            print("Make sure you are prepared for your upcoming semester!\n")
            course_num = int(input("How many courses are you taking?\n"))
            for i in range(course_num):
                course_code = input("What is the course code of course number "+str(i+1)+" you are taking\n (ex. COP-2500)\n")
                if course_code not in material_database:
                    print("This course has yet to be added by an office assistant or your instructor.  Please check back later.\n")
                if course_code in material_database:
                    print("For " + course_code + " you will need "+ material_database[course_code] + " for the upcoming semester.")
            print("Goodbye and goodluck with your semester!")
            return option
        elif option == 2 or option ==3:
            option_1 = 0
            while option_1 != 4:
                print("Make sure your courses material list is up to date!\n")
                print("What would you like to do?\n")
                option_1 = int(input(" 1. Add Materials\n 2. Remove Materials\n 3. Review Materials\n 4. Exit\n"))
                if option_1 == 1:
                    course_code = input("What is the course code you adding? (ex. COP-2500)\n")
                    if course_code not in material_database:
                        material = input("What is the textbook title needed for this course?\n")
                        material_list.append([course_code,material])
                        material_database[course_code] = (material)
                    print("Material " + material + " added for course " + course_code + " successfully!")
                elif option_1 == 2:
                    course_code = input("What is the course code for the class you would like to remove? (ex. COP-2500)\n")
                    if course_code in material_database:
                        material_list.remove([course_code, material_database[course_code]])
                        del material_database[course_code]
                        print("Material removed for course " + course_code + " successfully!")
                    else:
                        print("This course is not in currently in the database.\n")
                elif option_1 == 3:
                    course_code = input("What is the course code for the materials you would like to review? (ex. COP-2500)\n")
                    if course_code in material_database:
                        print("Materials for course " + course_code, ":")
                        for course, material in material_list:
                            if course == course_code:
                                print(material)
                    else:
                        print("This course is not currently listed in the database.\n")
                elif option_1 ==4:
                    print("\n")       
    else:
        print("Have a great day!  Whether you are an instructor, office staff, or a student, have a wonderful semester!")
option = menu(material_list, material_database)
menu = main(option, option, material_database, material_list)
# Calls the main function and runs the entire program.
main()
