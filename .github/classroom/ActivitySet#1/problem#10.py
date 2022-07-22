romeo = input("Enter file name: ") #Ask the user for the filename.
fh = open(romeo)                   #Open the file.
lst = list()                      #Create a list called lst.
for line in fh:                    #For each line in the fh?
	words = line.split()         #Separate the words in the line.
	for word in words :              #For each word in words.
         if word not in lst :      #If word not in the lst.
            lst.append(word)       #Add the word.
        # else:                    #Continue looping.
        #	continue
         #lst.sort()
print(sorted(lst))                         #Print the lst.