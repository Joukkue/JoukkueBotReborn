from telegram.ext import Updater, CommandHandler, run_async, MessageHandler, filters
import logging
import requests

from word_lists import beer, spruit

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

URL_BASE = 'http://127.0.0.1:8000/'


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


@run_async
def addquote(update, context):
    check_message(update, context)
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


@run_async
def readquote(update, context):
    check_message(update, context)
    chat = update.effective_chat
    try:
        tag = update.message.text.split(' ', 1)[1]
        response = requests.get(URL_BASE + 'api/quotes/' + tag).json()
        chat.send_message(text=response['message'])
    except IndexError:
        chat.send_message(text="Please provide a tag")


@run_async
def listquotes(update, context):
    check_message(update, context)
    chat = update.effective_chat
    try:
        response = requests.get(URL_BASE + 'api/quotes').json()
        chat.send_message(text=response['message'])
    except IndexError:
        chat.send_message(text="Please provide a tag")


@run_async
def check_message_handler(update, context):
    check_message(update, context)


def koira(update, context):
    chat = update.effective_chat.send_photo(photo=open('koirakuva-6.jpg', 'rb'))


@run_async
def check_message(update, context):
    chat = update.effective_chat
    message = update.message.text
    if any(word in message for word in spruit):
        chat.send_message(text="spruit")

    if any(word in message for word in beer):
        chat.send_message(text="Sanoiko joku kaljaa?")
    data = {
        'username': update.effective_user.username,
        'userid': update.effective_user.id,
        'chatid': update.effective_chat.id,
        'chatname': update.effective_chat.title,
    }
    requests.post(URL_BASE + 'api/update', data)


def main():
    updater = Updater('344427823:AAEuGoOkLJ_bMa-WVhPg7Toephtt_f8y91M', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('addquote', addquote))
    dp.add_handler(CommandHandler('quote', readquote))
    dp.add_handler(CommandHandler('listquotes', listquotes))
    dp.add_handler(CommandHandler('koira', koira))
    dp.add_handler(MessageHandler(filters.Filters.all, check_message))
    print("started")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
