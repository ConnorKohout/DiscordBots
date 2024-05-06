import discord
import random
import re

TARGET_USER_ID = 366660921051054080  # Replace with the actual user ID
FILE_PATH = 'C:/Users/Conno/projects/khu0ng/feddata.txt'  # Path where you want to save the file
FILE_PATH2 ='C:/Users/Conno/projects/khu0ng/jdata.txt'
def clean_text(text):
    """Basic text cleaning and normalization"""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces and strip trailing spaces
    text = re.sub(r'https?://\S+', '', text)  # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)  # Remove non-alphanumeric characters except spaces
    return text

quotes = ["That's what that tweak does to ya kid.","When you're around tweakers you end up with cops in your face","I was filming you actually stalking me I was heading down to the chief of police","I'm suing their ass off","I hope they fire ya",
          "the news agencies aint acting square these days americans","Paid for the gas, right over there. Number one... just like me.","whats up pig? whats up you sowbelly??","Whats the story brother?","Bottle babies??? Jesus...","I'm out here to communicate with you fuckers.",
          "Imma fuck em up with my wires.... and twist their fuckin souls....","Even this baby will wear a baby raper stamp on the forehead right there","Long story short my mom talked me out of not blowing his fuckin head off","ta-ta there, retard","Keep them baby-rapers on their toes, never let the featherin' stop.",
          "You can't corral the wild, and you sure can't cage this storm."]
# Define the bot class inheriting from discord.Client
class SimpleBot(discord.Client):
    async def on_ready(self):
        # This method is called when the bot is fully connected and ready
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        channel = self.get_channel(744742621938974813)  # Replace with the actual channel ID
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
        # This method is called whenever a message is sent in a channel your bot has access to
        if message.author == self.user:
            return  # Ignore messages sent by the bot itself

        if message.content.startswith('!quote'):
            quote = random.choice(quotes)
            await message.channel.send(quote)
            await message.delete()
            
        if message.content.startswith('!baby'):
            await message.channel.send("Bottle babies??? Jesus...")
            await message.delete()
        if message.content.startswith('!pig'):
            await message.channel.send("whats up pig? whats up you sowbelly??")
            await message.delete()
        if message.content.startswith('!fed'):
            await message.channel.send("Ta ta retard. That's what you get for being a baby rapin' fed.")
            await message.delete()

# Define intents for the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
with open("fedtoken.txt", "r") as file:
    token = file.read().strip()
# Create an instance of your bot
client = SimpleBot(intents=intents)
client.run(token)