import json
import requests
import discord
from discord.ext import commands
import config
bot = commands.Bot(command_prefix=".")
 
 
@bot.event
async def on_ready():
    print("Bot connected")
 
 
@bot.command()
async def join(ctx):
    """target_application_id
 
        Youtube Together - 755600276941176913
        Betrayal.io - 773336526917861400
        Fishington.io - 814288819477020702
        Poker Night - 755827207812677713
        Chess - 832012774040141894
 
    """
 
    data = {
        "max_age": 86400,
        "max_uses": 0,
        "target_application_id": 755600276941176913, # YouTube Together
        "target_type": 2,
        "temporary": False,
        "validate": None
    }
    headers = {
        "Authorization": "Bot ODg0NDM2NzYxODgxNzQzMzYw.YTYd7A.wQ40y8OzWXvoDnT6jMIdGXkp9DM",
        "Content-Type": "application/json"
    }
 
    if ctx.author.voice is not None:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel.id
        else:
            await ctx.send("Зайдите в канал")
    else:
        await ctx.send("Зайдите в канал")
 
    response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
    link = json.loads(response.content)
 
    await ctx.send(f"https://discord.com/invite/{link['code']}")
 
bot.run(config.TOKEN)