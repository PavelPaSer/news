import telebot
from telebot import TeleBot
from telebot import types

bot = TeleBot('5780442128:AAF70GEKfTsMzpsvL0mPCwf99d2hEjes9c4')


@bot.message_handler(commands=['Загрузить']) 
def file_start(message):
    bot.send_message(message.chat.id,
                     text=('Инструкция для загрузки: \n'
                           ' - Укажите данные в формате: ФИО, номер, комментарий. '
                           ' - Обязательно разделять запятыми. '
                           ' - Информация будет добавлена в конец справочника.\n'
                           '\n'
                           'Если готовы отправьте файл.'))


@bot.message_handler(commands=['Прочитать'])
def read_file(message):
    bot.send_message(message.chat.id,
                     text=read_file())


@bot.message_handler(commands=['Добавить'])
def edit_one_line(message: telebot.types.Message):
    next_message = bot.send_message(chat_id=message.from_user.id, text='Инструкция: \nУкажите через запятую: ФИО, номер, комментарий:' )
    bot.register_next_step_handler(callback=new_data_one, message=next_message)
    bot.send_message(chat_id=message.from_user.id, text='Введите данные')


def new_data_one(message):
    new_file(1, message.text)



@bot.message_handler(content_types=['document'])
def import_file(message: telebot.types.Message):
    file = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open('import_file.txt', "wb") as f_out:
        f_out.write(downloaded_file)
    import_file()
    #bot.send_message(chat_id=message.from_user.id, text='Готово')


@bot.message_handler(commands=['Выгрузить'])
def bot_export_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Файл готов')
    bot.send_document(chat_id=msg.from_user.id, document=open('list.txt', 'rb'))



# импорт
def import_file():
    with open("import_file.txt", "r", encoding="utf-8") as file:
        data = file.read()
    export_file = open("list.txt", "a")
    export_file.write(data)
    export_file.close()

# просмотр
def read_file():
    with open("list.txt", "r", encoding='UTF-8') as file:
        data = file.read()
        return data

# добавить
def new_file(lot, data_file):
    if lot == 1:
        with open("list.txt", "a", encoding='UTF-8') as file:
            file.write(f'\n{data_file}')
    else:
        data = data_file.split(", ")
        with open("list.txt", "a", encoding='UTF-8') as file:
            file.write(f'\n{data[0]}, ')
        with open("list.txt", "a", encoding='UTF-8') as file:
            file.write(f'\n{data[1]}, ')
        with open("list.txt", "a", encoding='UTF-8') as file:
            file.write(f'\n{data[2]}, ')
            file.write('\n')


@bot.message_handler(commands=['start'])
def main_menu(message):
    markup = types.ReplyKeyboardMarkup()
    star_file = types.KeyboardButton('/Загрузить')
    read_files = types.KeyboardButton('/Прочитать')
    exsport_file = types.KeyboardButton('/Добавить')
    import_file = types.KeyboardButton('/Выгрузить')
    markup.add(star_file, read_files, exsport_file, import_file)
    bot.send_message(message.chat.id, 'Телефонный справочник ООО "Ромашка".\n Выберете нужную кнопку', reply_markup=markup)


bot.polling()