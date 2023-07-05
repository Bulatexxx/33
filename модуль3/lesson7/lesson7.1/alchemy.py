from tkinter import *
import random

window = Tk()
window.geometry("600x600")


class Steam:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\aroma.png').subsample(4, 4)

    def __add__(self, other):
        pass


class Dust:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-dust-2396941.png').subsample(4, 4)


class Clay:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-pottery-7942410.png').subsample(4, 4)


class Wind:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust()


class Earth:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\ground.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Clay()


class Fire:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-fire-9509865.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()


class Water:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-water-drop-4246703.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()


canvas = Canvas(width=600, height=600)
canvas.pack()

elements = [Earth(), Water(), Wind(), Fire()]
for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)


def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        image_id_1, image_id_2 = images_ids[0], images_ids[1]

        elem_1 = elements[image_id_1 - 1]
        elem_2 = elements[image_id_2 - 1]

        new_elem = elem_1 + elem_2
        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)

    canvas.coords(images_ids, event.x, event.y)


class Item:
    def __init__(self, name, price, image, weight):
        self.name = name
        self.price = price
        self.image = image
        self.weight = weight

    def __sub__(self, other):
        return Item(f'{self.name} - {other.name}', self.price - other.price, self.image, self.weight - other.weight)

    def __mul__(self, other):
        return Item(f'{self.name} x {other.name}', self.price * other.price, self.image, self.weight * other.weight)

    def __truediv__(self, other):
        return Item(f'{self.name} / {other.name}', self.price / other.price, self.image, self.weight / other.weight)


aroma = Steam()
dust = Dust()
clay = Clay()

item1 = Item('Item1', 10, aroma.image, 20)
item2 = Item('Item2', 5, dust.image, 15)
item3 = Item('Item3', 15, clay.image, 10)

item4 = item1 - item2
item5 = item2 * item3
item6 = item3 / item1

print(item4.name, item4.price, item4.weight)
print(item5.name, item5.price, item5.weight)
print(item6.name, item6.price, item6.weight)


window.bind('<B1-Motion>', move)

window.mainloop()
