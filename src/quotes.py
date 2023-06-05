import logging
import requests
from src.utils import check_message


URL_BASE = 'http://127.0.0.1:8000/'


async def addquote(update, context):
    await check_message(update, context)
    chat = update.effective_chat
    try:
        quote = update.message.reply_to_message.text
        tag = update.message.text.split(' ', 1)[1]
        data = {'userid': update.effective_user.id, 'tag': tag, 'quote': quote}
        response = requests.post(URL_BASE + 'api/addquote', data).json()
        chat.send_message(text=response['message'])
    except AttributeError:
        chat.send_message(text="Please provide a quote")
    except IndexError:
        chat.send_message(text="Please provide a tag")
    except Exception as err:
        logging.log(err)


async def readquote(update, context):
    await check_message(update, context)
    chat = update.effective_chat
    try:
        tag = update.message.text.split(' ', 1)[1]
        response = requests.get(URL_BASE + 'api/quotes/' + tag).json()
    except IndexError:
        response = requests.get(URL_BASE + 'api/quotes/random').json()

    chat.send_message(text=response['message'])


async def listquotes(update, context):
    await check_message(update, context)
    chat = update.effective_chat
    try:
        response = requests.get(URL_BASE + 'api/quotes').json()
        chat.send_message(text=response['message'])
    except IndexError:
        chat.send_message(text="Please provide a tag")

