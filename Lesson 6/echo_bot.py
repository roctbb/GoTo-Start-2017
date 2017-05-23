import telebot

token = "381907090:AAGjkL5xD9pT9503MWS9sh-e8K_N9nW2sAw"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    result = message.text[::-1]
    bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)

