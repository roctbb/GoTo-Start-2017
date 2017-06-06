import time
import vk

token = "959baace8aefa7c8278304ad2d96da52cf98140773f24cca290d157288ae662e3b3375f14d26b1fa75450"

service_token = "2feef6c285d89838e0f23489f6a0ebb93d4ae9660e5544b25b9cc72dd8b5067ac1fa72ccd56b5164b3ba1"

session = vk.Session(access_token=token)
api = vk.API(session)

session2 = vk.Session(access_token=service_token)
api2 = vk.API(session2)

with open("last.txt", 'r') as file:
    last_message_id = int(file.read())

while True:
    messages = api.messages.get(count=100, v=5.65, last_message_id=last_message_id)
    if messages["items"]!=[]:
        last_message_id = messages["items"][0]["id"]
    with open("last.txt", 'w') as file:
        file.write(str(last_message_id))
    for message in messages["items"]:
        text = message["body"]
        if text!='':
            result = api2.wall.search(domain="baneks", count=100, query=text, v=5.65)
            if result["count"]!=0:
                anek_text = result["items"][-1]["text"]
                api.messages.send(user_id=message['user_id'], message=anek_text)


    print(messages)
    time.sleep(10)