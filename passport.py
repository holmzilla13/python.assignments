# Steven Holmes
# COP 2500
# Passport
# March 3, 2023

import turtle


#defines a function of the stamp created for the previous assignment.
def steven_holmes_stamp(posX,posY):
    turtle.pensize(3)
    turtle.speed(0)
    angle = 91
    turtle.penup()
    turtle.goto(posX,posY)
    turtle.pendown()
    turtle.penup()
    turtle.color("black","#F4F0ED")
    turtle.right(270)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(75)
    turtle.end_fill()
#This is the start for the drawing done in a loop.  The loop cycles through a rotation of colors in each iteration.
    turtle.penup()
    turtle.left(90)
    turtle.forward(75)
    turtle.pendown()
    for i in range(0,38,6):
            for color in ["#ab2222","black","#1021a3","silver","#FFD700","yellow","silver","#247508"]:
                turtle.color(color)
                turtle.circle(i)
                turtle.left(angle)
    turtle.left(123)
    turtle.penup()    
#Connor Tierce's code from TTH 12-115
def connor_tierce(posX,posY):
    my_turtle = turtle.Turtle()
    
    my_turtle.penup()
    my_turtle.goto(posX,posY)
    my_turtle.pendown()
    my_turtle.pencolor("black")
    my_turtle.forward(150)
    my_turtle.left(90)
    my_turtle.forward(90)
    my_turtle.left(90)
    my_turtle.forward(150)
    my_turtle.left(90)
    my_turtle.forward(90)



    my_turtle.penup()
    my_turtle.goto(posX+15, posY+75)
    my_turtle.pendown()



    #This is supposed to be a star that represents outer space.
    my_turtle.pencolor("blue")
    my_turtle.left(180)
    i = 1
    while i<6:
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.goto(posX+15, posY+75)
        my_turtle.pendown()
        my_turtle.left(72)
        i = i + 1



    my_turtle.left(180)
    my_turtle.penup()
    my_turtle.goto(posX+110, posY+80)
    my_turtle.pendown()



    #This is the U-C-F for the school.
    my_turtle.pencolor("gold")
    my_turtle.forward(10)
    my_turtle.left(90)
    my_turtle.forward(5)
    my_turtle.left(90)
    my_turtle.forward(10)
    my_turtle.left(90)
    my_turtle.penup()
    my_turtle.goto(posX+125, posY+80)
    my_turtle.pendown()
    my_turtle.forward(5)
    my_turtle.left(90)
    my_turtle.forward(10)
    my_turtle.left(90)
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.goto(posX+130, posY+80)
    my_turtle.pendown()
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.goto(posX+130, posY+80)
    my_turtle.pendown()
    my_turtle.left(90)
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.goto(posX+130, posY+75)
    my_turtle.pendown()
    my_turtle.forward(5)



    my_turtle.left(180)
    my_turtle.penup()
    my_turtle.goto(posX+25, posY+50)
    my_turtle.pendown()



    #This is my name where most countries might have the country name.
    my_turtle.pencolor("red")
    #C
    my_turtle.forward(10)
    my_turtle.left(90)
    my_turtle.forward(20)
    my_turtle.left(90)
    my_turtle.forward(10)
    #O
    my_turtle.penup()
    my_turtle.goto(posX+35, posY+50)
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.right(90)
    my_turtle.forward(20)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.right(90)
    my_turtle.forward(20)
    #N
    my_turtle.penup()
    my_turtle.goto(posX+55, posY+30)
    my_turtle.pendown()
    my_turtle.forward(20)
    my_turtle.right(150)
    my_turtle.forward(22.36)
    my_turtle.left(150)
    my_turtle.forward(20)
    #N
    my_turtle.penup()
    my_turtle.goto(posX+75, posY+30)
    my_turtle.pendown()
    my_turtle.forward(20)
    my_turtle.right(150)
    my_turtle.forward(22.36)
    my_turtle.left(150)
    my_turtle.forward(20)
    my_turtle.left(90)
    #O
    my_turtle.penup()
    my_turtle.goto(posX+105, posY+30)
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.right(90)
    my_turtle.forward(20)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.right(90)
    my_turtle.forward(20)
    #R
    my_turtle.penup()
    my_turtle.goto(posX+115, posY+30)
    my_turtle.pendown()
    my_turtle.right(180)
    my_turtle.forward(20)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.goto(posX+125, posY+40)
    my_turtle.pendown()
    my_turtle.left(115)
    my_turtle.forward(12.2)



    my_turtle.penup()
    my_turtle.goto(posX, posY)
    my_turtle.pendown()
#Whitney Nguyen's code from TTH 12-115
def whitney_nguyen_stamp(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pencolor("#da251d")
    turtle.fillcolor("#da251d")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(150)
        turtle.left(90)
    turtle.end_fill()
    # First half of a Pill
    turtle.penup()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor("#3c3b6e")
    turtle.begin_fill()
    turtle.circle(-12.5,-180)
    turtle.left(180)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.end_fill()
    # Second half of a Pill
    turtle.penup()
    turtle.left(180)
    turtle.pencolor("black")
    turtle.fillcolor("#7dabe8")
    turtle.forward(15)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(15)
    turtle.circle(-12.5,180)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()
    # Amber Vial
    turtle.penup()
    turtle.pencolor("black")
    turtle.fillcolor("#fa9500")
    turtle.left(90)
    turtle.forward(27)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    for y in range(2):
        turtle.forward(95)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    # Lid of prescription vial
    turtle.penup()
    turtle.forward(95)
    turtle.pendown()
    turtle.fillcolor("White")
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    # Label on prescription vial
    turtle.penup()
    turtle.left(180)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(30)
    turtle.end_fill()
    turtle.hideturtle()


#Defined a function named "Main" that combines the separate pieces of code
def Main():
    steven_holmes_stamp(50,0)
    steven_holmes_stamp(250,20)
    #Connor Tierce's code from TTH 12-115
    connor_tierce(250,-200)
    connor_tierce(-400,200)
    #Whitney Nguyen's code from TTH 12-115
    whitney_nguyen_stamp(-300,-200)
    whitney_nguyen_stamp(0, 200)
     
     
#Calls the main function
Main()
turtle.getscreen()._root.mainloop()