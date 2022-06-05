# Using Web Services
# https://www.py4e.com/lessons/servces
I'm trying to solve the assignments from coursera - Python.

Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
for line in handle:
    line = line.strip()
    if line.startswith("From"):
        words = line.split()
        email = words[1]
        lst.append(email)

dct = dict()
for email in lst:
    dct[email] = dct.get(email,0)+1

bigcount = None
email_address = None
for key,value in dct.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        email_address = key

print email_address, bigcount