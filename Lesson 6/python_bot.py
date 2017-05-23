import telebot
from subprocess import call

token = "381907090:AAGjkL5xD9pT9503MWS9sh-e8K_N9nW2sAw"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Я умею выполнять код! Пришли мне его полностью!")

@bot.message_handler(content_types=["text"])
def echo(message):
    try:
        result = eval(message.text)
    except Exception as e:
        result = "Ошибка: "+str(e)

    bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)

