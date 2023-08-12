import random

#A function do shuffle all the characters of a string 
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#Main programme starts here
uppercaseLetter1=chr(random.randint(65, 90)) #Generate a random Uppercase letter based on ASCII code)
uppercaseLetter2=chr(random.randint(65, 90)) #Generate a random Uppercase letter based on ASCIIcode)
uppercaseLetter3=chr(random.randint(65, 90))  #Generate a random Uppercase letter based on ASCIIcode)
uppercaseLetter4=chr(random.randint(65, 90)) #Generate a random Uppercase letter based on ASCII code)
uppercaseLetter5=chr(random.randint(65, 90)) #Generate a random Uppercase letter based on ASCII code)
lowercaseLetter6=chr(random.randint(97, 122)) #Generate password using all the characters, in random order
lowercaseLetter7=chr(random.randint(97, 122))  #....
digit1=chr(random.randint(48, 57))
digit2=chr(random.randint(48, 57))
#Generate password using all the characters, in random order
password = uppercaseLetter1  + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + lowercaseLetter6 + lowercaseLetter7 + digit1 + digit2
password = shuffle(password)

#output
print(password)


