#Steven Holmes
#COP 2500
#March 23, 2023
#Airport Names

# Created a function that will search through an input and sort through the letters to return specific letters to create an airport code from the airport name.
def airport_code(method, airport, city1):
    city1 = city1
    words = airport.split()
    word1 = words[0]
    word2 = words[1]
    word3 = words[2]
    count = 0
    code = ''

    if method == "name":
        # For loop that will funnel through the first word looking for capital letters.  This will return 2 capital letters if present and then also the first lowercase letter after the second capitol letter.
        for i in range(len(word1)):
            if word1[i].isupper():
                count += 1
                code += word1[i]
                if count ==2:
                    return code + word1[i+1]
        # If the count of capital letters is less than 2, this will return the first letter of the first 3 words in the airport name
        if count<2:
            return word1[0]+word2[0]+word3[0]
    if method == "city":
        return city1[0:3]

# This function calls the airport_code function, asks for the user inputs and runs them through airport_code to provide the desired results.
def main():
    method = input("What coding method would you like to return?\n").lower()
    airport = input("What is the name of the airport?\n")
    city1 = input("What city is the airport located in?\n")
    code1 = airport_code(method, airport, city1)
    print(airport, "-", city1.title(), "-", code1.upper())
#Calls the main() function.
main()


output.write("\n".join(initials)+ "\n")


file = open("us-airports.csv", "r")
line = file.readline()
file_out = open("output.csv","w")
count = 0
while count < 10:
    for line in file:
        name = line.split()
        names = len(name)
        word_1 = name[0]
        word_2 = name[1]
        word_3 = name[2]
        count +=1
        if names > 2:
            print(word_1[0].upper()+word_2[0].upper()+word_3[0].upper())
        else:
            names <= 2
            print(word_1[0].upper,word_2[0].upper())
        file_out.write(names)
file_out.close()
file.close()