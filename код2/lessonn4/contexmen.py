# file = open('test.text', 'w')
# file.write('веб по компьютерному менеджменту')
# file.close()
#
#
# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.write('вею по компьтерному менеджменту')
# import contextlib
#
#
# @contextlib.contextmanager
# def reverse_str(string):
#     yield string[::-1]
#
#
#
# with reverse_str('hello') as reversed_string:
#     print(reversed_string)
import contextlib


@contextlib.contextmanager
def exc_handler(exc):
    try:
        yield
    except exc:
        print("ошибка, но мне пофик")

my_list = [1, 2]
my_dict = {1: 1}
with exc_handler(IndexError, AttributeError, KeyError):
    print(my_list.asd)
    my_list[4]
    my_dict[2]

print('Еще какой-то текст...')