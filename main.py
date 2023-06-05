from telegram.ext import CommandHandler, MessageHandler, filters, Application
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


async def check_text_message_handler(update, context):
    await check_text_message(update, context)


async def check_message_handler(update, context):
    await check_message(update, context)


def main():
    application = Application.builder().token(DEVELOP_BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT, check_text_message_handler))
    application.add_handler(MessageHandler(filters.ALL, check_message_handler), group=1)

    for command in COMMANDLIST:
        application.add_handler(CommandHandler(command[0], command[1]), group=2)

    print("Started")
    application.run_polling()



if __name__ == '__main__':
    main()
