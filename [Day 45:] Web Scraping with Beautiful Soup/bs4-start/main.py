from bs4 import BeautifulSoup
import lxml

file_path = '/home/argento/Documents/Education/100Days_of_Python/[Day 45:] Web Scraping with Beautiful Soup/bs4-start/website.html'

with open (file_path) as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

#print(soup.title)
#print(soup.title.string)
#print(soup.prettify())

#print(soup.a) # first anchor tag

all_anchor_tags = soup.find_all('a')

for tag in all_anchor_tags:
    print(tag.get('href')) # get the href attribute of each anchor tag

heading = soup.find(name='h1', id='name')
print(heading)

section_heading = soup.find(name='h3', class_='heading') # class is a reserved keyword in Python, so we use class_ instead
print(section_heading)
print(section_heading.name)
print(section_heading.getText())


headings = soup.select('.heading') # select all elements with class 'heading'
name = soup.select_one('#name') # select the first element with id 'name'