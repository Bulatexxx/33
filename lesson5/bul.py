# a = 10
# b = 20
# c = 30
# d = 40
# result = a > b
#
#
# if (a < b) and (c < d):
#     print(True)
# else:
#     print(False)
#
#
#
# my_str = ' '
# my_list = [1]
# my_dist = {'key': 'value'}
#
# if my_str:
#     print(True)
# else:
#     print(False)

import requests

response = requests.get("https://swapi.dev/api/")

starships_url = response.json()['starships']

for i in range(1, 6):
    starships_url = f'{starships_url}{i}'
    response = requests.get(starships_url)
    print(response.json())


#     data['diameter'] = int(data['diameter'])
#     planets_list.append(data)
#
#
# print(max(planets_list, key=lambda x: x['diameter']))

# import requests
#
# response = requests.get('https://swapi.dev/api/starships/')
# print(response.json())
# starships_api = response.json()['results']
# max_speed = 0
# fastest_ship = ""
#
# for ships in starships_api:
#     speed = ships.get("max_atmosphering_speed")
#     if speed == "obscure":
#         continue
#     speed = int(speed)
#     if speed > max_speed:
#         max_speed = speed
#         fastest_ship = ships.get("name")
#
# print("самый быстрый корабль:", fastest_ship)

# import requests
#
# response = requests.get('https://swapi.dev/api/starships/').json()
# starships_api = response.get('results')
#
# max_speed = 0
# fastest_ship = ""
#
# for ship in starships_api:
#     speed = ship.get("max_atmosphering_speed")
#     if speed == "unknown":
#         continue
#     speed = int(speed)
#     if speed > max_speed:
#         max_speed = speed
#         fastest_ship = ship.get("name")
#
# print("The fastest ship is:", fastest_ship)
# response = requests.get(f'{planets_url}{i}')
#     data = response.json()
#     data['diameter'] = int(data['diameter'])
#     planets_list.append(data)
#
#
# print(max(planets_list, key=lambda x: x['diameter']))



# import requests
#
# response = requests.get('https://swapi.dev/api/starships/').json()
# starships_api = response.get('results')
#
# max_speed = 0
# fastest_ship = ""
#
# for ship in starships_api:
#     speed = ship.get("max_atmosphering_speed")
#     if speed == "unknown":
#         continue
#     speed = int(speed)
#     if speed > max_speed:
#         max_speed = speed
#         fastest_ship = ship.get("name")
#
# print("The fastest ship is:", fastest_ship)
#
#
# import requests
#
# response = requests.get("https://swapi.dev/api/")
#
# planets_url = response.json()['planets']
# print(planets_url)
#
# response = requests.get(planets_url)
# print(response.json())
#
# planets_list = []
# for i in range(1, 6):
#     response = requests.get(f'{planets_url}{i}')
#     data = response.json()
#     data['diameter'] = int(data['diameter'])
#     planets_list.append(data)
#
#
# print(max(planets_list, key=lambda x: x['diameter']))



# import requests
#
# response = requests.get('https://swapi.dev/api/starships/')
# starships_api = response.json()['results']
# print(starships_api)
# response = requests.get(starships_api)
# print(response.json())
# max_speed = 0
# fastest_ship = ""
#
# for ships in starships_api:
#     speed = ships.get("max_atmosphering_speed")
#     if speed == "obscure":
#         continue
#     speed = int(speed)
#     if speed > max_speed:
#         max_speed = speed
#         fastest_ship = ships.get("name")
#
# print("самый быстрый корабль:", fastest_ship)




