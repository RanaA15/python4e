#Write a program to read through a mail log, build a histogram
# Using a dictionary to count how many messages have come
# from each email address, and print the dictionary.

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
print(counts)