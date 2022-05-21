#Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (Chapter 5) to find who has the most messages
# and print how many messages the person has

fname = input('Enter file name: ')
counts = dict()
try:
    fhand = open(fname)
except:
    print('Invalid File Name')
    quit()

for line in fhand:
    if not line.startswith('From'):
        continue
    if line.startswith('From '):
        word = line.split()
        email = word[1]
        counts[email] = counts.get(email, 0) + 1

largest = -1
maxemail = None
for email,value in counts.items():
    if value > largest:
        largest = value
        maxemail = email
print(maxemail, largest)
