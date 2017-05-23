from threading import Thread

import telebot
from time import sleep

token = "381907090:AAGjkL5xD9pT9503MWS9sh-e8K_N9nW2sAw"

bot = telebot.TeleBot(token)

users = set()

@bot.message_handler(commands=["start"])
def start_spam(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=rdg4lkgsQ04")

@bot.message_handler(commands=["spam"])
def start_spam(message):
    users.add(message.chat.id)
    bot.send_message(message.chat.id, "Берем сироп вишневый")

@bot.message_handler(commands=["stop"])
def start_spam(message):
    users.remove(message.chat.id)
    bot.send_message(message.chat.id, "Ок, все.")


def update_messages():
    bot.polling(none_stop=True)

def send_spam():
    while True:
        for user in users:
            bot.send_message(user, "Затем сироп вишневый!")
        sleep(3)

polling = Thread(target=update_messages)
spamming = Thread(target=send_spam)

polling.start()
spamming.start()


