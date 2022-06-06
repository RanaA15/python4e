#Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that
# matched the regular expression

import re
fname1 = input('Enter a file name:')
try: #Tests the file name to see if it exists in the directory, if not, program quits
    fhand = open(fname1)
except:
    print('Invalid File Name')
    quit()
fname2 = input ('Enter a regular expression:')
count = 0

for line in fhand:
    line = line.rstrip()
    x = re.findall(fname2, line) #Searches through lines based on the inputted regex
    if len(x) < 1: #If the len(x) is less than 1, the program did not find a match
        continue
    else: #If a match is found, add to the count
        count += 1

print(fname1,'had', count, 'lines that matched', fname2)

