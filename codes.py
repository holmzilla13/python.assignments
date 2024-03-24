# Steven Holmes
# COP 2500
# Code Database
# March 31,2023

# This function accepts a read file as an input and reads through each individual line, if the line contains at least 3 words, it retreives the first letter
# of each word and joins them together.  If the line has 2 words, it pulls the first letter of each and word and joins them together.  It keeps all of these ordered
#in a list.
def airport_names(input, output):
    initials_list = []
    line = input.readline()
    for line in input:
        words = line.split()
        line_len = len(words)
        if line_len >2:
            initials = words[0][0] + words [1][0] + words [2][0]
        elif line_len == 2:
            initials = words[0][0]+words[1][0]
        initials_list.append(initials)
    return initials_list


# This function opens a document for reading and a document for writing.  Once the "airport_names" function runs, this will sort initals list and write each set
# to a new file.  Each line from the input file will be output onto its own line in subsequent order.  This will also capitalize the initials before writing them to the new document. 
def main():
    input = open("us-airports.csv", "r", encoding="utf-8")
    output = open("output.csv", "w")
    initials = airport_names(input,output)
    for i in range(len(initials)):
        output.write(initials[i].upper() + "\n")
    input.close()
    output.close()

# This calls the main function which will perform both main and airport_names function.
main()
main()