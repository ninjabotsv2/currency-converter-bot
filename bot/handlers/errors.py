import logging

logger = logging.getLogger("bot.handlers.errors")


def handle_error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
