# Import webscrapping module & urllib

from bs4 import BeautifulSoup 
import urllib.request

req = urllib.request.urlopen('https://www.eleconomista.es/rss/rss-flash-del-mercado.php')

# extraction format in html default so we've assigned the xml format
xml = BeautifulSoup(req, 'xml')

#Loop for taking all the links of the xml from the third one ([3:])
for item in xml.findAll('link')[3:]:
    print(item.text)
