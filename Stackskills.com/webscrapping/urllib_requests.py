import urllib.request
import urllib.parse #url encoding to handle the spaces in the url paramaters

values = {'q':'python programming tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search'+data

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

# data = data.encode('utf-8') # Necesario para Python3
print(data)
