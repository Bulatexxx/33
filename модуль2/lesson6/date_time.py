from datetime import datetime

print(datetime.now().date().month)
# today = datetime.today().strtime('%d.%m.%y')
# print(today)

# print({01} + {02} + {2013})

# import requests
#
# response = requests.get("https://swapi.dev/api/")
# starships_url = response.json()['starships']
#
#
# for i in range(1, 6):
#     starships_url = f'{starships_url}{i}'
#     response = requests.get(starships_url)
#     print(response.json())

