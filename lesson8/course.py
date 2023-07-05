import requests
from bs4 import BeautifulSoup
from datetime import datetime


today = datetime.today().strftime("%d.%m.%Y")
print(today)
response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp, params={'date_req': today")
soup = BeautifulSoup(response.content, features="xml")

def get_currency(currency_id):
    valute = soup.find("Valute", ID=currency_id)
    valute_value = valute.Value.text
    valute_value = valute.Name.text

    valute_info = {'name': valute_name, 'value': valute_value}

    return valute_info


# print(get_currency("R01010")['name'], get_currency("R01010"['valute'])



