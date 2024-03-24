def airport_names(airport):
    words = airport.split()
    if len(words) > 0:
        word1 = words[0]
        caps = [c for c in word1 if c.isupper()]
        if len(caps) == 2:
            return caps
    return None

def main(airport):
    caps = airport_names(airport)
    if caps is not None:
        print(caps)
 
main(airport = input("What is the name of the airport?\n"))
    

def airport_name(airport):
    caps1 = []
    caps2 = False
    for c in airport:
        if c.isupper():
            caps1.append(c)
            if len(caps1) == 2:
                caps2 = True
        elif caps2:
            return ''.join(caps1) + c
    if len(caps1) < 2:
        return caps1[0]
    else:
        return ''.join(caps1)

def main():
    airport = input("What is the name of the airport?\n")
    code1 = airport_name(airport).upper()
    print(code1)

    
    
main()

