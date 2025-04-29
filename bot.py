
import telebot

TOKEN = "7824101335:AAGMt4kuiyPHoVdz15ePLZEmTQAn0IVSCmM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to this bot! Send your YouTube video link")
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "You can Contact alpha.heist on Instagram")
@bot.message_handler(func=lambda message: "hello" in message.text or "hi" in message.text)
def hey_hello(message):
    bot.reply_to(message, "Hi hello chodo ye batao tum ho kaun")

bot.polling()
