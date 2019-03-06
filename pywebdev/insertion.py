from bs4 import BeautifulSoup
import time
import urllib2
#funcion que se conecta con MySQL gracias al archivo dbconnect.py
from dbconnect import connection 

req = urllib2.urlopen('https://www.eleconomista.es/rss/rss-flash-del-mercado.php')

xml = BeautifulSoup(req, 'xml')

c, conn = connection()

for item in xml.findAll('link')[3:]:
    url = 'http:' + item.text

    c.execute("SELECT * FROM links WHERE link = (%s)",
        [url])

    rows = c.fetchall()

    if len(rows) == 0:
        c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
                  [time.time(), url])
        conn.commit()
        print("A new link was founded!")
    else:
        print("Link already in database")


conn.close()
