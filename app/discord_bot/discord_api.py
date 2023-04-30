from dotenv import load_dotenv
import discord
import os
from app.openai.openai_api import openai_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)
    
    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        if message.content == '/ping':
            await message.channel.send('pong')
        
        command, user_message = None, None
        for text in ['/ask', '/bot', '/tell me', '/tellme', '/tell_me']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(command, '')
                print(command, user_message)
        
        if command in ['/ask', '/bot', '/tellme']:
            try:
                bot_response = openai_response(prompt = user_message)
                await message.channel.send(f'{bot_response}')
                print(f'Response - {bot_response}')
            except Exception as e:
                print(e)
                await message.channel.send('Sorry, I am not feeling well today. Please try again later.')
                
            
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)