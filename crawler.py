import requests
import urllib.robotparser
from bs4 import BeautifulSoup
#from requests import get
#from time import time, sleep
#from random import randint
#from IPython.core.display import clear_output
import pandas as pd

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.craigslist.org/robots.txt")
rp.read()
rrate = rp.request_rate("*")
#print(rrate.requests)
#print(rrate.seconds)
rp.crawl_delay("*")
pagen= 0
page = 0
newlstt = []
newlstp=[]
#s = input("Enter a search: ")
url = 'https://hartford.craigslist.org/search/sss?query=car'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
totalItems = soup.find("span", class_ = 'totalcount')
while pagen < int(totalItems.text):
    # sets up starting website (eBay search for "book", starting with second page of results)

    if rp.can_fetch("*", url):
        response = requests.get(url)

        # Extract listing titles on current page
        soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
        #listingLinks = soup.findAll("h3", class_="result-heading")

        listingTitles = soup.findAll("a", class_= 'result-title hdrlnk')
        listingPrices = soup.findAll("span", class_="result-price")

        # Prints all titles on current page
        #print("############### Current page number: " + str(page) + " ###############")
        #print()
        for listingTitle in listingTitles:
            print(listingTitle.text)
            print()
            newlstt.append(listingTitle.text)
        for x in range(0,len(listingTitles)):
            print(listingPrices[x].text)
            newlstp.append(listingPrices[x].text)
       # for listingLink in listingLinks:
        #    print(listingLink)

    item_data = pd.DataFrame({'title': newlstt, 'price': newlstp})

    pagen += 120
    page += 1
    url = 'https://hartford.craigslist.org/search/sss?s={pagen}&query=cars'


print(len(newlstt), len(newlstp))
print(item_data.info())
item_data.tail(10)

item_data.to_csv('item_data_raw.csv')
