from telegram.ext import Updater, CommandHandler, run_async, MessageHandler, filters
import logging
from src.quotes import readquote, listquotes, addquote
from secrets import DEVELOP_BOT_TOKEN
from src.utils import check_text_message, start, uptime, check_message

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

URL_BASE = 'http://0.0.0.0:8000/'

COMMANDLIST = [
    ('readquote', readquote),
    ('listquotes', listquotes),
    ('insertquote', addquote),
    ('start', start),
    ('uptime', uptime),
]
'''
Add your command to the commandlist
First parameter is the way the command is called
Second parameter is the command itself
'''


@run_async
def check_text_message_handler(update, context):
    check_text_message(update, context)


@run_async
def check_message_handler(update, context):
    check_message(update, context)


def main():
    updater = Updater(DEVELOP_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    for command in COMMANDLIST:
        dp.add_handler(CommandHandler(command[0], command[1]))
    dp.add_handler(MessageHandler(filters.Filters.text, check_text_message_handler))
    dp.add_handler(MessageHandler(filters.Filters.all, check_message_handler))
    print("started")
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
