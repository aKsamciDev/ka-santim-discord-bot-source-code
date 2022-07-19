import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random


intents = discord.Intents().all()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Ping: {round(bot.latency * 1000)}ms')
    print("Nully:CODE") 
    print("Bot'a bağlandı: {}".format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    await bot.change_presence(activity=discord.Game(name=f'{len(bot.guilds)} Sunucuda Ölçüm Yapıyor!'))

@bot.command()
async def destek(ctx):
    embed = discord.Embed(title="", description="") 
    color = (0xF90101)
    embed.add_field(name="**Nully:CODE**", value="**https://discord.gg/AkCETnaD**", inline=False) 
    embed.set_image(url="https://media.giphy.com/media/ZJB5EPInvETQY/giphy.gif")
    embed.set_footer(text="Developer By Nully:CODE ")
    await ctx.send('dm bak canim')
    await ctx.author.send(embed=embed) 
    
@bot.command(pass_context = True)
async def kaccm(ctx):
    embed = discord.Embed(title = (random.randint(1, 31)), description = "Santim ¿", color = (0xF9F501))
    await ctx.send(embed = embed)

@bot.command(pass_context = True)
async def kaçsantim(ctx):
    embed = discord.Embed(title = (random.randint(1, 31)), description = "Santim ¿", color = (0xF90101))
    await ctx.send(embed = embed)
    
@bot.command(pass_context = True)
async def kaçsantimabi(ctx):
    embed = discord.Embed(title = (random.randint(1000, 10000000)), description = "Ne santimi lan kilometre diyeceksin kilometre!", color = (0xF90101))
    await ctx.send(embed = embed)
    
@bot.command(pass_context = True)
async def zar(ctx):
    embed = discord.Embed(title = "Zar (1-6)", description = (random.randint(1, 6)), color = (0xEE76F5))
    await ctx.send(embed = embed)



bot.run('token')