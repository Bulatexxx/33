from course import get_currency, today
from tkinter import *

window = Tk()
window.geometry("500x500")

image_logo = PhotoImage(file=r"C:\Users\Булат\PycharmProjects\код0\lesson8\logo.png")
label_logo = Label(window, image=image_logo)
label_logo.place(x=0, y=0)

label_title = Label(window, text="ЦБРФ", font="TimesNewRoman 36")
label_title(x=230, y=50)

label_currencies = Label(window, text=f"Курс на {today:}", font="TimesNewRoman 20")
label_currencies.place(x=50, y=160)


currency_info = get_currency("R01010")
currency_info_str = f"{currency_info.get('name')} {dollar_info.get('value')}"

label_currency = Label(window, text=dollar_ifo_str, font="TimesNewRoman 16")
label_currency.place(x=50, y=210)
euro_ifo = get_currency("R01239")
euro_info_str = f"{euro_info.get('name')} {euro_info_str, font="TimesNewRoman 16"}"
euro_label.place(x=50, y=240)
entry = Entry(font="TimesNewRoman 16")
entry.place(x=50, y=400)
def search():
    currency_id = entry.get()
    currency_info = get_currency(currency_id)
    currency_info_str = f"window"


button = Button(text="Найти", font="TimesNewRoman 16", command=search)
button.place(x=235, y=390)

window.mainloop()