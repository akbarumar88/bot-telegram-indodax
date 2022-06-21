import os
from dotenv import load_dotenv
import telebot

load_dotenv()

API_KEY = os.getenv('API_KEY')
# print(API_KEY)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet', 'greet'])
def greet(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    print("Message From ", first_name, type(message))
    # bot.reply_to(message, "Salam dari Binjai!")
    bot.send_message(message.chat.id, "Salaaaam dari Binjai!!")


bot.polling()
