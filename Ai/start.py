# DOCUMENTATION
# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Types-Of-Handlers


# commandhandler -> messages with bot commands
# messagehandler -> for all mesages


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re

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


# SE NON DAI IL MEGLIO NON TI TORNA IL MEGLIO
# 
life_points = 100
PUNISH_POINT = -2
REWARD_POINT = +2

UPDATE = ""
ACTION_TYPE = ""
CONTEXT = ""



class Action():
    action_type = 0 # 0 is string, 1 is somethung else

action = new Action(update, action_type, context)


def get_reward(update, context):
    life_points = life_points + REWARD_POINT

def wrong_move(update, context):
    life_points = life_points + PUNISH_POINT

def move(update, context):
    
    

import win32api, win32con
def click(x,y):p
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(10,10)











def main():
    print("hello")
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    #dp.add_handler(CommandHandler('bop', send_photo))
    dp.add_handler(CommandHandler("start", start_callback))

    dp.add_handler(MessageHandler(Filters.all, answer_callback))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()


