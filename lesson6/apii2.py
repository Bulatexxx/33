import requests
from bs4 import BeautifulSoup
user_currency = input("Введите первые буквы валюты, которая вас инетерсует:").capitalize()
currency_date = input("Введите дату которая вас интересует курс валют в формате dd/mm/yyyy:")
response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")

currencies_list = soup.find_all("Valute")
for currency in currencies_list:
    currency_name = currency.Name.text
    currency_value = currency_Value.text
    currency_nominal = currency_Nominal.text

    if currency_name.startswith(user_currency):
        print(f"({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.")













