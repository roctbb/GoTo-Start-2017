text = ""

with open('text.txt', 'r') as file:
    text = file.read()

lines = text.split("\n")
print(lines)

users = {}

import time
import vk

token = "959baace8aefa7c8278304ad2d96da52cf98140773f24cca290d157288ae662e3b3375f14d26b1fa75450"
session = vk.Session(access_token=token)
api = vk.API(session)
with open("last.txt", 'r') as file:
    last_message_id = int(file.read())
while True:
    messages = api.messages.get(count=100, v=5.65, last_message_id=last_message_id)
    if messages["items"] != []:
        last_message_id = messages["items"][0]["id"]
    with open("last.txt", 'w') as file:
        file.write(str(last_message_id))
    for message in messages["items"]:
        if message['user_id'] not in users.keys():
            users[message['user_id']] = -1;
        users[message['user_id']] = (users[message['user_id']] + 2) % len(lines)
        number = users[message['user_id']]
        api.messages.send(user_id=message['user_id'], message=lines[number])
    print(messages)
    time.sleep(10)
