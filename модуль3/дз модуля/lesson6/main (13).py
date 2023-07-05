# class Year:
#     def __init__(self):
#         self.__days = 365
#         self.__season = 'лето'
#
#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception(f'Вы передали некорректное значение, в году не может быть {days} дней.')

# class Year:
#     def __init__(self):
#         self.__days = 365
#         self.__season = 'лето'
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, value):
#         if value == 365 or value == 366:
#             self.__days = value
#         else:
#             raise ValueError(f'Вы передали некорректное значение, в году не может быть {value} дней.')


#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         for sym in name:
#             if sym.isdigit():
#                 raise Exception('Имя недопустимо, так как содержит цифры')
#
#         self.__name = name
#
#     @name.deleter
#     def del_name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, name):
#         if name < 0:
#             raise ValueError('Возраст не может быть отрицательным')
#         self.__age = name
#
#     @age.deleter
#     def del_age(self):
#         del self.__age
#
#
# person = Person('Валера', 16)
# del person.name
# del person.age
# #
#


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if any(char.isdigit() for char in value):
#             raise ValueError('Имя недопустимо, так как содержит цифры')
#         self.__name = value
#
#     @name.deleter
#     def del_name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError('Возраст не может быть отрицательным')
#         self.__age = value
#
#     @age.deleter
#     def del_age(self):
#         del self.__age
#
#
# person = Person('Валера', 16)
# print(person.name)
# person.name = 'Гриша'
# print(person.name)
# del person.name
# del person.age


# class Year:
#     def __init__(self, days, season):
#         self.days = days
#         self.__season = season
#
#     @property
#     def get_days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         for sym in days:
#             if sym.isdigit():
#                 raise Exception('Имя недопустимо, так как содержит цифры')
#
#         self.__days = days
#
#
# year = Year('Валера', 16)
# print(year.days)
# year.days = 'Гриша'
# print(year.days)


# class Spisok(list):
#     def delete_last_item(self):
#         self.remove(self[-1])
#
# my_l = Spisok()
# my_l.append(1)
# my_l.append(2)
#
# my_l.delete_last_item()
# print(my_l)





# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if any(char.isdigit() for char in value):
#             raise ValueError('Имя недопустимо, так как содержит цифры')
#         self.__name = value
#
#     @name.deleter
#     def del_name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError('Возраст не может быть отрицательным')
#         self.__age = value
#
#     @age.deleter
#     def del_age(self):
#         del self.__age
#
#
# person = Person('Валера', 16)
# del person.name
# del person.age


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        for sym in name:
            if sym.isdigit():
                raise Exception('Имя недопустимо, так как содержит цифры')
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @name.deleter
    def name(self):
        del self.__name


person = Person('Валера', 16)
print(person.name)
person.name = 'Гриша'
print(person.name)

del person.name
print(person.age)





