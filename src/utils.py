import time

from telegram.ext import run_async
import requests

from word_lists import beer, spruit

URL_BASE = 'http://127.0.0.1:8000/'
global START_TIME
START_TIME = time.time()


def tissit(chat, message):
    if "tissit" in message:
        chat.send_photo(photo=open('media/koirakuva-6.jpg', 'rb'))


def tuli(chat, message):
    if any(word in message for word in spruit):
        chat.send_message(text="spruit")


def olut(chat, message):
    if any(word in message for word in beer):
        chat.send_message(text="Sanoiko joku kaljaa?")

@run_async
def check_message(update, context):
    chat = update.effective_chat
    message = update.message.text
    tuli(chat, message)
    olut(chat, message)
    tissit(chat, message)
    data = {
        'username': update.effective_user.username,
        'userid': update.effective_user.id,
        'chatid': update.effective_chat.id,
        'chatname': update.effective_chat.title,
    }
    requests.post(URL_BASE + 'api/update', data)


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def uptime(update, context):
    chat = update.effective_chat
    r_t_hours = (time.time() - START_TIME) // 3600
    r_t_minutes = (time.time() - START_TIME) % 3600 / 60
    r_t_seconds = (time.time() - START_TIME) % 3600 % 60
    msg = ""
    if r_t_hours >= 1:
        msg = "{:.0f}h {:.0f}min".format(r_t_hours, r_t_minutes,)
    elif r_t_minutes >= 1:
        msg = "{:.0f}min {:.0f}seconds".format(r_t_minutes, r_t_seconds)
    else:
        msg = "{:.2f} seconds".format(r_t_seconds)
    chat.send_message(text=msg)

