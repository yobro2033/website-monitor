import requests
from bs4 import BeautifulSoup
import difflib
import time
from datetime import datetime

url = "https://www.gucci.com/uk/en/pr/c/hot-wheels-x-gucci-cadillac-seville-replica-p-696473I312Z8464"
headers = {'User-Agent': 'Mozilla/5.0'}

hook = Webhook('https://discord.com/api/webhooks/658061206548119562/0k4VOMro53L3mCjFOTfgJgIYqeFvuBA6BAyC-Ol2exL9ijspMGf0hcJspKtP0at4h1he')

embed = Embed(
  description='Successfully created a VCC! Check your csv to get the cards number and CVC.',
  color=0x5CDBF0,
  timestamp='now'
  )

embed.add_field(name='RESTOCKED')
embed.add_field(name='Click this link', value='https://www.gucci.com/uk/en/pr/c/hot-wheels-x-gucci-cadillac-seville-replica-p-696473I312Z8464')

PrevVersion = ""
FirstRun = True
while True:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    for script in soup(["script", "style"]):
        script.extract() 
    soup = soup.get_text()
    if PrevVersion != soup:
        if FirstRun == True:
            PrevVersion = soup
            FirstRun = False
            print ("Start Monitoring "+url+ ""+ str(datetime.now()))
        else:
            hook.send(embed=embed)
            print ("Changes detected at: "+ str(datetime.now()))
            OldPage = PrevVersion.splitlines()
            NewPage = soup.splitlines()
            diff = difflib.context_diff(OldPage,NewPage,n=10)
            out_text = "\n".join([ll.rstrip() for ll in '\n'.join(diff).splitlines() if ll.strip()])
            print (out_text)
            OldPage = NewPage
            PrevVersion = soup
    else:
        print( "No Changes "+ str(datetime.now()))
    time.sleep(1)
    continue