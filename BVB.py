import requests
from bs4 import BeautifulSoup

url = 'https://www.bvb.ro/FinancialInstruments/Indices/IndicesProfiles'

number = float(input('Insert sum'))

data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')

final_dict = {}

for line in soup.select('tbody tr'):
    if line.contents[1].contents[0].name == 'a':
        final_dict[line.contents[1].contents[0].text] = number*float(line.contents[-2].text.replace(',','.'))/100

print(final_dict)