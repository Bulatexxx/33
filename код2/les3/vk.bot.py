
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from sb_vk import get_course

vk_session = vk_api.VkApi(token="vk1.a.LqQaubld_fPZKB4vjfrUNd84An-3pEkpRjexVExa5-nquVPchMNmzYU5CZQQra7KZlPVWo93o7F_iVXisHs8utpcM247PRWak3K_hryeMT1mYeh99EV4A4PSR-ZHfqVlqFyQx7M4R2ePecQ8mLUYQynBxF6_g2lmGqDSlxi2WP9vej1tFEQ0lLEU7SZzWQRKTQAZazu_bG4k7YkzvgjlIQ")
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        if user_message[0:2] == '-к':
            response = "Курсы доллара {0} руб. за 1 шт евро {1} руб. за 1 шт \Курс юаня {2} руб. за 1 шт".format(
                get_course("R01235"), get_course("R01239"), get_course("R01375")
            )
        elif user_message[0:2] == '-в':
            article = user_
        else:
            response = "Я не понимаю, что вы хотите от меня..."
            vk.messages.send(user_id=event.user_id, message=response, random_id=random.randint(-10 **7, 10 **7))

