import logging
import os

from telegram.ext import ConversationHandler, CommandHandler, Filters, MessageHandler

logger = logging.getLogger("bot.handlers.commands")


def log_command(func):
    def wrapper(bot, update):
        logger.info(f'User with id:{update.message.from_user.id} just entered command {update.message.text}')
        result = func(bot, update)
        return result

    return wrapper


@log_command
def handle_start(bot, update):
    try:
        update.message.reply_text(f'Hi, {update.message.from_user.first_name}! Read /help')
    except Exception as e:
        update.message.reply_text(f'Hi! Read /help')


@log_command
def handle_help(bot, update):
    update.message.reply_markdown(
        f"Type in two currencies with a separator (to, ->, >, -, etc.):\n"
        f"`10 eur to usd`.\n\n"
        f"You can omit the amount of money, so you will get just a currency rate:\n"
        f"`USD -> EUR`\n\n"
        f"Click on /support to ask a real human for a question."
    )


SUPPORT = range(1)


def get_support_handler():
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('support', _handle_support)],

        states={
            SUPPORT: [
                MessageHandler(Filters.text, _send_support_message),
            ],
        },

        fallbacks=[
            CommandHandler('cancel', _cancel_support),
        ],
    )

    return conversation_handler


@log_command
def _handle_support(bot, update):
    update.message.reply_text('Enter the message that you want to send to support.\n\n'
                              'Click /cancel if you want to finish.')
    return SUPPORT


def _send_support_message(bot, update):
    support_id = os.environ.get('SUPPORT_ID')

    try:
        text = update.message.text
        bot.send_message(
            support_id,
            f"[User](tg://user?id={update.message.from_user.id}) send a message:\n\n{text}",
            parse_mode='markdown'
        )
    except Exception as e:
        return SUPPORT

    return ConversationHandler.END


@log_command
def _cancel_support(bot, update):
    update.message.reply_text('You have cancelled your action.')
    return ConversationHandler.END
