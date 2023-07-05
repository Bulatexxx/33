# def func(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#
#
#
# func(10, 20, 30, 40, 50, 60, 70, 'Алина', 'Булат', name='Ксюша')

# def func(a, b="apple"):
#     print(a, b)
#
#
# func(10)


# age = 18
#
# if age >= 18:
#     is_allow = 'yes'
# else:
#     is_allow = 'no'
#
# print(is_allow)
# citizenship = "РФ"
# is_allow = 'yes' if age >= 18 and citizenship == "РФ" else 'no'
# print(is_allow)




# a = False
# b = True
#
# c = a or b
#
# print(c)

# my_list = [i if i % 3 == 0 else i ** 2 for i in range(1000) if i % 5 == 0]
#
# print(my_list)


# my_dict = {i: len(i) for i in ['orange', 'green', 'blue'] if len(i) !=5}
# print(my_dict)

# my_list_1 = [1, 2]
# my_list_2 = [1, 2]
# a = 20
# b = 20
# print(my_list_1 == my_list_2)
# print(my_list_1 is my_list_2)
# print(a is b)


# print(id(a), id(b))
# print(id(my_list_1), id(my_list_2))




# my_tuple = (1, 2, 3, 4, 5)
# print(type(my_tuple))
# print(my_tuple.count(4))
# print(my_tuple.index(4))
# print(my_tuple[2:4])

# my_tuple = (i for i in range(100))
# print(my_tuple)
#
# for i in my_tuple:
#     print(i)


# my_list =[1, 2, 3, 4, 4]
# my_set = set(my_list)
# print(my_set)
# my_set = {1, 2, 3, 4, 5}
# my_set_2 = {4, 5, 6, 7, 8}
# print((my_set.intersection(my_set_2)))
# print(my_set.union((my_set_2)))


# import threading
# import time
# import tkinter
# import random
# import ctypes
#
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#
#
# def update(root, label, smile, color):
#     root.config(background=["black", "white"][color])
#     label.config(fg=["black", "white"][not color], bg=["black", "white"][color])
#     smile.config(fg=["black", "white"][not color], bg=["black", "white"][color])
#     root.after(750, lambda: update(root, label, smile, not color))
#
#
# def you_are_an_idiot():
#     root = tkinter.Tk()
#     root.title("you are an idiot")
#     root.geometry(f"+{random.randint(0, screensize[0])}+{random.randint(0, screensize[1])}")
#     label = tkinter.Label(root, text="you are an idiot", font=("Times New Roman", 30))
#     smile = tkinter.Label(root, text="☺ ☺ ☺", font=("Times New Roman", 54))
#     label.pack()
#     smile.pack()
#     root.after(750, lambda: update(root, label, smile, False))
#     root.mainloop()
#
#
# for i in range(500):
#     my_thread = threading.Thread(target=you_are_an_idiot)
#     my_thread.start()
#
#
# import requests
# import json
#
# url = "https://swapi.dev/api/vehicles/"
#
# response = requests.get(url).json()
# starships_api = response.get('starships')
#
#
# def starships(url):
#     response_starships = requests.get(url).json()
#     for i in response_starships['results']:
#         print(i['name'])
#         print(i['max_atmosphering_speed'])
#
#
# starships(url)

# import requests
#
# res = requests.get('https://swapi.dev/api/starships/').json()['results']
#
# print(max(((x['name'], x['max_atmosphering_speed']) for x in res),
#     key=lambda x: int(x[1].replace('n/a', '0').replace('km', '')))[0])


even_numbers = []
odd_numbers = []

for i in range(10):
    number = int(input("Введите число!: "))
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("четные числа:", even_numbers)
print("нечетные числа:", odd_numbers)
