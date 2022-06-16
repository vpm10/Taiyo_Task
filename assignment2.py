from bs4 import BeautifulSoup
import requests
from csv import writer
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
}
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
