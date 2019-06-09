#!/usr/bin/env python3

import discord

TOKEN = 'NTg3MzQ1NjMzNzQ5MjM3Nzk0.XP1Ynw.UPnqr8r8m-l712VgPL29OTnJxCA'

def discordStart():
    client = discord.Client()

    @client.event
    async def on_ready():
        print("The bot is ready!")
        await client.change_presence( activity=discord.Game(name="Making a Bot"))
    @client.event
    async def on_message (message):
        if message.author == client.user:
            return
        if message.content.startswith('!hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

    client.run(TOKEN)

discordStart()