import telepot
import time
import sys
from pprint import pprint
from ReqOvff import search_ovff
from telepot.loop import MessageLoop

bot = telepot.Bot('1788200432:AAGRjgv5f98swon8CUiWK6FmFLkfDpcTGtA')

def handle(msg):
    pprint(msg)
    chat_id = msg['chat']['id']
    output = search_ovff(msg['text'])
    
    s = ''
    print(output)
    for t in output:
        
        s += t + '\n'
    
    bot.sendMessage(chat_id, s)



MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while 1:
    time.sleep(5)

    