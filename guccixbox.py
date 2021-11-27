import requests
import difflib
import time
from datetime import datetime
from dhooks import Webhook, Embed

url = "https://www.gucci.com/uk/en_gb/pr/c/xbox-by-gucci-p-693083UI7BD8957"
headers = {'User-Agent': 'Mozilla/5.0'}

hook = Webhook('https://discord.com/api/webhooks/658061206548119562/0k4VOMro53L3mCjFOTfgJgIYqeFvuBA6BAyC-Ol2exL9ijspMGf0hcJspKtP0at4h1he')

embed = Embed(
  description='XBOX x GUCCI RELEASED',
  color=0x5CDBF0,
  timestamp='now'
  )

embed.add_field(name='Click this link', value='https://www.gucci.com/uk/en_gb/pr/c/xbox-by-gucci-p-693083UI7BD8957')

response = requests.get(url, headers=headers)
responseH = str(response.history)
print ("Start Monitoring "+url+ " @ "+ str(datetime.now()))
i = 0
while responseH != "[<Response [403]>]":
    i = i + 1
    response = requests.get(url, headers=headers)
    responseH = str(response.history)
    if responseH != "[<Response [301]>]":
        hook.send(embed=embed)
        print(i, "Detected change @ " + str(datetime.now()))
        time.sleep(1)
    elif responseH == "[]":
        hook.send(embed=embed)
        print(i, "Detected change @ " + str(datetime.now()))
        time.sleep(1)
    else:
        print(i, "No Change " + str(datetime.now()))
    time.sleep(0.1)