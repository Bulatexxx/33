# import vk_api
# import random
#
#
#
# vk = vk_api.VkApi(token="vk1.a.LqQaubld_fPZKB4vjfrUNd84An-3pEkpRjexVExa5-nquVPchMNmzYU5CZQQra7KZlPVWo93o7F_iVXisHs8utpcM247PRWak3K_hryeMT1mYeh99EV4A4PSR-ZHfqVlqFyQx7M4R2ePecQ8mLUYQynBxF6_g2lmGqDSlxi2WP9vej1tFEQ0lLEU7SZzW"
#                         "QRKTQAZazu_bG4k7YkzvgjlIQ")
#
#
# while True:
#     messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
#     if messages['count'] >= 1:
#         msg_text = messages['items'][0]['last_message']['text']
#
#         if msg_text.lower() == "курс":
#             pass
#         else:
#             pass
#
#
#             ans = f"Курс доллара сост {get_dollar_course}"
#
#
#         user_id = messages['items'][0]['last_message']['from_id']
#         vk.method(
#             "messages.send",
#             {
#                 'random_id': random.randint(-10 ** 7, 10 ** 7),
#                 'user_id': user_id,
#                 'message': msg_text
#             }
#         )
#
#
#


import vk_api
import random
import requests


vk = vk_api.VkApi(token="vk1.a.LqQaubld_fPZKB4vjfrUNd84An-3pEkpRjexVExa5-nquVPchMNmzYU5CZQQra7KZlPVWo93o7F_iVXisHs8utpcM247PRWak3K_hryeMT1mYeh99EV4A4PSR-ZHfqVlqFyQx7M4R2ePecQ8mLUYQynBxF6_g2lmGqDSlxi2WP9vej1tFEQ0lLEU7SZzWQRKTQAZazu_bG4k7YkzvgjlIQ")

def get_dollar_course():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return response['Valute']['USD']['Value']


while True:
    messages = vk.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
    if messages['count'] >= 1:
        msg_text = messages['items'][0]['last_message']['text']

        if msg_text.lower() == "курс":
            ans = f"Курс доллара сегодня {get_dollar_course()} рублей"
        else:
            ans = "Я не понимаю вас, напишите \'курс\', чтобы получить информацию о курсе доллара."

        user_id = messages['items'][0]['last_message']['from_id']
        vk.method(
            "messages.send",
            {
                'random_id': random.randint(-10 ** 7, 10 ** 7),
                'user_id': user_id,
                'message': ans
            }
        )










