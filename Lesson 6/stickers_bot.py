import telebot

token = "338777500:AAGNxqdZU7GxBgoXRxSrhYfRPWnhs24EzIg"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["sticker"])
def echo(message):
    sticker = message.sticker.file_id
    print(sticker)
    bot.send_sticker(message.chat.id, sticker)

bot.polling(none_stop=True)

