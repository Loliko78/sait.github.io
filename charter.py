import telebot
import sqlite3
import main
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random


bot = telebot.TeleBot('7739855756:AAEawsXWjZpCyYEMm68nR9weB2RQlQvXa7U')

connection = sqlite3.connect('min.db')
cursor = connection.cursor()
cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS Users (
        id TEXT,
        money TEXT,
        photo TEXT PRIMARY KEY,
        art TEXT,
        kat TEXT,
        ch TEXT
        )''')
connection.commit()

@bot.message_handler(commands=['start'])
def start(m):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Открыть маркет", url='t.me/CLMARKETBot/market_in_telegram'))
    bot.send_message(m.chat.id, text=f"Привет, чтобы добавить товар или услугу напиши /add\nЧтобы удалить свой товар напиши /delete", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def add(m):
    if m.text == '/add':
        bot.send_message(m.chat.id, 'Начнем добавление вашего товара или услуги!')
        bot.send_message(m.chat.id, 'Отправте название товара/услуги и описание')
        bot.register_next_step_handler(m,n)
    elif m.text =='/delete':
        bot.send_message(m.chat.id, 'Отправь описание товара/услуги который нужно удалить.')
        
        bot.register_next_step_handler(m, dl)
    elif m.text == '/delete_a' and m.chat.id == 564049757:
        bot.send_message(m.chat.id, 'Отправь описание товара/услуги который нужно удалить.')
        bot.register_next_step_handler(m, d)

def d(m):
    conn = sqlite3.connect("min.db")
    cursor= conn.cursor()
    cursor.execute('DELETE FROM Users WHERE (money) = (?) ', (m.text))    
    conn.commit()
    conn.close()
    bot.send_message(m.chat.id, 'Успешно удалено.')
def dl(m):
    
    conn = sqlite3.connect("min.db")
    cursor= conn.cursor()
    cursor.execute('DELETE FROM Users WHERE (id, money) = (?,?) ', (m.from_user.username, m.text))    
    conn.commit()
    conn.close()
    bot.send_message(m.chat.id, 'Успешно удалено.')
        
def n(m):
    global opis
    opis = m.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Одежда")
    btn2 = types.KeyboardButton("Игры")
    btn3 = types.KeyboardButton("ПК")
    btn5 = types.KeyboardButton("Другое")
    btn4 = types.KeyboardButton("Услуги")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(m.chat.id, 'Выберете категорию товара/услуги.', reply_markup=markup)
    bot.register_next_step_handler(m,kar)  
def kar(m):
    global kat
    kat = m.text
    bot.send_message(m.chat.id, 'Отправте цену на ваш товар/услугу(СИМВОЛЫ $₽ ВПИСЫВАЙТЕ В СООБЩЕНИЕ).')
    bot.register_next_step_handler(m,gh)
def gh(m):
    global cg
    cg = m.text
    bot.send_message(m.chat.id, 'Отправте фото товара/услуги.')
    bot.register_next_step_handler(m,b)
def b(m):
    import os
    global opis
    global kat
    global cg
    connection = sqlite3.connect('min.db')
    cursor = connection.cursor()
    photo_info = m.photo[-1]  # Получаем самую большую версию фото (обычно последний элемент списка) 

    # Получаем путь к файлу фотографии 
    file_id = photo_info.file_id 
    file_path = bot.get_file(file_id).file_path 

    # Загружаем фото из Telegram в текущую директорию 
    downloaded_file = bot.download_file(file_path) 

    # Определите, в какой папке вы хотите сохранить фотографии 
    save_path = 'static'
    file_name = f'{file_id}.png' 
    # Сохраняем фотографию в указанную папку 
    with open(os.path.join(save_path, file_name), 'wb') as new_file: 
        new_file.write(downloaded_file)
    try:
        art = str(random.randint(1, 9999999))
        cursor.execute(f'INSERT INTO Users (id, money, photo, art, kat, ch) VALUES (?, ?, ?, ?,?,?)', (f"{m.from_user.username}", opis, file_name, art, kat, cg))
        connection.commit()
        bot.send_message(m.chat.id, f'Товар/услуга добавлен.\nЕго артикул: {art}\nКатегория: {kat}')
    except:
        bot.send_message(m.chat.id, 'Товар с таки фото уже существует.')


main.start()
bot.infinity_polling()
