import requests
url="https://quotes.toscrape.com/"

response=requests.get(url)

#if response.status_code==200:

    #print("Fetched  the web page successfully")
#else:
    #print(f"Failed:{response.status_code}") 

from bs4 import BeautifulSoup

soup=BeautifulSoup(response.text,"html.parser")
#print(soup)

Title=soup.find("div",class_="col-md-8")
#print(Title.text)

quotes=soup.find_all("span",class_="text")
print(quotes)