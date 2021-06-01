import telepot
import time
import sys
import json
from pprint import pprint
from ReqOvff import search_ovff
from telepot.loop import MessageLoop

def handle(msg):
    pprint(msg)
    chat_id = msg['chat']['id']
    output = search_ovff(msg['text'])
    
    s = ''
    print(output)
    for t in output:
        
        s += t + '\n'
    
    bot.sendMessage(chat_id, s)

if __name__ == '__main__':
    
    with open ('Token.json', 'r') as json_file:
        data = json.load(json_file)
    
    bot = telepot.Bot(data['token'])
    
    MessageLoop(bot, handle).run_as_thread()
    print("I'm listening...")
    
    while 1:
        time.sleep(5)

    