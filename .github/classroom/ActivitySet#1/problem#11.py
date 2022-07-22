""""Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order."""
fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
hand = open(fname)

LIST = list()

for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    LIST.append(line[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword,bigcount)