#!/usr/bin/env python3

import discord
from discord.ext import commands

TOKEN = 'NTg3MzQ1NjMzNzQ5MjM3Nzk0.XP1Ynw.UPnqr8r8m-l712VgPL29OTnJxCA'

client = discord.Client()
bot = commands.Bot(command_prefix='!')
author = discord.User.id
def startdiscord():
    @client.event
    async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        if message.content.startswith('!hello'):
            msg = 'Hello this is a test'
            await bot.on_message(msg)

    @bot.command
    async def test(ctx):
        await ctx.send('I heard you! {0}'.format(ctx.author))

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    client.run(TOKEN)


startdiscord()