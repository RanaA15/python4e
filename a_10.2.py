#This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that string
# into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fname = input('Enter a file name:')
counts = dict()
try:
    fhand = open(fname)
except:
    print('Invalid File Name')
    quit()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]                     #Find the section of the line that contains time information
        findhour = time.split(':') #Splits this section by the semicolon in order to separate hour, minute and second (pos 0, 1 and 2 respectively)
        hour = findhour[0] 
        counts[hour] = counts.get(hour,0) + 1 #Checks to see if the hour is present in the dictionary, default is 0. If not present, it gets added with a value of 1. If already present, 1 is added to prev count.


lst = list()    #Creates a list

for key, val in list(counts.items()): 
    lst.append((key, val)) #Adds the hour, count to a list
lst.sort(reverse = False) #Sorts from lowest to greatest

for key, val in lst[:]:
    print(key, val) #Prints out counts, sorted by hour