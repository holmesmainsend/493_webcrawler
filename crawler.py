import requests
import urllib.robotparser
from bs4 import BeautifulSoup
#from requests import get
#from time import time, sleep
#from random import randint
#from IPython.core.display import clear_output
import pandas as pd
locations = ['hartford','newlondon','newhaven','nwct']
locationsIndex = 0
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.craigslist.org/robots.txt")
rp.read()
rrate = rp.request_rate("*")
rp.crawl_delay("*")
pagen= 0
newlstt = []
newlstp=[]
#s = input("Enter a keyword: ")
url = 'https://'+locations[locationsIndex]+'.craigslist.org/search/cta'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
totalItems = soup.find("span", class_ = 'totalcount')
while locationsIndex < 3:
    while pagen < int(totalItems.text):
        # sets up starting website (craigslist cars+trucks section, starting with first page of results)

        if rp.can_fetch("*", url):
            response = requests.get(url)

            # Extract listing titles on current page
            soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
            #listingLinks = soup.findAll("h3", class_="result-heading")

            listingTitles = soup.findAll("a", class_= 'result-title hdrlnk')
            listingPrices = soup.findAll("span", class_="result-price")

            # Prints all titles on current page
            for y in range(0,len(listingTitles)-1):
                print(listingTitles[y].text)
                if listingTitles[y+1].text == listingTitles[y].text:
                    continue
                else: newlstt.append(listingTitles[y].text)

            for x in range(0,len(listingPrices)-1):
                print(listingPrices[x].text)
                if listingPrices[x+1].text == listingPrices[x].text:
                    continue
                else: newlstp.append(listingPrices[x].text)
        while len(newlstt) < len(newlstp):
            newlstt.append('')
        while len(newlstp) < len(newlstt):
            newlstp.append('')

        pagen += 120

        url = 'https://'+locations[locationsIndex]+'.craigslist.org/search/cta?s={pagen}'
    locationsIndex += 1
    url = 'https://'+locations[locationsIndex]+'.craigslist.org/search/cta'
    pagen = 0
item_data = pd.DataFrame({'title': newlstt, 'price': newlstp})
item_data.to_csv('item_data_raw.csv')
