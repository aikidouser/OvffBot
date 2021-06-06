#%%
import sys
import json
import logging
import telegram
from pprint import pprint
from ReqOvff import search_ovff
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

#%%
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

#%%
def start_command(update: Update, _: CallbackContext):
    
    re_msg = '先來嘗試輸人個中文字吧'
    update.message.reply_text(re_msg)

#%%
def help_command(update: Update, _: CallbackContext):
    
    bot.send_chat_action
    re_msg = '此機器人是來嘸蝦米查碼的喔\n僅只援繁體中文'
    update.message.reply_text(re_msg)

#%%
def call_ovff(update: Update, _: CallbackContext):
    
    # 會顯示chatbot正在輸入中，增加對話真實感
    bot.send_chat_action(chat_id = update.message.chat_id, action = telegram.ChatAction.TYPING) 
    
    if len(update.message.text) < 6:
        re_msg = search_ovff(update.message.text)
    else:
        update.message.reply_text('也太長')
        return
    
    if re_msg:
        update.message.reply_text(re_msg)
    
    # empty means that the msg is non Chinese
    else:
        update.message.reply_text('只可以輸入中文喔')

#%%
def msg_except(update: Update, _: CallbackContext):
    
    re_msg = '不要玩我'
    update.message.reply_text(re_msg)

#%% 
if __name__ == '__main__':
    
    with open ('Token.json', 'r') as json_file:
        data = json.load(json_file)
    TOKEN = data['token']
    
    updater = Updater(TOKEN)
    bot = telegram.Bot(token = TOKEN)
    dispatcher = updater.dispatcher
    
    # command
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help_command))
    
    # input word to search
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, call_ovff))
    
    # else
    dispatcher.add_handler(MessageHandler(~Filters.text & ~Filters.command, msg_except))
    updater.start_polling()
    
    updater.idle()