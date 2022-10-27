import telebot.types
from telebot import TeleBot 

# bot = TeleBot('5766227792:AAEo5-i-dLmqOQPlhSPZxFraRHbXNQ163vU')

# боту шлем два числа и он выводт сумму
"""
def summator(text):
    lst = text.split() #делим по пробелам
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit(): #если нулево элемент
        return str(int(lst[0]) + int(lst[1])) # str хорошо лучше чтоб возврашет в том в чем принимает
    return 'Это некорректный запрос'


@bot.message_handler() # @ улучает функцию, помечает функции что должна отрабавать сообщение
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text)) # chat_id=msg.from_user.id) - это кому отправляем сообщение, заметим сам текс(что мы ему пишем)

bot.polling() # когда придет письмо(запрос), тогда телеграм бот отправит на ваш сервер. Работает только с HTPSS. Нам нужен домен, белый ip или удаленный сервер. Нужно чтоб не менялся ip адрес. Статический
"""
# РАБОТА С ФАЙЛАМИ

"""
@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                    text='Log программы\nwdasdsadaw')
    bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))
"""

"""
import telebot.types
from telebot import TeleBot
 
 
bot = TeleBot('5472063097:AAF-3Y2QeK9OnkiQECdUdUxDC99mRzgU1q8')
 
 
def summator(text):
    lst = text.split()
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
        return str(int(lst[0]) + int(lst[1]))
    return 'Это некорректный запрос'
 
Отправить файл
@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Лог программы\newcoiywgecowegcouwefoyewfov')
    bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))
 

Скачать файл
@bot.message_handler(content_types=['document'])
def hello(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
 
 
@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Справка")
 
 
@bot.message_handler(commands=['summator'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=sum_items, message=msg)
 
 
def sum_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text))
 
 
@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Вы ввели:")
 
 
bot.polling()
 """



# ЗАДАНИЕ 1
"""
При помощи виртуального окружения и PIP реализовать решение задач с прошлых семинаров:
Напишите программу, удаляющую из текста все слова, содержащие "абв".
"""
from cgitb import text
import telebot.types
from telebot import TeleBot

bot = TeleBot('5766227792:AAEo5-i-dLmqOQPlhSPZxFraRHbXNQ163vU')

def delete_word(msg):
    return ' '.join([i for i in msg.split() if i.count('абв')])

@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=delete_word(msg.text))

bot.polling()


