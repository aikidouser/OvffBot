#%%
import requests
import logging
from bs4 import BeautifulSoup

#%%
logger = logging.getLogger(__name__)

#%%
def full2half(s):
    
    n = list()

    for x in s:
        num = ord(x)
        if num == 0x3000:
            num = 32
        
        elif 0xFF01 <= num <= 0xFF5E:
            num -= 0xFEE0
            
        num = chr(num)
        n.append(num)
    n = ''.join(n)
        
    return n
    

#%%
def search_ovff(dest):
    final_out = list()
    basic_url = "https://boshiamy.com/liuquery.php?q="
    
    basic_url += dest
    
    #print(basic_url)
    
    responce = requests.get(basic_url)
    soup = BeautifulSoup(responce.text, "html.parser")
    
    tbody = list(soup.find("tbody").select("ul"))
    
    for i, text in enumerate(tbody):
        #print(dest[i])
        final_out.append(dest[i])
        for outs in text.select("li"):
            outs = outs.getText()
            outs = outs.split("　")[0]
            outs = full2half(outs)
            final_out.append(outs)
            #print(outs)
        
        if i != len(tbody) - 1:
            final_out.append('-------')
    
    msg = str()
    for out in final_out:
        msg += out + '\n'

    return msg
    
if __name__ == "__main__":
    
    dest = input()
    output = search_ovff(dest)
    
    print(output)
