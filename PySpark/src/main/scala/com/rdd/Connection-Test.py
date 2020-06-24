import requests
req = requests.get("https://www.datacamp.com/")
print(req.status_code)
print(req.headers)


'''
import urllib.request
# open a connection to a URL using urllib
webUrl = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

# Get the result code and print it
print("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print(data)
'''