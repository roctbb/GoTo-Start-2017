import time
import vk

token = "959baace8aefa7c8278304ad2d96da52cf98140773f24cca290d157288ae662e3b3375f14d26b1fa75450"



session = vk.Session(access_token=token)
api = vk.API(session)
last_message_id = 0
while True:
    messages = api.messages.get(count=100, v=5.65, last_message_id=last_message_id)
    if messages["items"]!=[]:
        last_message_id = messages["items"][0]["id"]
    for message in messages["items"]:
        api.messages.send(user_id=message['user_id'], message='сам такой!', forward_messages=str(message['id']))
    time.sleep(10)

    print(messages)