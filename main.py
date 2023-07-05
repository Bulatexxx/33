# name = "Иван"
#
# salary = 200_000
#
# print('y' + name + 'зарплата равна' + str(salary))
#
# print(f'Y {name} Зарпата равна {salary}')
#       print(Y' {name}' зарплата равна {salary1}'.format



# employee = {'name': 'Иван', 'salary': 200_000, 'on_vacation': False}
# print(f'У {employee.get("name")} зарплата равна {employee.get("salary")}')
# on_vacation = "в отпуске" if employee.get("On_vacatoin")

# employees_list = [
#     {
#         'name': 'Данил',
#         'salary': 250_000,
#     },
#     {
#         'name': 'Алина',
#         'salary': 250_000,
#
#     },
#     {
#         'name': 'Андрей',
#         'salary': 225_000,
#
#     }
#
# ]
# for employee in employees_list:
#     print(f'У {employee.get("name")} зарплата равна {employee.get("salary")}')



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f'У {self.name} зарплата равна {self.salary}')


employee1 = Employee('Danil', 250_000)
employee2 = Employee('Alina', 250_000)
employee3 = Employee('Andrew', 220_000)

my_list = []

my_list.append(employee1)
my_list.append(employee2)
my_list.append(employee3)

for employee in my_list:
    employee.info()


my_list.remove(employee3)
print(my_list)