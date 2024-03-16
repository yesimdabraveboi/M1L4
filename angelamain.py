from settings import settings
import discord
from bot_logic import *
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
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
    elif message.content.startswith('$clash'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('Angela, generate a password'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('ANGELA!'):
        await message.channel.send('Manager, you do not need to yell for I am right next to you.')
    if message.content.startswith('$guess'):
            await message.channel.send('Guess a number between 1 and 10, manager.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)
            try:
                guess = await client.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long to think, dear manager. It was {answer}.')

            if not guess.content.isdigit():
                return await message.channel.send("That's not a valid guess. Please enter a number, manager.")
            
            if int(guess.content) == answer:
                await message.channel.send('You are correct, manager.')
            else:
                await message.channel.send(f'Incorrect. It is actually {answer}, manager. Sometimes I wonder your competence to run this company.')
client.run("TOKEN")
