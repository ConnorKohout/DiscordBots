import discord
import random

quotes = ["you busting no nuts lil bro. ur testosterone levels are dangerous low according to your doctor.", "we need to get quinton some honeys",
          "and his name is fucjing jermaine jackson","ethan tryna get good brain","drunk and high two spectrums","i need to grt higher","ur testosterone levels are dangerous low according to your doctor",
          "faaaccttts","im thick like a chopstick","iowa smoking good weed","im here at the library with my other dogs","i need drugs","ridin around in the lobby i know that they tie of me having like ten hoes",
          "playing both sides with ethans mom","he was like u smoking dick tryna trip like fen video","jermane said he a no show",
          "i mix all problems with prometh until i roll in my death bed","i rescind my previous comment","we not with that gay shit here","cant trust no bitch",
          "but im sippen that kombucha either pink or brown","i know that they tired of me havin like ten hoes","im dead sears","me and jmane committed murder on the low",
          "don had a creampie","he was receiving a creampie","kill yourself","yall aint sensed my energy fake af","so is dame fucking or whats up","ima lock you up cuz your mentally deteriorating","for waifu yes she gotta have good brain",
          "cannabism","he def hoeing","gay as fuck","fuck them mexicans","jk love then mexicans","if i ever put the gang on id be the most legendary member","traveling the world like the pope","guys guys im having a baby","why the fuck these 7777777 acting like they know us"
          ,"like interdimensional travel type fried not blackout type","have u started on that 440 prog assignment","i dont got a mom so fuck you pussy","on a scale of 1-sydney sweeney i give it a sydney sweeney","if you know what i know hide your hoe","can i fuck hoes at your crib",
          "i need to curate ethans tinder"]
# Define the bot class inheriting from discord.Client
class SimpleBot(discord.Client):
    async def on_ready(self):
        # This method is called when the bot is fully connected and ready
        print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        # This method is called whenever a message is sent in a channel your bot has access to
        if message.author == self.user:
            return  # Ignore messages sent by the bot itself

        if message.content.startswith('!kys'):
            await message.delete()
            await message.channel.send('IF YOU COMPLAIN YOU A CERTIFIED BITCH!!!! KILL YOURSELF')
            

        if message.content.startswith('!ethan'):
            await message.channel.send("https://www.youtube.com/watch?v=vZAgr33aBIg")
            await message.delete()

        if message.content.startswith('!xiu'):
            await message.channel.send("xiu lau quay nan chi phai fuck you")
            await message.delete()

        if message.content.startswith('!help'):
            await message.channel.send("xiu lau quay nan chi phai fuck you")
            await message.delete()

        if message.content.startswith('!jmane'):
            await message.channel.send("$quote")
            await message.delete()

        if message.content.startswith('!quote'):
            quote = random.choice(quotes)
            await message.channel.send(quote)
            await message.delete()

# Define intents for the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Create an instance of your bot
client = SimpleBot(intents=intents)
with open("khotoken.txt", "r") as file:
    token = file.read().strip()
client.run(token)