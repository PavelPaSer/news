# from telebot import TeleBot
# import telebot
# from telebot import types

# bot = TeleBot('5419643455:AAEWwlB39V0oQsTGmVRP8JT7iw-JD2S36b4')


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("/рациональные")
#     btn2 = types.KeyboardButton("/комплексные")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я калькулятор!"
#                                            "Пожалуйста, выберите числа, с которыми будете работать".format(message.from_user), reply_markup=markup)

# @bot.message_handler(commands=["рациональные"])
# def handle_text(msg: telebot.types.Message):
#         bot.send_message(msg.chat.id, text="Введите 2 числа и действие между ними")
#         bot.register_next_step_handler(callback=viev_rac_num, message=msg)

# def viev_rac_num(msg: telebot.types.Message):
#         bot.send_message(chat_id=msg.from_user.id, text=rac_num(msg.text))

# def rac_num(text):
#     try:
#         res = 0
#         if "+" in text:
#             lst = text.split('+')
#             res = float(lst[0])+float(lst[1])
#             return res
#         elif "-" in text:
#             lst = text.split('-')
#             res = float(lst[0])-float(lst[1])
#             return res
#         elif "*" in text:
#             lst = text.split('*')
#             res = float(lst[0])*float(lst[1])
#             return res
#         elif "/" in text:
#             lst = text.split('/')
#             res = float(lst[0])/float(lst[1])
#             return res
#         else:
#             res = 'Вы ввели не то, Введите два числа и между ними действие, например: 2*3'
#             return res
#     except:
#         res = 'Я не понимаю запятых, поменяйте пожалуйста  на точки, и могу решать одно действие'
#         return res

# @bot.message_handler(commands=["комплексные"])
# def handle_text(msg: telebot.types.Message):
#         bot.send_message(msg.chat.id, text="Введите 2 комплексных числа,"
#                                            " например: 10+8j / 2-2j (с пробелом между ними)")
#         bot.register_next_step_handler(callback=viev_rac_num2, message=msg)

# def viev_rac_num2(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id,  text=complex_num(msg.text))

# def complex_num(text):
#     res = None
#     lst = text.split()
#     if lst[1] == '-':
#         res = complex(lst[0]) - complex(lst[2])
#         return str(res)
#     elif lst[1] == '+':
#         res = complex(lst[0]) + complex(lst[2])
#         return str(res)
#     elif lst[1] == '/':
#         res = complex(lst[0]) / complex(lst[2])
#         return str(res)
#     elif lst[1] == '*':
#         res = complex(lst[0]) * complex(lst[2])
#         return str(res)
#     else:
#         print('Неверный ввод')
# @bot.message_handler()
# def error(msg: telebot.types.Message): 
#     bot.send_message(msg.from_user.id, "Я могу выполнять только одно действие, сделайте свой выбор заново")

# bot.polling(none_stop=True)