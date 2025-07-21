import requests
url="https://quotes.toscrape.com/"

response=requests.get(url)

if response.status_code==200:

    print("Fetched  the web page successfully")
else:
    print(f"Failed:{response.status_code}") 

from bs4 import BeautifulSoup

soup=BeautifulSoup(response.text,"html.parser")
#print(soup)

Title= soup.find("div",class_="col-md-8")

print(Title.text.strip())

quotes=soup.find_all("span",class_="text")
#print(quotes)
#for quote in quotes:
   # print(quote.text)

authors=soup.find_all("small",class_="author")

#for author in authors:
    #print(author.text)

quote=soup.find("div"class_="quote")
links=quote.find_all("a",class_="tag")  
for link in links:
    print(link.text)  
    print(link["href"])

pages=1

while pages <=3:
    url=f"https://quotes.toscrape.com/pages/{pages}"
    response=requests.get(url)
