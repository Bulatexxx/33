import requests
from xml.etree import ElementTree as ET


class CurrencyInfo:
    def __init__(self, currency_id):
        self.currency_id = currency_id

    def __enter__(self):
        response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
        xml_tree = ET.fromstring(response.content)
        currency_rate = None
        for valute in xml_tree.findall('Valute'):
        if valute.find('CharCode').text == self.currency_id:
        currency_rate = float(valute.find('Value').text.replace(',', '.'))
        break
        if currency_rate is None:
            raise ValueError(f'Currency with code {self.currency_id} not found.')
            self.rate = currency_rate
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def info(self, count):
        if count == 1:
            return f"(1 шт.) {self.currency_id} стоит {self.rate} руб."
        else:
            return f"({count} шт.) {self.currency_id} стоят {count * self.rate} руб."


with CurrencyInfo('AUD') as currency:
print(currency.info(1))  # (1 шт.) Австралийский доллар стоит 49.2779 руб.

with CurrencyInfo('USD') as currency:
print(currency.info(5))  # (5 шт.) Доллар США стоят 408.1605 руб.

with CurrencyInfo('ZZZ') as currency:
print(currency.info(1))  # ValueError: Currency with code ZZZ not found.