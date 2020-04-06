import os
from dotenv import load_dotenv

import random

import discord
from discord.ext import commands

import math

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hi {ctx.author.display_name}")

@bot.command(name = "equ", help="Solves your sacrifised quadratic and linear equations, takes in three arguments: a, b, c, which are coefficients. Even if coefficient is 0, it has to be listed. As example for equation 3x-4=0 you have to send 0 3 -4 as argumants.")
async def equation(ctx, a, b, c):
    if a==0:
        await ctx.send(f"x = {(-c)/b}")
    elif a!=0:
        discr= b**2 - 4*a*c
        if discr>=0:
            await ctx.send(f"x = {(-b+math.sqrt(discr))/2*a} ,  {(-b-math.sqrt(discr))/2*a]}")
        else:
            await ctx.send(f"x = ({-b} ± i√{discr})/{2*a}")
    elif a==0 & b==0:
        await ctx.send("There is no x to solve for")

#new command
@bot.command(name="Sacrifice", help="Sacrifice stuff")
async def sacrifice(ctx):
    opt = ["Yummy", "Nom", "Thank you", "*screeching*", "Mort is thankful", "I need more"]
    await ctx.send(opt[random.randint(0, 5)])

bot.run(TOKEN)
 #random stuff

