import requests

from bs4 import BeautifulSoup

url="https://www.jumia.co.ke/catalog/?q=deals+of+the+week"
response=requests.get(url)
print(response)
print(response.status_code)

#create a fake user-so that you do not get blocked
headers={
    "user_agent":"chrome/5.0"
}

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,"html.parser")
print(soup)
print(soup.prettify())

products=soup.find_all("article",class_="prd")
print(products)
print(products[0].prettify())

import csv
product_data=[]

for product in products:
    name=product.select_one(".name")
    brand=product.select_one(".brand")
    price=product.select_one(".prc")
    old_price=product.select_one(".old")
    discount=product.select_one(".discount_selector_here")
    reviews=product.select_one(".rev")
    rating=product.select_one(".stars")

    product_data.append({
        "product name":name.get_text(strip=True) if name else "N/A",
        "price (Ksh)": price.get_text(strip=True) if price else "N/A",
        "old price":old_price.get_text(strip=True) if old_price else "N/A",
        "Discount (%)":discount.get_text(strip=True) if discount else "0%",
        "Rating":rating["style"] if rating and rating.has_attr("style") else "N/A",
        "Total reviews":reviews.get_text(strip=True) if reviews else "0"
    })

keys=product_data[0].keys()
with open("jumia_deals.csv","w" , newline="", encoding="utf-8") as f:
    writer=csv.DictWriter(f,fieldnames=keys)
    writer.writeheader()   
    writer.writerows(product_data)
print("Data collection complete. Check 'jumia_deals.csv'")