import telebot
from telebot import types

bot = telebot.TeleBot('%ваш токен%')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    iin_num = input("Enter your IIN:")

    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('a')
    itembtnv = types.KeyboardButton('v')
    itembtnc = types.KeyboardButton('c')
    itembtnd = types.KeyboardButton('d')
    
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd)
    tb.send_message(chat_id, "Choose your candidate:", reply_markup=markup)