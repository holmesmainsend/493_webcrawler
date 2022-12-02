import requests
from bs4 import BeautifulSoup

page = 2
while page < 600:
    # sets up starting website (eBay search for "book", starting with second page of results)
    url='https://www.ebay.com/sch/i.html?_from=R40&_nkw=book&_sacat=0&_pgn={page}'
    response = requests.get(url)

    #Extract book titles on current page
    soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
    bookTitles = soup.findAll("span", role = "heading")  # makes list of book titles

    # Prints all titles on current page
    print("############### Current page number: " + str(page) + " ###############")
    print()
    for bookTitle in bookTitles:
        print(bookTitle.text)
        print()
    
    page = page + 1