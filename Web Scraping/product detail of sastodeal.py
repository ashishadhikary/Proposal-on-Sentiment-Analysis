import requests
from bs4 import BeautifulSoup
result=requests.get("https://www.sastodeal.com/ariel-detergent-powder-2kg.html")
print(result.status_code)

src=result.text


soup=BeautifulSoup(src,'lxml')

src1=soup.find('div',class_='product attribute description')
print(src1)
src2=(src1.find('div',class_="value"))
print(src2)
print(src2.p.text)