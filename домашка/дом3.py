from tkinter import *


class Image(Frame):
    def __init__(self):
        # Инициализирую предка этого класса
        Frame.__init__(self)
        # Устанавливаю заголовок окна
        self.master.title("Прямоугольники и треугольники")
        # Размещаю на всё окно рамку
        self.pack(fill=BOTH, expand=True)

        # Создаю объект для рисования (Canvas) по рамке (self)
        c = Canvas(self)
        # Создаю 3 треугольника. Толщина линии - 2 пикселя
        c.create_line(10, 10, 100, 100, 150, 50, 10, 10,
                      fill="#1f1", width=2)
        c.create_line(150, 10, 150, 100, 180, 200, 150, 10,
                      fill="#2e2", width=2)
        c.create_line(250, 110, 350, 150, 280, 200, 250, 110,
                      fill="#2e2", width=2)

        # Рисую 2 прямоугольника.
        c.create_rectangle(230, 10, 290, 60,
                           outline="#f11", fill="#1f1", width=2)
        c.create_rectangle(20, 110, 90, 160,
                           outline="#f11", fill="#1f1", width=2)
        # Размещаю нарисованное на всё окно
        c.pack(fill=BOTH, expand=True)

    # Создаю главное окно


w = Tk()
# Создаю изображение, которое описано выше
f = Image()

# Устанавливаю размер основного окна
w.geometry("400x250")
# Запускаю главный цикл обработки событий
w.mainloop()






from tkinter import *

window = Tk()
window.geometry("800x600")

canvas = Canvas(window, width=800, height=600, bg="white")  # создание холста
canvas.pack()  # прилепили холст на окно


class House:
    def __init__(self, square, count_of_floors, color_of_walls, color_of_triangle):
        self.square = square
        self.count_of_floors = count_of_floors
        self.color_of_walls = color_of_walls
        self.color_of_triangle = color_of_triangle
    def title(self):
        print("Прямоугольники и треугольники")

    def __str__(self):
        return f"Дом площадью {self.square}, кол-во этажей {self.count_of_floors}, цвет дома: {self.color}"

    def print_info(self):
        print(f"Дом площадью {self.square}, кол-во этажей {self.count_of_floors}, цвет дома: {self.color}")

    def do_something(self):
        pass

    def build_house(self):
        canvas.create_rectangle(200, 200, 400, 400, fill=self.color_of_walls, outline="red")
        canvas.create_polygon(200, 200, 300, 150, 400, 200, fill=self.color_of_triangle)


house = House(200, 10, 'red', 'orange')
house.build_house()
house2 = House(300, 15, 'green', 'blue')
house2.build_house()