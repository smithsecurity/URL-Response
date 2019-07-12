#Takes a list of URLs from a file and returns the URL and the response code.
import requests
import sys

if sys.argv[1] == "-h":
        print("Takes a list of subdomains and checks their response code.")
        print("Usage: python3 URL-Response.py <input file> <output file>")
else:
    with open(sys.argv[1], "r") as subs:
        URLs = []
        for sub in subs:
            URLs.append("http://" + sub[0:-1])
            URLs.append("https://" + sub[0:-1])

    output = open(sys.argv[2], "a")
    i = 0
    for url in URLs:
        try:
            response = requests.get(url)
            print(url + " returned: " + str(response))
            output.write(url + " returned: " + str(response) + "\r\n")
            
        except Exception:
            print(url + " connection refused.")
            output.write(url + " connection refused." + "\r\n")
            pass
        i += 1
