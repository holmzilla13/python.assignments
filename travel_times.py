# Steven Holmes
# COP 2500
# Travel Times
# February 4, 2023

print("Welcome to the travel planner!")
num_places = int(input("How many places are we visiting today?\n"))

print("Answer each of the following questions referencing the time in minutes.")

visit = int(input("How long do you have to visit today?\n"))

location = int(1)
sum = 0

for number in range(num_places):
    minutes = int(input("How long does it take to travel to location #"+str(location)+"?\n"))
    minutes_1 = int(input("How long would you like to stay in location #"+str(location)+"?\n"))
    location = location +1
    current_total = int(minutes_1+minutes)
    sum = sum + current_total

time = visit-sum

if time < visit and time >=0:
    print("This trip would take",sum,"minutes.")
    print("You are able to take this trip!")
if time < visit and time <0:
    print("This trip would take",sum,"minutes.")
    print("You are not able to take this trip in time.")

