# Databases
# https://www.py4e.com/lessons/database
""""url = "http://www.kite.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection.")""""







import re

hand = open("regex_sum_24962.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)