import logging

logger = logging.getLogger("bot.handlers.text")


def handle_text(bot, update):
    # TODO: add currency conversion

    if update.message:
        update.message.reply_text('Please, read /help.')
