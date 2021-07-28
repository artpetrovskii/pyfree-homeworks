import telebot
from random import choice

token = "1804558241:AAHoNaQAA-ykuqKqQf_fSnJV1eLmoXtpczE"

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список (название задачи запрашиваем у пользователя).
/show - напечатать все доюавленные задачи.
/random - добавить случайную задачу на дату Сегодня"""

todos = dict()

def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = ' '.join([tail])
    if len(task) < 3:
        bot.send_message(message.chat.id, 'Задачи должны быть больше 3х символов')
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')


@bot.message_handler(commands=['print'])
def print_(message):
    dates = message.text.split()[1].lower().split()
    response  = ''
    for date in dates:
        tasks = todos.get(date)
        response += f'{date}: \n'
        for task in tasks:
            response += f'[ ] {task}\n'
        response += '\n'
    bot.send_message(message.chat.id, response)


bot.polling(none_stop=True)
