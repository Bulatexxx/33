from telebot import TeleBot
from telebot.types import Message
from utils import welcome_keyboard, get_random_photo, BASE_FILES_PATH, poem_keyboard

bot = TeleBot("5880824665:AAHr4ffrNXbN-9FYpyPARtQW0hKT4iYmY08")


@bot.message_handler(commands=["start", "help"])
def welcome(message: Message):
    keyboard = welcome_keyboard()
    bot.send_message(message.from_user.id, "Привет, выбери один из вариантов:", reply_markup=keyboard)


@bot.message_handler(commands=["cats"])
def cats(message: Message):
    random_img = get_random_photo()
    bot.send_photo(message.from_user.id, random_img)


@bot.message_handler(commands=["music"])
def music(message: Message):
    audio = open(fr"{BASE_FILES_PATH}\happy.mp3", "rb")
    bot.send_audio(message.from_user.id, audio)


@bot.message_handler(commands=["poem"])
def poem(message: Message):
    keyboard = poem_keyboard()
    bot.send_message(message.from_user.id, "Села муха на варенье, вот и всё стихотворенье", reply_markup=keyboard)


@bot.message_handler(commands=["sticker"])
def sticker(message: Message):
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEHKQRjuXt6gDhZUV8c0C6cRRcyR_6DqgACQBkAApb2AAFIS6_0BkxQ5NEtBA")

