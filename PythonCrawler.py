import lxml
import requests
import urllib.robotparser
from bs4 import BeautifulSoup
import pandas as pd

locations = ['hartford', 'newlondon', 'newhaven', 'nwct']
locationsIndex = 0
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.craigslist.org/robots.txt")
rp.read()
rrate = rp.request_rate("*")
rp.crawl_delay("10000")
pagen = 0
newlstt = []
newlstp= []

url = 'https://'+locations[locationsIndex]+'.craigslist.org/search/cta'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
response = requests.get(url,headers,timeout=5)
soup = BeautifulSoup(response.content, 'lxml')  # Parse lxml
totalItems = soup.find("span", class_='totalcount')
while locationsIndex < 3:
    while pagen < int(totalItems.text):
        # sets up starting website (craigslist cars+trucks section, starting with first page of results)

        if rp.can_fetch(str(headers), url):
            response = requests.get(url,headers,timeout=5)

            # Extract listing titles on current page
            soup = BeautifulSoup(response.content, 'lxml')  # Parse lxml
            posts = soup.find_all('li', class_='result-row')

            listingTitles = soup.findAll("a", class_='result-title hdrlnk')
            listingPrices = soup.findAll("span", class_="result-price")

            # Prints all titles on current page
            for y in range(0, len(listingTitles)-1):
                if listingTitles[y+1].text == listingTitles[y].text:
                    continue
                else: newlstt.append(listingTitles[y].text)

            for x in range(0, len(listingPrices)-1):
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
# Putting results into a spreadsheet
item_data = pd.DataFrame({'Title': newlstt, 'Price': newlstp})
item_data.to_csv('ResultsFromCrawler.csv')


