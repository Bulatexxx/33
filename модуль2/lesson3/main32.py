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