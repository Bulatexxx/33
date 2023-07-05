# import time

# my_list = [time.sleep(x) for i in range(1,3)]
# my_list = (time.sleep(x) for x in range(1, 3))
# for sleep in my_list:
#     print(sleep)


# def my_lazy_func(items):
#     yield from items
#
# for items in my_lazy_func([1,2,3, 3, 4, 5]):
#     print(items)
sum = 0
pos_count = 0
neg_count = 0

while True:
    num = int(input())
    if num == 0:
        break
    sum += num
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1

print(sum, pos_count - neg_count)




