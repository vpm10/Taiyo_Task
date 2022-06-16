# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
from csv import writer


# Function can scrape all the links in webpage
# function to extract html document from given url
def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


# assign required credentials
# assign URL
url_to_scrape = "https://www.bls.gov/"

# create document
html_document = getHTMLdocument(url_to_scrape)

# create soap object
soup = BeautifulSoup(html_document, 'html.parser')

# find all the anchor tags with "href"
# attribute starting with "https://"
for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    print(link.get('href'))


# The below code gives the updated information everyday.
# If we have data that varies in every time remove that break point which gives updated data each itration
def parseDate():
    url = 'https://www.bls.gov/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    month = soup.find('div', class_='nr-date-month')
    date = soup.find('div', class_='nr-date-day')
    heading = soup.find('span', class_='heading')
    info = [month, date, heading]
    return info


while True:
    print('the current sta :' + str(parseDate()))
    break

# The below code can scrape the all data in the website and can save as csv file
url = 'https://www.bls.gov/news.release/ximpim.nr0.htm'
with open('details.csv', 'w', encoding='utf8', newline='') as file:
    the_writer = writer(file)
    header = ('Tittle', 'Content')
    the_writer.writerow(header)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find(id="container")
    tittle = soup.find_all('h1')
    content = soup.find_all('div', class_='normalnews')
    info = [tittle, content]
    the_writer.writerow(info)
    print(tittle)
    print(content)
