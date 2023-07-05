# squares = []
# for i in range(1000001):
#     squares.append(i ** 2)
#
#
#
# squares = [i ** 2 for i in range(1000001)]
#
#
# assert squares[0] == 0
# assert squares[1] == 1
# assert squares[2] == 4
# assert squares[4] == 16



#
# class Year:
#     def.init
#     def get_days(self):
#         return self._days
#
#     def get_days(self,days):
#         if days == 365 or days == 366:
#             self._days = days
#         else:
#             raise Exception("vi peredali nekkorectnoe znachenie, v gody ne mochet buit {days} дней")
#
#
# year = Year()
# print(year.get_days())
# year.get.days(364)
# print(year.get_days())

# class Person:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         for sym in name:
#             if sym.isdigit():
#                 raise Exception('ima nedostypno')
#
#         self.__name = name
#
#
# person = Person('Valera', 16)
# print(person.name)
# person.name = 'Grisha'
# print(person.name)


class CustomList:
    def init(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def delete_last_item(self):
        if len(self.items) > 0:
            self.items.pop()

    def len(self):
        return len(self.items)

    def getitem(self, index):
        return self.items[index]

    def setitem(self, index, value):
        self.items[index] = value

    def delitem(self, index):
        del self.items[index]

    def repr(self):
        return repr(self.items)


custom_list = CustomList()
custom_list.append(1)
custom_list.append(2)
custom_list.append(3)
print(custom_list)