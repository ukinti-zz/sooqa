import telebot
bot = telebot.TeleBot(token='477042082:AAEBDDi0BizL-RnrRH7tzHyaEDlIjcwL4N8')
@bot.message_handler(commands=['help'])
def aoi(msg):
    bot.reply_to(msg, 'async2')
bot.polling(none_stop=True)
