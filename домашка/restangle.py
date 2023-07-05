# from tkinter import *
#
# window = Tk
# window.geometry("800x600")
#
#
# canvas = Canvas(window, width=800, height=600, bg="white")  # создание холста
# canvas.pack()  # прилепили холст на окно
#
# canvas.create_rectangle(200, 200, 400, 400, fill='red', outline='blue')
# canvas.create_polygon(200, 200, 300, 100, 400, 200, fill='pink')
# canvas.create_rectangle(400, 500, 500, 400, fill='cyan', outline='blue')
# canvas.create_rectangle(200, 400, 100, 500, fill='green', outline='black')


# canvas = Canvas(window, width=800, height=600, bg="white") # создание холста
# canvas.pack() # прилепили холст на окно
#
# canvas.create_rectangle(200, 200, 400, 400, fill='red', outline='blue')
# canvas.create_polygon(200, 200, 300, 100, 400, 200, fill='pink')
# canvas.create_rectangle(400, 500, 500, 400, fill='cyan', outline='blue')
# canvas.create_rectangle(200, 400, 100, 500, fill='green', outline='black')

# window.mainloop()




# from tkinter import *
# #
# #
# class House(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.master.title("Прямоугольники и треугольники")
#         self.pack(fill=BOTH, expand=True)
#
#         # Создаю объект для рисования (Canvas) по рамке (self)
#         c = Canvas(self)
#         # Создаю 3 треугольника. Толщина линии - 2 пикселя
#         c.create_line(10, 10, 100, 100, 150, 50, 10, 10,
#                       fill="#1f1", width=2)
#         c.create_line(150, 10, 150, 100, 180, 200, 150, 10,
#                       fill="#2e2", width=2)
#         c.create_line(250, 110, 350, 150, 280, 200, 250, 110,
#                       fill="#2e2", width=2)
#
#         # Рисую 2 прямоугольника.
#         c.create_rectangle(230, 10, 290, 60,
#                            outline="#f11", fill="#1f1", width=2)
#         c.create_rectangle(20, 110, 90, 160,
#                            outline="#f11", fill="#1f1", width=2)
#         # Размещаю нарисованное на всё окно
#         c.pack(fill=BOTH, expand=True)
#
#     # Создаю главное окно
#
#
# w = Tk()
# # Создаю изображение, которое описано выше
# f = Image()
#
# # Устанавливаю размер основного окна
# w.geometry("400x250")
# # Запускаю главный цикл обработки событий
# w.mainloop()

from tkinter import *
window = Tk()
window.geometry("800x600")
class Racet(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Ракета")
        self.pack(fill=red, expand=True)
        canvas = Canvas(self)
        canvas.create_rectangle(200, 200, 400, 400, fill='red', outline='blue')
        canvas.create_polygon(200, 200, 300, 100, 400, 200, fill='pink')
        canvas.create_rectangle(400, 500, 500, 400, fill='cyan', outline='blue')
        canvas.create_rectangle(200, 400, 100, 500, fill='green', outline='black')
        canvas.pack(fill=red, expand=True)


V = Racet()
window.mainloop()