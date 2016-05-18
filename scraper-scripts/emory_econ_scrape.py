import requests
from lxml import html
# takes the given webpage and scrapes out the specified section's html

page = requests.get('http://economics.emory.edu/home/undergraduate/major_minor_requirements.html')

pagetree = html.fromstring(page.content)

raw_html = pagetree.xpath("//div[@class='data-entry ']/h2/strong")
text_html = pagetree.xpath("//div[@class='data-entry ']/ul/li")

contains = dict()
temp = ""
x = 0
# for item in raw_html:
#    temp = (item.text.strip())
#    x = x + 1
#    contains[x] = temp

for item in text_html:
    temp = (item.text.strip())
    x = x + 1
    contains[temp] = x

econmajor = dict()
x = 0

for key, value in contains.iteritems():
    if key.startswith('Econ') | key.startswith('Math'):
        x = x + 1
        econmajor[key] = x

for key, value in econmajor.iteritems():
	print key
