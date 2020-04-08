import requests
from bs4 import BeautifulSoup
# Here we extaract the information from "https://www.whitehouse.gov/briefings-statements/"
# We extract the link  which the h2 tag contains.
# Youtube video source ::: https://www.youtube.com/watch?v=87Gx3U0BDlo&t=1s

result=requests.get("https://www.whitehouse.gov/briefings-statements/")
# request function is used to know if the access to the website is legal or not.(sayaad not sure about that)
print(result.status_code)
# code 200 refers to the everything is okay and u r allow to go further for the process.
src=result.content
soup=BeautifulSoup(src,'lxml')
# BeautifulSoup() helps to format the content so that it can be easy for the manipulation of the data
# Here "soup" is object.We use dot notation to access the website content using DOM.

#You can print those things to see the output
#print(src)
#print(soup)

# Creating the empty array "urls" which contains the list of h2 tags urls.
urls=[]

# search  all h2 tag in soup and then it assigned to "h2_tag" variable
for h2_tag in soup.find_all("h2"):
    # all "a" tag inside "h2" tag is assigned to "a_tag" variable
    a_tag=h2_tag.find("a")
    # appending all the "a" tag href to the urls array
    urls.append(a_tag.attrs['href'])


#print(urls[2])

# Printing total numbers of links urls array contains
print(len(urls))