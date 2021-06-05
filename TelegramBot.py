import telepot
import time
import sys
import json
from pprint import pprint
from ReqOvff import search_ovff
from telepot.loop import MessageLoop
from telepot.exception import TelegramError

def handle(msg):
    #pprint(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        
        if msg['text'] == '/help':
            re_msg = '此機器人是來嘸蝦米查碼的喔\n僅只援繁體中文'
            bot.sendMessage(chat_id, re_msg)
            return
        
        output = search_ovff(msg['text'])
    
    else:
        re_msg = '不要玩我'
        bot.sendMessage(chat_id, re_msg)
        return
    
    s = ''
    #print(output)
    for t in output:    
        s += t + '\n'
    
    try:
        bot.sendMessage(chat_id, s)
    
    except TelegramError:
        re_msg = '只可以輸入中文喔'
        bot.sendMessage(chat_id, re_msg)
    
if __name__ == '__main__':
    
    with open ('Token.json', 'r') as json_file:
        data = json.load(json_file)
    
    bot = telepot.Bot(data['token'])
    
    MessageLoop(bot, handle).run_as_thread()
    print("I'm listening...")
    
    while 1:
        time.sleep(5)

    