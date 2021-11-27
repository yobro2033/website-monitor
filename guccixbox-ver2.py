import requests
import difflib
from bs4 import BeautifulSoup
import time
from datetime import datetime
from dhooks import Webhook, Embed

url = "https://www.gucci.com/uk/en_gb/pr/c/xbox-by-gucci-p-693083UI7BD8957"
headers = {'User-Agent': 'Mozilla/5.0'}

hook = Webhook('https://discord.com/api/webhooks/658061206548119562/0k4VOMro53L3mCjFOTfgJgIYqeFvuBA6BAyC-Ol2exL9ijspMGf0hcJspKtP0at4h1he')

embed = Embed(
  description='XBOX x GUCCI RESTOCK',
  color=0x5CDBF0,
  timestamp='now'
  )

embed.add_field(name='Click this link', value='https://www.gucci.com/uk/en_gb/pr/c/xbox-by-gucci-p-693083UI7BD8957')

FirstRun = True
FirstRunVar = ""
SecondRunVar = ""
while FirstRun == True:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    dataFirst = soup.findAll("div",{"class":"sizes"})
    FirstRunVar = str(dataFirst)
    print ("Start Monitoring "+url+ " @ "+ str(datetime.now()))
    FirstRun = False
while FirstRun == False:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    dataSecond = soup.findAll("div",{"class":"sizes"})
    SecondRunVar = str(dataSecond)
    if FirstRunVar != SecondRunVar:
        hook.send(embed=embed)
        time.sleep(0.5)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        dataSecond = soup.findAll("div",{"class":"sizes"})
        SecondRunVar = str(dataSecond)
        print("Detected change @ " + str(datetime.now()))
    else:
        print("No Change " + str(datetime.now()))
    time.sleep(0.001)