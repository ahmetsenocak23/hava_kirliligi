import discord
from discord.ext import commands
import os 
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.command()
async def merhaba(ctx):
    await ctx.send("Merhaba ben bir discord botum , Ben hava kirliliği hakkında bilgiler verebilirim. Eğer hava kirliliği ile ilgili bilgi almak istiyorsanız **-bilgi** yazabilirsin. \n Video için **-vid** yazabilirsin.")

@bot.command()
async def bilgi(ctx):
    await ctx.send("**Hava kirliliğini önlemek için yapmamız gerekenler :** \n **1.** benzinli arbalar yerine elektrikli araçlar kullanmalıyız.(Toplu taşıma kullanmak da bir seçenek😀) \n **2.** Parfüm kullanmayı bırakmalıyız veya yavaş yavaş azaltıp kullanımını bitirmeliyiz. \n **3** plastik kullanımını azaltmalıyız dolylı yoldan ilk önce çevreyi sonra havayı kirletir. \n **4** Yeşil alanları arttırmalıyız.")

@bot.command()
async def vid(ctx):
 await ctx.send("https://www.youtube.com/watch?v=Wd0FzQTDM90")

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')


bot.run("GİZLİ TOKEN BURUYA / SECRET TOCEN HERE")
