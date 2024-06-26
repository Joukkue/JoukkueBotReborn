import time

import requests

from word_lists import beer, spruit

URL_BASE = 'http://127.0.0.1:8000/'
global START_TIME
START_TIME = time.time()


async def tissit(chat, message):
    if "tissit" in message:
        await chat.send_photo(photo=open('media/koirakuva-6.jpg', 'rb'))


async def tuli(chat, message):
    if any(word in message for word in spruit):
        await chat.send_message(text="spruit")


async def olut(chat, message):
    if any(word in message for word in beer):
        await chat.send_message(text="Sanoiko joku kaljaa?")


async def check_text_message(update, context):
    chat = update.effective_chat
    if update.message:
        message = update.message.text
        message_low = message.lower()
        await tuli(chat, message_low)
        await olut(chat, message_low)
        await tissit(chat, message_low)
    elif update.edited_message:
        updated_message = update.edited_message.text
        message_low = updated_message.lower()
        await tuli(chat, message_low)
        await olut(chat, message_low)
        await tissit(chat, message_low)
    data = {
        'username': update.effective_user.username,
        'userid': update.effective_user.id,
        'chatid': update.effective_chat.id,
        'chatname': update.effective_chat.title,
    }
    try:
        requests.post(URL_BASE + 'api/update', data)
    except:
        print("Couldn't connect to backend")


async def check_message(update, context):
    data = {
        'username': update.effective_user.username,
        'userid': update.effective_user.id,
        'chatid': update.effective_chat.id,
        'chatname': update.effective_chat.title,
    }
    try:
        requests.post(URL_BASE + 'api/update', data)
    except:
        print("Couldn't connect to backend")


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


async def uptime(update, context):
    chat = update.effective_chat
    r_t_hours = (time.time() - START_TIME) // 3600
    r_t_minutes = (time.time() - START_TIME) % 3600 / 60
    r_t_seconds = (time.time() - START_TIME) % 3600 % 60
    r_t_days = r_t_hours // 24
    if r_t_days >= 1:
        msg = "{:.0f}d {:.0f}h".format(r_t_days, r_t_hours,)
    elif r_t_hours >= 1:
        msg = "{:.0f}h {:.0f}min".format(r_t_hours, r_t_minutes,)
    elif r_t_minutes >= 1:
        msg = "{:.0f}min {:.0f}seconds".format(r_t_minutes, r_t_seconds)
    else:
        msg = "{:.2f} seconds".format(r_t_seconds)
    await chat.send_message(text=msg)

