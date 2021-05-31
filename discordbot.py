from discord.ext import commands
import os
import traceback
import discord 
import random

client = discord.Client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@client.event
async def on_message(message):
   if message.author.bot:　　　　　　　　　　　　　　　
       return
   if message.content == '樋□さんこんちわ':
       await message.channel.send('しずかにして')

 if message.content == "お話して！":
　　　　　#↓
       haha = ["", "", "", "", "", "", ""]
       choice = random.choice(haha)
       await message.channel.send(choice)

bot.run(token)
