import telebot
tb = telebot.AsyncTeleBot(token='543196227:AAE4nTGtYYlBdsSXdR817_6hjYynyF7yt4Q')
bot = telebot.TeleBot(token='477042082:AAEBDDi0BizL-RnrRH7tzHyaEDlIjcwL4N8')
@tb.message_handler(commands=['start'])
def aio(msg):
    tb.reply_to(msg, 'async1')
@bot.message_handler(commands=['help'])
def aoi(msg):
    bot.reply_to(msg, 'async2')
((tb)and(bot)).polling(none_stop=True)