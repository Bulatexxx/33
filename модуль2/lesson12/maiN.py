from tkinter import *
import time


window = Tk()
window.geometry("500x400")
window.resizable(width=False, height=False)

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.x = 1
        self.y = 1

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        position = self.canvas.coards(self.oval)
        if position[0] <= 0:
            self.x = -self.x

        if position[2] > 500:
            self.y = -self.x

        if position[1] > 400:
            self.y = -self.y

        if position[3] > 400:
            self.y = -self.y


class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(200, 200, 300, 230, fill=color)
        self.x = 300

    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        position = self.canvas.coords(self.oval)





canvas = Canvas(window, width=500, height=400)
canvas.pack()
ball = Ball(canvas=canvas, color="red")

window.bind("Key-Left", platform.left)




while True:
    ball.draw()
    window.update()
    time.sleep(0.001)

