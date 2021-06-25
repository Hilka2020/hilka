import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

def write_msg(chat_id, message):
    vk.method('messages.send', {'chat_id': chat_id, 
                                'message': message, 'random_id':get_random_id()
                                })
def chat_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':get_random_id()})

#Ввод ответов, которые рандомно выдаёт бот
a1 = ['Привет' ]
a2 = ['Пока!']
a3 = ['Я такой)']
a4 = ['Русский включи']
a5 = ['Хорошо. У тебя как?']
a6 = ['Общаюсь с тобой']
a7 = ['Ну вот и отлично.']
a8 = ['Досвидос']

# API-ключ, созданный ранее
token = "74f968a27ee48d8bfbab31a279dc3586570575dde3e73dcbe408661b50ac083d0e22bd60e00601c9aaa54"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
 # Работа с сообщениями
longpoll = VkLongPoll(vk)
print("Бот запущен")
# Основной цикл

while True:
    for event in longpoll.listen():
        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:
            # Если оно имеет метку для меня( то есть бота)
            if event.to_me:
                # Сообщение от пользователя
                request = event.text
                # Каменная логика ответа
                if request in ("Привет",'привет',):
                    chat_msg(event.user_id, random.choice(a1))  
                elif request in ('Молодец бот', 'молодец бот'):
                    chat_msg(event.user_id, random.choice(a3))
                elif request in ('Как дела?', 'как дела?'):
                    chat_msg(event.user_id, random.choice(a5))
                elif request in ('Что делаешь?', 'что делаешь?'):
                    chat_msg(event.user_id, random.choice(a6))
                elif request in ('Хорошо', 'хорошо', 'отлично', 'Отлично'):
                    chat_msg(event.user_id, random.choice(a7))
                elif request in ('Плохо', 'плохо','Неочень', 'неочень'):
                    chat_msg(event.user_id, random.choice(a8))
                elif request in ('Пока', 'пока'):
                    chat_msg(event.user_id, random.choice(a2))  
                elif request.split()[0] == "command":
                    chat_msg(event.user_id, commander.do(request[8::]))
                else:
                    chat_msg(event.user_id, random.choice(a4))