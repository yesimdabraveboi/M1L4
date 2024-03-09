from settings import settings
import discord
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hi Angela'):
        await message.channel.send('Greetings. I am Angela, an AI. I am your assistant, your secretary, and someone to whom you can talk. I  hope I can help make your time here a little more comfortable.')
    elif message.content.startswith('Angela, smile'):
        await message.channel.send('Do you wish for me to smile, manager? Very well. I will smile for you.')
    elif message.content.startswith('!Clash'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('Angela, generate a password'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('ANGELA!'):
        await message.channel.send('Manager, you do not need to yell for I am right next to you.')

client.run("TOKEN")
