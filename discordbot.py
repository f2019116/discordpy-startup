from discord.ext import commands
import os
import traceback
import discord
import random

bot = commands.Bot(command_prefix='/')
token = 'ODMxNzI4NjY5MzQ0MjY4MzI1.YHZdrw.2CWYmA0J6SyQHnOrMAp4TyRdXGM'
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
@client.event()
async def on_message(message):#メッセージを受け取る関数
    if message.content == "おはよう":
        await client.send_message(message.channel,"おはー")
    
bot.run(token)

