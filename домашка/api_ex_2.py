
#
# response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
# soup = BeautifulSoup(response.content, features="xml")
# australian_dollar = soup.find("Valute", ID="R01010")
# armanian_dram = soup.find("Valute", ID="R01090B")
# bulgar_lev = soup.find("Valute", ID="")
# print(australian_dollar, armanian_dram, bulgar_lev)
# currency_value = australian_dollar.Value.text
# currency_value = armanian_dram.Value.text
# currency_value = bulgar_lev.Value.text
# currency_nominal = australian_dollar.Nominal.text
# currency_nominal = armanian_dram.Nominal.text
# currency_nominal = bulgar_lev.Nominal.text
# currency_name = australian_dollar.Name.text
# currency_name = armanian_dram.Name.text
# currency_name = bulgar_lev.Name.text
# print(f"({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value}")
#
#
# currencies_list = soup.find_all("Valute")
# for currency in currencies_list:
#     get_course(currency["ID"])


valute_from = "EUR"
valute_to = "USD"
amount = int(input("Введите сумму, которую будем конвертировать: "))


def course(valute_from, valute_to, amount):
    cost = {
        "RUR": 1.0,
        "USD": 70.38,
        "EUR": 76.73
    }

    if valute_from == "RUR":
        return amount / cost[valute_to]
    else:
        return amount / cost[valute_from] * cost[valute_to]


print("конвертация:", course(valute_from, valute_to, amount))


