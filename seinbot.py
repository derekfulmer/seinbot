#!/usr/bin/env python3
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'Hellooo! {member.name}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

    # Turn this into a DB look up.
	sein_quotes = [
		'Looking at cleavage is like looking at the sun.',
		'But, I don\'t wanna be a pirate!',
		'Hello...Newman.',
		'Are you master of your domain?',
		'People on dates shouldn\'t be allowed in public.'
	]

	if message.content == '!sein':
		response = random.choice(sein_quotes)
		await message.channel.send(response)
	
client.run(TOKEN)
