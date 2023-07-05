# name = "Иван"
# salary = 200_000

# print('У ' + name + ' зарплата равна ' + str(salary))
# print(f'У {name} зарплата равна {salary}')
#
# print('У {name1} зарплата равна {salary1}'.format(
#     name1=name,
#     salary1=salary
# ))

# employee = {'name': 'Иван', 'salary': 200_000, 'on_vacation': True}
# print(f'У {employee.get("name")} зарплата равна {employee.get("salary")}')
# on_vacation = "в отпуске " if employee.get('on_vacation') else 'на работе'
#
# print(on_vacation)

# employees_list = [
#     {
#         'name': 'Данил',
#         'salary': 200_000,
#     },
#
#     {
#         'name': 'Алина',
#         'salary': 250_000,
#     },
#
#     {
#         'name': 'Андрей',
#         'salary': 225_000,
#     }
#
# ]

# for employee in employees_list:
#     print(f'У {employee.get("name")} зарплата равна {employee.get("salary")}')

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def info(self):
#         print(f'У {self.name} зарплата равна {self.salary}')
#
#
# employee1 = Employee('Данил', 200_000)
# employee2 = Employee('Алина', 250_000)
# employee3 = Employee('Андрей', 225_000)
#
# my_list = []
#
# my_list.append(employee1)
# my_list.append(employee2)
# my_list.append(employee3)
#
# for employee in my_list:
#     employee.info()
#
# my_list.remove(employee3)
# print(my_list)


# class Employee:
#     def __init__(self, name, salary, on_vacation):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#
#     def info(self):
#         print(f'У {self.name} зарплата равна {self.salary}. Сейчас {"в отпуске" if self.on_vacation else "на работе"}')
#
#
# employee1 = Employee('Данил', 200_000, False)
# employee2 = Employee('Алина', 250_000, True)
# employee3 = Employee('Андрей', 225_000, False)
#
#
# my_list = []
# my_list.append(employee1)
# my_list.append(employee2)
# my_list.append(employee3)
#
# for employee in my_list:
#     employee.info()


# class Employee:
#
#     def __init__(self, name, salary, on_vacation):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#
#     def print_info(self):
#         print(
#             f"Employee {self.name} has salary of {self.salary} and is currently {'on vacation' if self.on_vacation else 'working'}")
#
#
# emp1 = Employee("John", 50000, False)
# emp2 = Employee("Alice", 60000, True)
#
# emp1.print_info()
# emp2.print_info()


class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee

    def info(self):
        print(f'У {self.name} зарплата равна {self.salary}. Сейчас {"в отпуске" if self.on_vacation else "на работе"}')

employees = [Employee('Данил', 200_000, False, True),
             Employee('Алина', 250_000, True, True),
             Employee('Андрей', 225_000, False, True),
             Employee('Федор', 280_000, False, True),
             Employee('Екатерина', 190_000, False, False)]

for employee in employees:
    if not employee.is_good_employee:
        print(f"Увольняем {employee.name}")
        employees.remove(employee)

print("Оставшиеся работники:")
for employee in employees:
    employee.info()