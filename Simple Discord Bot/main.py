import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

#Sends message
@bot.command()
async def hello(ctx):
  await ctx.send("Hello!")


#Speak as bot
@bot.command()
async def nsay(ctx, *, message):
     await ctx.message.delete()
     await ctx.send(f"{message}" .format(message)) 
  
#Status
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Youtube"))
    print("Bot is Online and Ready")


#Sends some Embed
@bot.event
async def on_message(message):
    if message.content.startswith('!help'):
        embedVar = discord.Embed(title="Commands", description="Available commands **4**", color=0xCCA95A)
        embedVar.add_field(name="Fun-Stuff", value="!yourcommand", inline=False)
        await message.channel.send(embed=embedVar)

#Reply to your message		
@bot.event      
async def on_message(message):
    if message.content == "hi":
        await message.channel.send("hello", reference=message)

                  
client.run(os.getenv('TOKEN'))
