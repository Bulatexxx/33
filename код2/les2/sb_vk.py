import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)
soup = BeautifulSoup(response.content, features="xml")


def get_course():
    return soup.find("Valute", ID=course.id).Valute.text




