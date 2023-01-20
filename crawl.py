import requests
from bs4 import BeautifulSoup
url = "https://climate.mit.edu/explainers/carbon-capture"


#Step 1: get the html

r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content
print(htmlContent)		# printing the code

# Step 2 : Parse the html

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

# Step 3: HTML tree traversal

title = soup.title   # get title of html page

print(type(title))             #tag
print(type(title.string))      #navigable string
print(type(soup))              #beautiful soup

# get paragraph of html page
paras = soup.find_all('p')
print(paras)


#get first elemenmt in html page
print(soup.find('p'))

# get classes of any element in the html page
print(soup.find('p')['class'])

# find all the elemnts with class lead
print(soup.find_all("p",class_="lead"))

#  Get the text from the tag/soup
print(soup.find('p').get_text())
print(soup.get_text())

#get anchors of html page
anchors = soup.find_all('a')
all_links = set()
# get all the links on the page
for link in anchors:
    if(link != '#'):
       all_links.add("https://codewithharry.com" +link.get('href'))
    
print(anchors)



