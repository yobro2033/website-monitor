import requests
import difflib
from bs4 import BeautifulSoup
import time
from datetime import datetime
from dhooks import Webhook, Embed

url = "https://anything-we-want-it-to-be.myshopify.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

hook = Webhook('https://discord.com/api/webhooks/658061206548119562/0k4VOMro53L3mCjFOTfgJgIYqeFvuBA6BAyC-xxx')

embed = Embed(
  description='Detected A Ma Maniere changed domain',
  color=0x5CDBF0,
  timestamp='now'
  )

FirstRun = True
FirstRunVar = ""
SecondRunVar = ""
while FirstRun == True:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    FirstRunVar = str(soup)
    print ("Start Monitoring "+url+ " @ "+ str(datetime.now()))
    FirstRun = False
while FirstRun == False:
    response = requests.get(url, headers=headers)
    soup2 = BeautifulSoup(response.text, "html.parser")
    SecondRunVar = str(soup2)
    if FirstRunVar != SecondRunVar:
        newDomain = soup.findAll("meta",{"property":"og:url"})
        hook.send(embed=embed)
        time.sleep(0.5)
        print("Detected change @ " + str(datetime.now()))
    else:
        print("No Change " + str(datetime.now()))
    time.sleep(0.5)
