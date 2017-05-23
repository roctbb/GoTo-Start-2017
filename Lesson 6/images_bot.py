import uuid
import telebot
from PIL import Image

token = "381907090:AAGjkL5xD9pT9503MWS9sh-e8K_N9nW2sAw"

bot = telebot.TeleBot(token)

def process(filename):
    image = Image.open(filename)
    image = image.rotate(90)
    image.save(filename)

@bot.message_handler(content_types=["photo"])
def save(message):
    file_id = message.photo[-1].file_id

    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)

    extn = '.' + str(path.file_path).split('.')[-1]

    cname = str(uuid.uuid4()) + extn
    with open('images/' + cname, 'wb') as new_file:
        new_file.write(downloaded_file)

    process('images/' + cname)

    with open('images/' + cname, 'rb') as new_file:
        bot.send_photo(message.chat.id, new_file.read())


bot.polling(none_stop=True)

