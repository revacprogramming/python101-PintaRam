fname = input("Enter file name: ")
if len(fname) == 0:
    fname = open('romeo.txt')
newList = list()
for line in fname:
    words = line.rstrip().split()
    for i in words:
        newList.append(i) 
        newList.sort()
print(newList)










fname = input("Enter file name: ") #Ask the user for the filename.
fh = open(fname)                   #Open the file.
lst = list()                       #Create a list called lst.
for line in fh:                    #For each line in the fh?
	words = line.split()       #Separate the words in the line.
for word in words :           #For each word in words.
         if word not in lst :      #If word not in the lst.
            lst.append(word)       #Add the word.
         elif word in lst :            #Continue looping.
        	continue
lst.sort()
print(lst)                         #Print the lst.