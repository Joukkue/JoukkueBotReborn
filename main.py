from telegram.ext import Updater, CommandHandler, run_async, MessageHandler, filters
import logging
import requests
from src.quotes import readquote, listquotes, addquote
from secrets import DEVELOP_BOT_TOKEN
from word_lists import beer, spruit
from src.utils import check_message, start

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

URL_BASE = 'http://127.0.0.1:8000/'

COMMANDLIST = [
    ('quote', readquote),
    ('listquotes', listquotes),
    ('addquote', addquote),
    ('start', start)
]
'''
Add your command to the commandlist
First parameter is the way the command is called
Second parameter is the command itself
'''

@run_async
def check_message_handler(update, context):
    check_message(update, context)


def main():
    updater = Updater(DEVELOP_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    for command in COMMANDLIST:
        dp.add_handler(CommandHandler(command[0], command[1]))
    dp.add_handler(MessageHandler(filters.Filters.all, check_message_handler))
    print("started")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
