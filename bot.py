import telebot

TOKEN = "7824101335:AAGMt4kuiyPHoVdz15ePLZEmTQAn0IVSCmM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to this bot")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "You can Contact alpha.heist on Instagram")

@bot.message_handler(func=lambda messages: True)
def calc(message):
    try:
        ans = eval(message.text)
        bot.reply_to(message, ans)
    except:
        bot.reply_to(message, "invalid input")


bot.polling()
