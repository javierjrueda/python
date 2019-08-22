# Import webscrapping module & urllib

from bs4 import BeautifulSoup 
import urllib.request
import time

req = urllib.request.urlopen('https://www.eleconomista.es/rss/rss-flash-del-mercado.php')

# extraction format in html default so we've assigned the xml format
xml = BeautifulSoup(req, 'xml')

#Loop for taking all the links of the xml from the third one ([3:])
for item in xml.findAll('link')[3:]:
    url = 'http:' + item.text
    news = urllib.request.urlopen(url).read()
    print(url)
#Añades "features = "lxml"" para que limar incompatibilidades entre BeautifulSoup yy lxml
    page = BeautifulSoup(news, features = "lxml")
    for p in page.findAll('p'):
        print(p.text)

        time.sleep(5)

        
