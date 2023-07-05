from tkinter import *
import random
window = Tk(
)

window.geometry("600x600")


class Dust:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-dust-2396941.png').subsample(4,4)


class Clay:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-pottery-7942410.png').subsample(4,4)


class Steam:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\aroma.png').subsample(4,4)

    def __add__(self, other):
        pass


class Wind:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\wind.png').subsample(4,4)

    def __add__(self, other):
        pass


class Earth:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\ground.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust()
        elif isinstance(other, Water):
            return Clay()


class Water:
    mage = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-water-drop-4246703.png').subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Wind):
            return Steam()
        elif isinstance(other, Earth):
            return Clay()


class Fire:
    image = PhotoImage(file=r'C:\Users\Булат\PycharmProjects\код0\модуль3\lesson7\free-icon-fire-9509865.png').subsample(4,4)

    def __add__(self, other):
        pass


canvas = Canvas(width=600, height=600)
canvas.pack()
elements = [Earth(), Water(), Wind(), Fire()]
for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)

def move(event):
    print('vi kliknyli na okno')



window.mainloop()
