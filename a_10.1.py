#Revise a previous program as follows: Read and parse the "From" lines and pull
# out the addreses from the line. Count the number of messages from each person using a dictionary. 
#After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary/
#Then sort the list in reverse order and print out the person who has the most commits. 

fname = input("Enter file name: ")
counts = dict()

try:
    fhand = open(fname)
#Excep statement to counteract any improper file names or inputs
except:
    print('Invalid file name')
    quit()
#Searches through the file for all lines that start with 'From',
#  skips all other lines

for line in fhand:
    if not line.startswith('From '):
        continue
# If the line starts with from, line is split into a list of words
# Emails are always at position 1 when the line starts with 'From'
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email,0) +1

lst = list()

for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse = True)

for val, key  in lst[:1]:
    print(key, val)