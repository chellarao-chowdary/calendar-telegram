#!/usr/bin/python3

import logging

from telegram.ext import Updater,CallbackQueryHandler,CommandHandler
from telegram import  ReplyKeyboardRemove,ParseMode

import telegramcalendar

# Go to botfather and create a bot and copy the token and paste it here in token
TOKEN = "" # token of the bot


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update,context):
    context.bot.send_message(chat_id=update.message.chat_id,text="Hey {}! I am calender bot \n \n Please type /calendar to view my power".format(update.message.from_user.first_name),parse_mode=ParseMode.HTML)

# A simple command to display the calender
def calendar_handler(update,context):
    update.message.reply_text(text="Please select a date: ",
                    reply_markup=telegramcalendar.create_calendar())
    

def inline_handler(update,context):
    selected,date = telegramcalendar.process_calendar_selection(update,context)
    if selected:
        context.bot.send_message(chat_id=update.callback_query.from_user.id,
                        text="You selected %s" % (date.strftime("%d/%m/%Y")),
                        reply_markup=ReplyKeyboardRemove())


if TOKEN == "":
    print("Please write TOKEN into file")
else:
    updater = Updater(TOKEN,use_context=True)
    dp=updater.dispatcher


    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("calendar",calendar_handler))
    dp.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()
