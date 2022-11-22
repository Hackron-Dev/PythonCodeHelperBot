import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from config import TOKEN

vk_session = vk_api.VkApi(token=TOKEN)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text
        print(request)

        if request.lower() == "привет":
            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет!', 'random_id': 0})
        elif request.lower() == "пока":
            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Пока!', 'random_id': 0})
        else:
            vk_session.method('messages.send',
                              {'user_id': event.user_id, 'message': 'Не понял вашего ответа!', 'random_id': 0})
