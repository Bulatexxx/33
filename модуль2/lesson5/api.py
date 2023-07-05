import requests

response = requests.get("https://swapi.dev/api/")
print(response.json())
planets_url = response.json()['planets']

planets_list = []
for i in range(1, 6):
    response = requests.get(f'{planets_url}{i}')
    data = response.json()
    data['diameter'] = int(data['diameter'])
    planets_list.append(data)

print(max(planets_list, key=lambda x: x['diameter']))

max_diameter = 0

for planet in planets_list:
    if planet['diameter'] > max_diameter:
        max_diameter = planet['diameter']

for planet in planets_list:
    if planet['diameter'] == max_diameter:
        print(planet)
        break


# import requests
# import json
#
# url = 'https://swapi.dev/api/'
# response = requests.get(url).json()
# starships_api = response.get('starships')
#
#
# def check_planets(url):
#     speedlist = []
#     infolist = []
#     for i in range(1, 5):
#         response = requests.get(f'{url}/{i}').json()
#         infolist.append({response.get('name'): response.get('max_atmosphering_speed')})
#         speedlist.append(response.get('max_atmosphering_speed'))
#     print(speedlist)
#     print(infolist)


# check_planets(starships_api)