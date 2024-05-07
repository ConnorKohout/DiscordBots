import discord
import asyncio
import re
import random

quotes=["starts off with being tipsy on the job then boom your in mexico with three baby mama","where is my ramona flowers",
        "o block has an aura that i can feel from my hotel","getting up is for the strong i am currently weak","i was playing the game until like 5 last night","hater alert hater alert",
        "well the bigger question is can we prove something is recognizable by failing mapping reduction with nhalt being the problem we reduce",
        "im about to leave the lib if cranston does not answer by the time i get home houston we have a problem","thats exactly what i am saying since we are talking in generality the property state that  if given an a description of a machine l1 accepts a machine encoding that accepts its forward or its backwards, we dont need to know the encoding as long as it accepts forward and backwards then it will be in l1 see how it says there is at least one machine m with m in l1 if we say that the machine m is the machine with the encoding that accepts palindromes and the reverse that m is a member of l1",
"intellectual humanoids like cranston and myself just vibrate diff","jermane turing","knowledge is power but power is not knowledge","cause xiu lau quack liu is a vibe",
"u not khoung chomsky","nastyyy","aye that virginia one hit though","maybe his cranston smarts can rub off on me"
,"hey girl are you into pda because ive constructed a pushdown automata that can generate binary palindromes",""]
intents = discord.Intents.default()
intents.messages = True  # Enable message intents
intents.message_content = True  # Enable message content intent for handling messages

TARGET_USER_ID = 570788093527851008  # Replace with the actual user ID
FILE_PATH = 'C:/Users/Conno/projects/bots/DiscordBots/quackdata.txt'  # Path where you want to save the file
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
        try:
            with open("channel_ID.txt", "r") as file:
                channelIDs = file.readlines()
            for channelID in channelIDs:
                channel = self.get_channel(int(channelID.strip()))
                if channel:
                    async for message in channel.history(limit=100000):  # Adjust limit as needed
                        if message.author.id == TARGET_USER_ID and not message.author.bot:
                            if message.content and not message.content.startswith(('!', '/', '.')):
                                cleaned_message = clean_text(message.content)
                                if len(cleaned_message) > 1:
                                    with open(FILE_PATH, 'a', encoding='utf-8') as f:
                                        f.write(f"{cleaned_message}\n")
        except Exception as e:
            print(f"Error during setup: {e}")


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
        if message.content.startswith('$apu'):
            await message.channel.send("Apu is apuing")
            await message.delete()
# Replace 'mytokenishere' with your actual Discord bot token
client = MyDiscordBot(intents=intents)
with open("jertoken.txt", "r") as file:
    token = file.read().strip()
client.run(token)
