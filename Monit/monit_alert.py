#!/usr/bin/python3
# -*- coding: utf-8 -*- #
import os
import logging
from telegram.bot import Bot
from telegram.error import NetworkError, TelegramError

# Monit alert bot info
BOT_TOKEN = ''
CHAT_ID = ''

def send_alert(token, chatid, message):
    """
    Send Telegram alert message
    """

    try:
        bot = Bot(token=token)
        bot.send_message(chat_id=chatid, parse_mode='HTML', text='{0}'.format(message))
        logging.info("Alert successfully sent via Telegram.")
    except (NetworkError, TelegramError) as tg_err:
        logging.error("Unable to send alert, Telegram exception: %s", tg_err)


def main():
    
    message = "Nginx was reloaded"
    send_alert(BOT_TOKEN, CHAT_ID, message)


if __name__ == '__main__':
    main()
