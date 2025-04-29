import telebot

TOKEN = "7824101335:AAGMt4kuiyPHoVdz15ePLZEmTQAn0IVSCmM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to this bot!")

bot.polling()
