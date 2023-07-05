class House:
    def __init__(self, square, count_of_floors, color):
        self.square = square
        self.count_of_floors = count_of_floors
        self.color = color
    def __str__(self):
        return f"Дом площадью {self.square}, кол-во этажей {self.count_of_floors}, цвет дома {self.color}"
    def print_info(self):
        print(f"Дом площадью {self.square}, кол-во этажей {self.count_of_floors}, цвет дома {self.color} ")
    def do_something(self):
        pass
house = House(200, 10, 'red')
print(house)
# print(house.square)
# print(house.color)
#  print(house.count_of_flours)


# class Auto:
#     def __init__(self, brand, max_speed, weight):
#         self.brand = brand
#         self.max_speed = max_speed
#         self.weight = weight
#
#
# my_favorite_auto = Auto('porshe', 411, 3)
# andrew_favorite_auto = Auto('Mersedes', 500, 2)
#
# print(my_favorite_auto.brand)
# print(andrew_favorite_auto.brand)
