from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from bs4 import BeautifulSoup
import requests

link = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination" \
       "%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east" \
       "%22%3A-122.22184218359375%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37" \
       ".847169233586946%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState" \
       "%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D" \
       "%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C" \
       "%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr" \
       "%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22" \
       "%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible" \
       "%22%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en-US",
}

response = requests.get(url=link, headers=headers)
data = response.text
# print(data)
soup = BeautifulSoup(data, "html.parser")
listing = soup.select(".bfcHMx a")

# ----------------------------------------------------------------------------- LINKS
link_list = []
sub_list = []
for l in listing:
    link = l["href"]
    sub_list.append(link)
sub_list = list(dict.fromkeys(sub_list))

for sub in sub_list:
    if "http" not in sub:
        link_list.append(f"https://www.zillow.com{sub}")
    else:
        link_list.append(sub)

# print(link_list)

# ----------------------------------------------------------------------------- PRICES
price_list = []
prices = soup.select(".hRqIYX")
for p in prices:
    price = p.get_text()
    price_list.append(price)
print(price_list)
