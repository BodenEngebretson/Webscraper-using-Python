from bs4 import BeautifulSoup
import requests

url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

for h3 in soup.find_all("h3", class_="country-name"):
    print(h3.text.strip())