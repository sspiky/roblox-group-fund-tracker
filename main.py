import requests
import asyncio
from datetime import datetime
import discord

bot = discord.Client(intents=discord.Intents.all())

groups = ['111111111','22222222','1333333337','444444444','5555555']
headers = {"cookie":".ROBLOSECURITY=_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_asdfasfbasgfhjasahjsafavjcvbzvz"}

@bot.event
async def on_ready():
    while True:
            await fetch()
            await send_embed()
            await asyncio.sleep(3600)

async def fetch():
    global total, r
    r = []
    total = 0
    
    for i in groups:
        try:
            res = requests.get(f'https://economy.roblox.com/v1/groups/{i}/currency', headers=headers)
            nres = requests.get(f'https://groups.roblox.com/v2/groups?groupIds={i}')
            name = nres.json()["data"][0]["name"]
            robux = res.json()["robux"]
            r.append(f"`{robux:,}` | **{name}**")
            total += robux
            
        except Exception:
            await asyncio.sleep(3)
            continue

async def send_embed():
    global total, r
    embed = discord.Embed(title=f":money_with_wings: `{total:,}` R$ in stock", description="**Groups:**\n{r}".format(r='\n'.join(r)), timestamp=datetime.utcnow())
    channel = bot.get_channel(123456789123456789)
    await channel.send(embed=embed, delete_after=3600)

bot.run('put bot token here')

