import os
from dotenv import load_dotenv
import telebot
import requests


load_dotenv()
BASE_URL = "http://localhost:3333"

API_KEY = os.getenv('API_KEY')
# print(API_KEY)

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet', 'greet'])
def greet(message):
    print(f"Format: {'{:.2f}'.format(None)}")
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    print("Message From ", first_name, type(message))
    # bot.reply_to(message, "Salam dari Binjai!")
    bot.send_message(message.chat.id, "Salaaaam dari Binjai!!")


@bot.message_handler(commands=['Level', 'level'])
def level(message):
    print(message.text)
    msgSplit = message.text.split()
    if (len(msgSplit) == 0):
        bot.send_message(message.chat.id, "Argumen Kosong Gan")
        return

    level = msgSplit[1]

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive",
            'Content-Type': 'application/json',
            'accept': 'application/json',
        }
        r = requests.get(BASE_URL+"/bot-level?level="+level, headers=headers)
        res = r.json()
        print(r.status_code, type(r.text), type(res), res)
        msg = f"*** Level {level} ***\n\n"

        for i in range(len(res['data'])):
            cur = res['data'][i]

            hargaidr = '{:.2f}'.format(
                float(cur['hargaidr'])) if cur['hargaidr'] is not None else None
            hargausdt = '{:.2f}'.format(
                float(cur['hargausdt'])) if cur['hargausdt'] is not None else None
            volumeidr = '{:.2f}'.format(
                float(cur['volumeidr'])) if cur['volumeidr'] is not None else None
            volumeusdt = '{:.2f}'.format(
                float(cur['volumeusdt'])) if cur['volumeusdt'] is not None else None
            lastbuy = '{:.2f}'.format(
                float(cur['lastbuy'])) if cur['lastbuy'] is not None else None
            lastsell = '{:.2f}'.format(
                float(cur['lastsell'])) if cur['lastsell'] is not None else None
            jumlah = '{:.2f}'.format(
                float(cur['jumlah'])) if cur['jumlah'] is not None else None

            print(
                {'hargaidr': hargaidr,
                 'hargausdt': hargausdt,
                 'volumeidr': volumeidr,
                 'volumeusdt': volumeusdt,
                 'lastbuy': lastbuy,
                 'lastsell': lastsell,
                 'jumlah': jumlah}
            )
            msg += (
                f"Periode ***{cur['periode']}***\n"
                f"___Harga IDR (Sum)___: {hargaidr}\n"
                f"___Harga USDT (Sum)___: {hargausdt}\n"
                f"___Volume IDR (Sum)___: {volumeidr}\n"
                f"___Volume USDT (Sum)___: {volumeusdt}\n"
                f"___Last Buy (Sum)___: {lastbuy}\n"
                f"___Last Sell (Sum)___: {lastsell}\n"
                f"___Jumlah (Count)___: {jumlah}\n\n"
            )

        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    except Exception as e:
        print(f"Error gan {e}")
        bot.send_message(message.chat.id, e)


@bot.message_handler(commands=['Jenis', 'jenis'])
def level(message):
    print(message.text)
    msgSplit = message.text.split()
    if (len(msgSplit) == 0):
        bot.send_message(message.chat.id, "Argumen Kosong Gan")
        return

    jenis = msgSplit[1]

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive",
            'Content-Type': 'application/json',
            'accept': 'application/json',
        }
        r = requests.get(BASE_URL+"/bot-jenis?jenis="+jenis, headers=headers)
        res = r.json()
        print(r.status_code, type(r.text), type(res), res)
        msg = f"*** Jenis {jenis} ***\n\n"

        for i in range(len(res['data'])):
            cur = res['data'][i]

            hargaidr = '{:.2f}'.format(
                float(cur['hargaidr'])) if cur['hargaidr'] is not None else None
            hargausdt = '{:.2f}'.format(
                float(cur['hargausdt'])) if cur['hargausdt'] is not None else None
            volumeidr = '{:.2f}'.format(
                float(cur['volumeidr'])) if cur['volumeidr'] is not None else None
            volumeusdt = '{:.2f}'.format(
                float(cur['volumeusdt'])) if cur['volumeusdt'] is not None else None
            lastbuy = '{:.2f}'.format(
                float(cur['lastbuy'])) if cur['lastbuy'] is not None else None
            lastsell = '{:.2f}'.format(
                float(cur['lastsell'])) if cur['lastsell'] is not None else None
            jumlah = '{:.2f}'.format(
                float(cur['jumlah'])) if cur['jumlah'] is not None else None

            print(
                {'hargaidr': hargaidr,
                 'hargausdt': hargausdt,
                 'volumeidr': volumeidr,
                 'volumeusdt': volumeusdt,
                 'lastbuy': lastbuy,
                 'lastsell': lastsell,
                 'jumlah': jumlah}
            )
            msg += (
                f"Periode ***{cur['periode']}***\n"
                f"___Harga IDR (Sum)___: {hargaidr}\n"
                f"___Harga USDT (Sum)___: {hargausdt}\n"
                f"___Volume IDR (Sum)___: {volumeidr}\n"
                f"___Volume USDT (Sum)___: {volumeusdt}\n"
                f"___Last Buy (Sum)___: {lastbuy}\n"
                f"___Last Sell (Sum)___: {lastsell}\n"
                f"___Jumlah (Count)___: {jumlah}\n\n"
            )

        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    except Exception as e:
        print(f"Error gan {e}")
        bot.send_message(message.chat.id, e)


bot.polling()
print("Server Running and start Polling")
