
import telebot
from currency_converter import CurrencyConverter
from telebot import types
bot = telebot.TeleBot('7343036423:AAHnR36ycdGVBftj_FrPQpOPycHMGzDDt6o')
currency = CurrencyConverter()
amount = 0

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'salom {message.from_user.first_name}  summani kiritng ')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "kiritilgan son noto'g'ri" )
        bot.register_next_step_handler(message, summa)
        return


    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
    btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
    btn3 = types.InlineKeyboardButton('USD/RUBL', callback_data='usd/rubl')
    btn4 = types.InlineKeyboardButton('другое назначение', callback_data='другое назначение')

    markup.add(btn1,btn2,btn3,btn4)
    bot.send_message(message.chat.id,'valyutani kiriting', reply_markup=markup)







bot.polling(non_stop=True)














