

choice = input('Пожалуйста, выберите знак операции')

num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
elif choice == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
else:
    print('Пожалуйста, попробуйте снова!')



