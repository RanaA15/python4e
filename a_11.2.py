import re
fname = input('Enter a file name:')
try: #Tests the file name to see if it exists in the directory, if not, program quits
    fhand = open(fname)
except:
    print('Invalid File Name')
    quit()
numlist = list()
count = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ''([0-9]+)', line)
    if len(x) < 1:
        continue
    else:
        numlist.append(x)
        count += 1
onelist = sum(numlist, [])
intlist = map(int, onelist)
avglist = int(sum(intlist)/count)
print(avglist)




