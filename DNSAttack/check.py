import json
from whois import whois
from random import choices
from urllib.parse import urlparse

jsonFile = open("register.json", "r")
jsonData = json.load(jsonFile)["2021-01-05"]
jsonFile.close()

randomData = choices(jsonData, k=200)

checkData = set()

for site in randomData:
    url = site['link']
    parsedURL = urlparse(url)
    if (parsedURL.scheme == 'https'):
        try:
            whoisData = whois(parsedURL.hostname)
        except:
            continue
        if ('registrar' not in whoisData) or (not whoisData['registrar']):
            checkData.add(parsedURL.hostname)

for site in checkData:
    print(site)