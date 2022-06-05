fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        print words[1]
        count = count + 1
    else:
        continue        
print "There were", count, "lines in the file with From as the first word"`