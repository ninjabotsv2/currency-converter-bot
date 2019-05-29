import logging
import os

from telegram.ext import Updater

from bot import set_handlers, TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

if __name__ == '__main__':
    # create an updater and get the dispatcher
    updater = Updater(TOKEN)
    dp = set_handlers(updater)

    # local running
    if os.environ.get('LOCAL', True):
        updater.start_polling()

    # set webhook
    else:
        appname = os.environ.get('APPNAME')
        port = int(os.environ.get('PORT', 8443))

        updater.start_webhook(listen="0.0.0.0",
                              port=port,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{0}/{1}".format(appname, TOKEN))

    updater.idle()
