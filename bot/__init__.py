import os

from telegram.ext import CommandHandler, MessageHandler, Filters

from bot.handlers.commands import handle_start, handle_help, get_support_handler
from bot.handlers.errors import handle_error
from bot.handlers.text import handle_text

TOKEN = os.environ.get('TOKEN')


def set_handlers(updater):
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(CommandHandler('start', handle_start))
    dispatcher.add_handler(CommandHandler('help', handle_help))

    # support handler will be here
    dispatcher.add_handler(get_support_handler())

    # other handlers
    dispatcher.add_handler(MessageHandler(Filters.text, handle_text))
    dispatcher.add_error_handler(handle_error)

    return dispatcher


