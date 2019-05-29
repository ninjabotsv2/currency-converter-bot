import logging

from bot.api import Converter

logger = logging.getLogger("bot.handlers.text")


def handle_text(bot, update):
    separators = [' -> ', ' to ', ' - ', ' > ', ' в ']
    separator = ' '
    text = update.message.text

    for s in separators:
        if s in text:
            separator = s

    data = text.rsplit(separator, 1)
    currency_from, currency_to = data
    amount = 1

    if len(data[0].split(' ')) > 1:
        data_splitted = data[0].split(' ')
        if len(data_splitted) > 2:
            update.message.reply_text('Please, read /help.')
            return

        amount, currency_from = data_splitted

    converter = Converter()
    result = converter.convert(currency_from, currency_to, amount=float(amount))

    if not result:
        update.message.reply_text("Couldn't convert your currencies. Try later.")

    else:
        update.message.reply_text(f"{amount} {currency_from.upper()} = {result:.2f} {currency_to.upper()}")
