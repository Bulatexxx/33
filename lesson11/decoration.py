# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs):
#         print("Время работы функции '{func_name} сoставило {totsl_time} ")
#
#
#
#
# def get_list_by_default(val):
#     start = time.time()
#     my_list = []
#     for i in range(val):
#         my_list.append(i)
#         end = time.time()
#
#     print("time", end - start)
#     return my_list
#
#
#
# def get_list_by_comp(val):
#
#     my_list = [i for i in range(val)]
#     return my_list
#
#
# get_list_by_comp(10 ** 6 * 15)
# get_list_by_default(10 ** 6 ** 15)
# import random
# age = 18
#
# is_allow = True if age >= 18 else False
#
# print(is_allow)


# class User:
#     def __init__(self, name, health, strength, agility):
#         self.name = name
#         self.health = health
#         self.strength = strength
#         self.agility = agility
#
#
# class Mage(User):
#     def __init__(self, name, health, strength, agility, mana):
#         super().__init__(name, health, strength, agility)
#         self.mana = mana
#
#
# class Warrior(User):
#     def __init__(self, name, health, strength, agility, weapon):
#         super().__init__(name, health, strength, agility)
#         self.weapon = weapon
#
#
# class Archer(User):
#     def __init__(self, name, health, strength, agility, bow):
#         super().__init__(name, health, strength, agility)
#         self.bow = bow




import random
#
# greetings = ['Здравствуйте!', 'Привет!', 'Добрый день!', 'Рад вас видеть!']
# print("Привет")
# print(random.choice(greetings))
import random
movies = ["The Godfather", "The Dark Knight", "Forrest Gump", "Inception","The Matrix", "Interstellar"]

def recommend_movie():
    print("Фильм: ")
    print(random.choice(movies))


recommend_movie()