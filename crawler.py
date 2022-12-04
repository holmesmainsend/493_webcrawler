import requests
import urllib.robotparser
from bs4 import BeautifulSoup
#import panda as pd

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.amazon.com/robots.txt")
rp.read()
rrate = rp.request_rate("*")
#print(rrate.requests)
#print(rrate.seconds)
rp.crawl_delay("*")
page = 2
url = 'https://www.amazon.com/s?k=dinosaur&crid=M88MOWAW22CT&qid=1670123615&sprefix=dinosaur%2Caps%2C79&ref=sr_pg_1'
while page < 600:
    # sets up starting website (eBay search for "book", starting with second page of results)

    if rp.can_fetch("*", url):
        response = requests.get(url)

        # Extract listing titles on current page
        soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
        listingTitles = soup.findAll("span", class_="a-size-base-plus a-color-base a-text-normal")

        # Prints all titles on current page
        #print("############### Current page number: " + str(page) + " ###############")
        #print()
        for listingTitle in listingTitles:
            print(listingTitle.text)
            print()
    url = 'https://www.amazon.com/s?k=dinosaur&page={page}&crid=M88MOWAW22CT&qid=1670123703&sprefix=dinosaur%2Caps%2C79&ref=sr_pg_{page}'
    page += 1