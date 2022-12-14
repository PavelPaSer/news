from telebot import TeleBot
import telebot
from telebot import types
import logger as log

bot = TeleBot('5657665886:AAHjVPkc3y90Y-Bm2WO7K8TQSZdQ7-FhAY8')
value = ''
old_value = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton('C', callback_data='c'),
                telebot.types.InlineKeyboardButton('<=', callback_data='<='),
                telebot.types.InlineKeyboardButton('+', callback_data='+'),
                telebot.types.InlineKeyboardButton('/', callback_data='/') )

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data='9'),
                telebot.types.InlineKeyboardButton('*', callback_data='*') )

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data='6'),
                telebot.types.InlineKeyboardButton('-', callback_data='-') )

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data='3'),
                telebot.types.InlineKeyboardButton('c0plex', callback_data='complex') )

keyboard.row(   telebot.types.InlineKeyboardButton('j', callback_data='j'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data='.'),
                telebot.types.InlineKeyboardButton('rational', callback_data='rational') )


@bot.message_handler(commands=['Запустить'])

def getMessage(message):
    log.loger(f'Пользователь {message.from_user.first_name} начал пользоваться калькулятором')
    bot.send_message(message.chat.id,
                     text=('Инструкция для работы с рациональными и комплексными числами: \n'
                           ' - Рациональные. Пример: "2+2" после нажимаете "rational"\n'
                           ' - Комплексные. Пример: "10+8j/2-2j" после нажимаете "c0plex"\n'))
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data 

    if data =='c':
        log.loger(f'Пользователь {query.from_user.first_name} удалил все введеные числа')
        value = ''
    elif data == '<=':
        log.loger(f'Пользователь {query.from_user.first_name} удалил последнию цыфру введенного числа')
        if value != '':
            value = value[:len(value)-1]
    elif data == 'rational':
        log.loger(f'Пользователь {query.from_user.first_name} выбрал рациональные числа')
        try:
            value = float( eval(value) )
        except:
            log.loger(f'Ошибка! Пользователь {query.from_user.first_name} произвел деление на ноль, при использование "rational"')
            value = 'Ошибка!'

    elif data == 'complex':
        log.loger(f'Пользователь {query.from_user.first_name} выбрал комплексные числа')
        try:
            value = complex( eval(value) )
        except:
            log.loger(f'Ошибка! Пользователь {query.from_user.first_name} произвел деление на ноль при использование "complex"')
            value = 'Ошибка!'
    else:
        value += data
 

    
    if (value != old_value and value != '') or (value != old_value and value == '') :
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0', reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value, reply_markup=keyboard)
            old_value = value 

    if value == 'ошибка': value = ''
    
@bot.message_handler(commands=['start'])
def main_menu(message):
    log.loger(f'Пользователь {message.from_user.first_name} добавил бота')
    markup = types.ReplyKeyboardMarkup()
    read_files = types.KeyboardButton('/Запустить')
    reads_start = types.KeyboardButton('/start')
    markup.add(read_files, reads_start)
    bot.send_message(message.chat.id, 'Здравствуйте.\n'
                                    'Калькулятор для рациональных и комплексных чисел.\n'
                                    'Запустите калькулятор.\n', reply_markup=markup)


bot.polling(none_stop=True)