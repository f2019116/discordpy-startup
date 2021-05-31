from discord.ext import commands
import os
import traceback

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
       return  　　　　　　　　＃発言者がBOTなら無視
   if message.content == 'やっほー':　　　　　＃発言に返信する
       await message.channel.send('やっほー')　＃返信内容は''で括る。


bot.run(token)
