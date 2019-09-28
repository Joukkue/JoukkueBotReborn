from telegram.ext import run_async
import requests

from word_lists import beer, spruit

URL_BASE = 'http://127.0.0.1:8000/'


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

