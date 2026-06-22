import discord
from discord.ext import commands
import os
import random
import requests

verduras = ['zanahorias la huerta', 'lechugas fresquitas', 'tomates don rojo', 'cebollas el surco', 'verduras el sembrador']
carnes = ['carnes el rancho', 'reses la pradera', 'cortes don ganado', 'carniceria el protrero', 'carnes selectas el campo']
frutas = ['manzanas del valle', 'frutas sol tropical', 'naranjas la cosecha', 'frutas el huerto', 'mangos don sol']
harinas = ['harina trigal', 'harnia la espiga', 'harina molino real', 'harina campo dorado', 'harina el costal']
otros = ['alimentos la mesa', 'productos buen sabor', 'delicias caceras', 'alimentos el granero', 'sabor de familia']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command('comprar')
async def productos(ctx):
    verdura = random.choice(verduras)
    carne = random.choice(carnes)
    fruta = random.choice(frutas)
    harina = random.choice(harinas)
    otro = random.choice(otros)
    await ctx.send(f'"{verdura}", es importante comer mucha verdura. "{carne}", la carne te dará muchas proteinas. "{fruta}", la fibra es vital. "{harina}", las harinas le a;aden un buen sabor. "{otro}", un pequeño gustito.')


bot.run("tu token va aqui")