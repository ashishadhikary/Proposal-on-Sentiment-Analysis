# -----Scraping the oliz.com website

import requests
from bs4 import BeautifulSoup
result=requests.get("https://www.olizstore.com/moshi-pluma-laptop-sleeve-for-macbook-s-13-blue.html")
print(result.status_code)

src=result.text

soup=BeautifulSoup(src,'lxml')

src1=soup.find_all('span',class_="base")
print(src1)
#src2=src1.text
#print(src2)

print("--------------Name------------------")
for span in src1:
    print(span.text.replace('USD', '').strip())


#product description

print("-------------Description ---------------- ")

review=soup.find('div',class_='product attribute description')
review2=review.find('div',class_='value')
review3=review2.p.span
print(review3.text)


print("---------Features--------------")
feature=soup.find('div',class_='product attribute description')
feature2=feature.find('div',class_='value')
uls=feature2.find("ul")
#print(uls)


for li in uls.find_all('li'):
    print("=>",li.text)


