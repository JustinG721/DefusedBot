import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from datetime import datetime as dt
import humanize

from config import token

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('ready when you are')
    print('I am running on {}'.format(bot.user.name))
    print('with ID: {}'.format(bot.user.id))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('pong')

@bot.command(pass_context=True)
async def stats(ctx, user: discord.Member):
    now = dt.utcnow()
    duration = humanize.naturaltime((now - user.joined_at).total_seconds())

    embed = discord.Embed(title=user.name, description='This is you', color=0xFFFF00)
    embed.add_field(name='Name', value=user.name, inline=False)
    embed.add_field(name='Date Joined', value=humanize.naturaldate(user.joined_at), inline=False)
    embed.add_field(name='Joined', value='{}'.format(duration), inline=False)
    await bot.say(embed=embed)

bot.run(token)