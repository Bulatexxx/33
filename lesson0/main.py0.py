# questions = [
#     {'question': 'Кто из героев Киновселенной Marvel начал знакомство с Землёй, попав под грузовик?',
#     'answers': ['Фил Колсон', 'Халк', 'Капитан Америка', 'Правильного ответа нет'],
#     'right_answer': 4},
#
#     {'question': 'Как звучит полное имя младшего брата Тора?',
#     'answers': ['Локи Одинсон', 'Локи Эриксон', 'Локи Лафейсон', 'Правильного ответа нет'],
#     'right_answer': 3},
#
#     {'question': 'Какой суперзлодей отличился тем, что за очень короткое время собрал в ангаре сотни управляемых дронов для армии США?',
#     'answers': ['Иван Ванко', 'Альтрон', 'Танос', 'Правильного ответа нет'],
#     'right_answer': 1}
# ]
# name = input("Как вас зовут? ")
# points = 0
#
# for i_question in questions:
#     text = i_question.get("question")
#     answers = i_question.get("answers")
#     number_of_answer = 1
#     print(text)
#     for i_answer in answers:
#         print(number_of_answer, i_answer)
#         number_of_answer += 1
#
#     user_answer = int(input("Введите правильный ответ: "))
#     right_answer = i_question.get("right_answer")
#
#     if user_answer == right_answer:
#         print("Верно!")
#         points += 1
#     else:
#         print("Не верно!")
#
#
# test_result_file = open("test.txt", "w", encoding="utf-8")
# test_result_file.write(name + " " + str(points))
# test_result_file.close()
#
# # def summa(a, b):
# #     return a + b
# #
# #
# # result = summa(100, 50)
# # print(result)
#
# def discriminant(a, b, c):
#     return b * b - 4 * a * c
#
# result = discriminant(9, 18, 7)
# print(result)
# def calc(a,b, operand):
#     if operand == '+':
#         res = a + b
#     elif operand == '-':
#         res = a - b
#     elif operand == '*':
#         res = a * b
#     elif operand == '/':
#         res = a / b
#     else:
#         res = 'Извините, но такой операции нет в калькуляторе.'
#     return res
#
# num1 = int(input('Введите число:'))
# num2 = int(input('Введите число:'))
# opel = input('введите операцию:')
# toga= calc(num1, num2, opel)
# print(toga)

