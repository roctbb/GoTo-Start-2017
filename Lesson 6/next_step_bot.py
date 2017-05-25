import telebot

token = "338777500:AAGNxqdZU7GxBgoXRxSrhYfRPWnhs24EzIg"

bot = telebot.TeleBot(token)

def anek(message):
    if message.text.lower() == "да":
        bot.send_message(message.chat.id, "Купил мужик шляпу, а она ему как раз.")
    else:
        bot.send_message(message.chat.id, "Ну как хочешь :(")


@bot.message_handler(content_types=["text"])
def echo(message):
    if message.text.lower() == "привет":
        m = bot.send_message(message.chat.id, "Хочешь анек расскажу?")
        bot.register_next_step_handler(m, anek)

bot.polling(none_stop=True)

