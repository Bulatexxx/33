from tkinter import *
import random

window = Tk()
window.geometry("600x600")
canvas = Canvas(window, width=600, height=600)
canvas.pack()

background = PhotoImage(file=r"C:\Users\Булат\PycharmProjects\код0\lesson4\bg_2.png")


class Knight:
    def __init__(self):
        self.v = 0
        self.x = 150
        self.y = 350
        self.v_x = 0
        self.photo = PhotoImage(file=r"C:\Users\Булат\PycharmProjects\код0\lesson4\knight.png")

    def up(self, event):
        self.v = -3

    def down(self, event):
        self.v = 3

    def right(self, event):
        self.v_x = +3

    def left(self, event):
        self.v_x = -3

    def stop(self, event):
        self.v = 0
        self.v_x = 0




knight = Knight()


class Dragon:
    def __init__(self):
        self.x = random.randint(500, 600)
        self.y = random.randint(50, 550)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file=r"C:\Users\Булат\PycharmProjects\код0\lesson4\dragon.png")


dragons = []
for i in range(3):
    dragons.append(Dragon())


def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=background)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v
    knight.x += knight.v_x

    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        dragon.x -= dragon.v

        if ((dragon.x - knight.x) ** 2 + (dragon.y - knight.y) ** 2) ** 0.5 < 50:
            dragons.remove(dragon)
    if knight.y <= 52:
        knight.y = 53
    if knight.y >= 541:
        knight.y = 540
    if knight.x <= 51:
        knight.x = 50
    if knight.x >= 551:
        knight.x = 550
    window.after(10, game)



window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)
window.bind("<KeyRelease>", knight.stop)

game()
window.mainloop()
