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

print (email_address, bigcount)