import asyncio
from telethon import TelegramClient, events
from os import remove, getenv, walk, path
from dotenv import load_dotenv
import PyPDF2 as pd
import re,  time
from telethon import errors

load_dotenv()
# Remember to use your own values from my.telegram.org!
# Credentials while logging...
API_ID = int(getenv('api_id'))
API_HASH = getenv('api_hash')


MY_CHAT_ID = int(getenv('my_channel_id'))
MY_CHAT_ID2 = int(getenv('my_channel_id2'))
PD_CHAT_ID = getenv('pd_chat_id')

client = TelegramClient('anon', API_ID, API_HASH)

#Capturing messages from the targetted Telegram Channel


@client.on(events.NewMessage(chats=PD_CHAT_ID))
async def handler(event):
 try:
            await event.download_media(file=open(event.file.name, "wb"))
            pdf_mgmt(event.file.name)
            await asyncio.wait([ 
                client.send_file(MY_CHAT_ID,file= open(event.file.name, 'rb'), thumb='thumb.jpg'),
                client.send_file(MY_CHAT_ID2,file= open(event.file.name, 'rb'), thumb='thumb.jpg'),
            ])
          

        
            remove(event.file.name)

        

 except errors.FloodWaitError as e:
    print('Have to sleep', e.seconds, 'seconds')
    time.sleep(e.seconds)


def pdf_mgmt (f_name) :
    
    pattern = 'DAILY NEWSPAPERS PDF'
    dir_path = path.dirname(path.abspath(__file__))
    
    #renaming pdfs
    for root, dirs, files in walk(dir_path):
        for file in files: 
            
            if file.startswith('TH') or file.startswith('IE'):
                
                merger = pd.PdfFileMerger( strict=True)
                merger.append(pd.PdfFileReader(path.join(root,'promo.pdf')))
                merger.append(pd.PdfFileReader(path.join(root,f_name)))
                
                merger.write(f_name)
                merger.close()
                
    #getting no. of pages for pdfs
                infile = pd.PdfFileReader(path.join(root,f_name))
                numPages = infile.getNumPages()
                delPages = []

                for i in range(0, numPages):
                    pageObj = infile.getPage(i)
                    ex_text = pageObj.extractText()
                    if re.search(pattern, ex_text):
                        # print(f'Pattern found on Page no: {i}')
                        delPages.append(i)
                #deleting required pages and uploading to telegram...
                if len(delPages) > 0 :
                    infile = pd.PdfFileReader(path.join(root,f_name))
                    output = pd.PdfFileWriter()
                    
                    for i in range(infile.getNumPages()):
                        if i not in delPages:
                            p = infile.getPage(i)
                            output.addPage(p)

                    with open(path.join(root,f_name),'wb') as f:
                        output.write(f)
                
client.start()
#this will make your bot run forever untill any interruption
client.run_until_disconnected()