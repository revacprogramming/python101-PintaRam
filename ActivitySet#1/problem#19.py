"""import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enterthe  URL -')
repeat = int(input('Enter number of repeatations: '))
position = int(input('Enter the link position: '))

#to repeat desired times
for i in range(repeat):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1

        #stopping at desired position
        if count>position:
            break
        url = tag.get('href', None)
        name = tag.contents[0]

print(name)"""




import re
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

url=input('\033[1m Enter the Link \033[0m ->')
#count=int(input("Enter the count(Repeatation): "))
#pos=int(input("Enter the position :"))

html_content=urlopen(url)
#print(html_content)

soup=BeautifulSoup(html_content,"lxml")
all_links=[]
for link  in soup.find_all('a'):
    #print(link.get('href'))
    all_links.append(link.get('href'))
for i in range(7):
    url = Request(all_links[17])
    html_content = urlopen(url)
    soup = BeautifulSoup(html_content,"lxml")
    for title in soup.find_all("title"):
        print(title.get_text())
    all_links.clear() 
    for i in soup.find_all('a'):
        all_links.append(i.get('href'))






