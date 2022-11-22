import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from config import TOKEN

vk_session = vk_api.VkApi(token=TOKEN)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def sender(user_id, text):
    vk_session.method('messages.send', {'user_id': user_id, 'message': text, 'random_id': 0})


# TODO: Переделать структуру бота
def replies():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            user_id = event.user_id
            print(msg)
            if msg == 'привет':
                sender(user_id, 'и тебе тоже привет')
            elif msg == 'пока':
                sender(user_id, 'давай удачи')
            else:
                sender(user_id, 'ладно')


replies()
