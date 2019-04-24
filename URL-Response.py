#Takes a list of URLs and returns the URL and the response code.
import requests

with open("/root/Documents/subbrute.txt", "r") as subs:
    URLs = []
    for sub in subs:
        URLs.append("http://" + sub[0:-1])
        URLs.append("https://" + sub[0:-1])

output = open("/root/Documents/responses.txt", "a")
i = 0
for url in URLs:
    try:
        response = requests.get(url)
        print(url + " returned: " + str(response))
        
    except Exception:
        print(url + " connection refused.")
        pass
    i += 1
