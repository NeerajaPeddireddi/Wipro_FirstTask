import requests
from bs4 import BeautifulSoup

def test_scrapePatients():
    html=requests.get("http://127.0.0.1:5000/api/patients").text
    soup=BeautifulSoup(html,"html.parser")
    print(soup.prettify())