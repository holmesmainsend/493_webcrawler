# Still need to decide what webpage to use, ccsu's directory website has 5 pages
# Next Step: Get to next page and extract emails from there

import requests
from bs4 import BeautifulSoup

# sets up starting website
url='https://directory.ccsu.edu/'
response = requests.get(url)

#Extract page 1 of Faculty Emails
soup = BeautifulSoup(response.text, 'html.parser')  # Parse HTML
print(soup.title) # Title Page
emails = soup.findAll("div", class_="profile-email")  # makes list of emails

# Prints all emails on page 1
for email in emails:
    print(email.text)
