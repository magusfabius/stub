# DOCUMENTATION
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Types-Of-Handlers


# commandhandler -> messages with bot commands
# messagehandler -> for all mesages


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import time

from uuid import uuid4

# logging module, so you will know when (and why) things don't work as expected:
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



# telegram CONSTANTS
BOT_TOKEN = "1959604620:AAEdTCS9az7woTg5e8XOne26bd3Lww3z9uU"




url_requested = "https://www.sciencenewsforstudents.org/wp-content/uploads/2021/08/LL_AI_feat-1030x580.jpg"

# get url from request
def get_url():
    contents = requests.get(url_requested).json()    
    url = contents['url']
    return url

def send_photo(bot, update):
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url_requested)

def start_callback(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text("You said: " + user_says)
    update.message.reply_text("Welcome to my awesome bot!")

def help_callback(update, context):
    help_request = " ".join(context.args)
    # TODO: elaboration of the input request, download pytorch

def answer_callback(update, context):
    print(update.message)
    print(update.edited_message)
    print(update.channel_post)
    print(update.edited_channel_post)



def add_user_activity(update, context):
    user_action = context.args
    start_time = time.time()


    context.user_data["activity"] = new_activity_list
    print(user_action, start_time)

# ACT methodology with a bot
def add_negative_emotion(update, context):
    update.message.reply_text("Take 3 deep breaths with me and embrace the emotion")
    # breath sound
    update.message.reply_text("Brief description of negative emotion ...")
    update.message.reply_text("Give a name to this emotion ... ")

    # METADATA
    update.message.reply_text("Where are you?")
    update.message.reply_text("What were you doing?")
    update.message.reply_text("Extra notes")



def main():
    print("hello")
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    #dp.add_handler(CommandHandler('bop', send_photo))
    dispatcher.add_handler(CommandHandler("start", start_callback))
    dispatcher.add_handler(CommandHandler("activity", add_user_activity))


    dispatcher.add_handler(MessageHandler(Filters.all, answer_callback))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()


