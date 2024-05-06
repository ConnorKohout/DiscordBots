import discord
import asyncio
import re
import random

quotes=["starts off with being tipsy on the job then boom your in mexico with three baby mama","where is my ramona flowers","o block has an aura that i can feel from my hotel"]

intents = discord.Intents.default()
intents.messages = True  # Enable message intents
intents.message_content = True  # Enable message content intent for handling messages

TARGET_USER_ID = 452873873428316160  # Replace with the actual user ID
FILE_PATH = 'C:/Users/Conno/projects/khu0ng/khdata.txt'  # Path where you want to save the file
FILE_PATH2 ='C:/Users/Conno/projects/khu0ng/jdata.txt'
def clean_text(text):
    """Basic text cleaning and normalization"""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces and strip trailing spaces
    text = re.sub(r'https?://\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove non-alphanumeric characters except spaces
    return text

class MyDiscordBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(1028516903603421264)  # Replace with the actual channel ID
        if channel:
            async for message in channel.history(limit=100000):  # Fetch all messages
                if message.author.id == TARGET_USER_ID and not message.author.bot:
                    if message.content and not message.content.startswith(('!', '/', '.')):
                        cleaned_message = clean_text(message.content)
                        if len(cleaned_message) > 1:  # Only save messages longer than 1 characters
                            try:
                                with open(FILE_PATH, 'a', encoding='utf-8') as file:
                                    file.write(f"{cleaned_message}\n")
                            except Exception as e:
                                print(f"Error writing message to file: {e}")

    async def on_message(self, message):
        # Prevent the bot from replying to itself
        if message.author == self.user:
            return
        
        if message.content.startswith('$quote'):
            quote = random.choice(quotes)
            await message.channel.send(quote)
            await message.delete()
        
        if message.content.startswith('$help'):
            await message.channel.send('Hello! I am Jermane bot. Here is a list of known commands: $hello, $ice, $floor, $apu, $fein, $quote')

        if message.content.startswith('$hello'):
            await message.channel.send('Hello! I am Jermane bot here to assist you with any coding assignment you are currently failing.')

        if message.content.startswith('$floor'):
            await message.channel.send('I am on the floor.')
            await message.delete()
        if message.content.startswith('$ice'):
            await message.channel.send("Ice Spice's a MUNCH!")
            await message.delete()
        if message.content.startswith('$ramona'):
            await message.channel.send("where is my ramona flowers")
            await message.delete()

        if message.content.startswith('$fein'):
            await message.channel.send("https://www.youtube.com/watch?v=B9synWjqBn8")
            await message.delete()
        if message.content.startswith('$apu'):
            await message.channel.send("Apu is apuing")
            await message.delete()

        if message.content.startswith('$khuong'):
            await message.channel.send("!quote")
            
        if message.content.startswith('$cancer'):
            await message.channel.send('shawty you got to be cancer cause you make me feel some type of way and no i cannot be canceled cause you feel some type of way')
            await message.delete()
# Replace 'mytokenishere' with your actual Discord bot token
client = MyDiscordBot(intents=intents)
with open("jertoken.txt", "r") as file:
    token = file.read().strip()
client.run(token)