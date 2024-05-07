import discord
import random
import re

quotes = ["you busting no nuts lil bro. ur testosterone levels are dangerous low according to your doctor.", "we need to get quinton some honeys",
          "and his name is fucjing jermaine jackson","ethan tryna get good brain","drunk and high two spectrums","i need to grt higher",
          "ur testosterone levels are dangerous low according to your doctor",
          "faaaccttts","im thick like a chopstick","iowa smoking good weed","im here at the library with my other dogs","i need drugs",
          "ridin around in the lobby i know that they tie of me having like ten hoes",
          "playing both sides with ethans mom","he was like u smoking dick tryna trip like fen video","jermane said he a no show",
          "i mix all problems with prometh until i roll in my death bed","i rescind my previous comment","we not with that gay shit here","cant trust no bitch",
          "but im sippen that kombucha either pink or brown","i know that they tired of me havin like ten hoes","im dead sears","me and jmane committed murder on the low",
          "don had a creampie","he was receiving a creampie","kill yourself","yall aint sensed my energy fake af","so is dame fucking or whats up",
          "ima lock you up cuz your mentally deteriorating","for waifu yes she gotta have good brain",
          "cannabism","he def hoeing","gay as fuck","fuck them mexicans","jk love then mexicans","if i ever put the gang on id be the most legendary member",
          "traveling the world like the pope","guys guys im having a baby","why the fuck these 7777777 acting like they know us"
          ,"like interdimensional travel type fried not blackout type","have u started on that 440 prog assignment","i dont got a mom so fuck you pussy",
          "on a scale of 1-sydney sweeney i give it a sydney sweeney","if you know what i know hide your hoe","can i fuck hoes at your crib",
          "i need to curate ethans tinder","you come with me ill give you riches","no fucking doubt i would abuse my power","im like kanye",
          "cranston brain would blow up from the filth that he witnesses","yall know damn well im the catalyst","don the original finesse god","don is my antithesis",
          "im banishing you to the shadow realm where you belong","i said i missed you and you come back with this outrageous bussy shit"
          ,"i would blow but im not gonna","so i ended up monetizing ethans mom by recording us committing adultery and selling the tapes at a high price online",
          "always take pussy with consent tho we dont steal pussy","go to the fucking gym","me and jermane finna pull up stomp somebody","bitch bitch bitch"]


class ResponseCategory:
    def __init__(self, pattern, responses):
        self.pattern = re.compile(pattern, re.IGNORECASE)
        self.responses = responses

    def match(self, text):
        return self.pattern.search(text)

    def respond(self, text):
        response = random.choice(self.responses)
        return response.format(text)

class Eliza:
    def __init__(self):
        self.categories = [
            ResponseCategory(r"I need (.*)", ["Need {0}, huh?'?", "{0}? I got you with that quack phai.", "You think needing {0} makes you a big man? Ta-ta there, retard."]),
            ResponseCategory(r"I am (.*)", ["You are {0}? Keep yappin', I've dealt with bigger fishes than you.", "{0}? That's right, run along now, sheep.", "Oh, you’re {0}? Watch your tone, chomo."]),
            ResponseCategory(r"police|cops", ["Cops? Those baby rapers are all on the featherin' list!", "Don't trust those costume wearers, always sniffin' around.", "Ha! Those gang stalkers? I've got my eye on them."]),
            ResponseCategory(r"(.*)(car|vehicle|van)(.*)", ["What’s with your {1}? You live in that thing or somethin'?", "Your {1}, huh? Does it run faster than the law?", "A {1}, eh? Bet it doesn’t have half the miles mine does."]),
            ResponseCategory(r"(.*)", ["What's that supposed to mean, huh?", "Keep talking, I’m just heating up my branding iron.", "Is that right? Well, ta-ta there, baby raper."])
        ]

    def reflect(self, phrase):
        words = phrase.split()
        replacements = {"i": "you", "you": "I", "me": "you", "am": "are", "my": "your", "your": "my"}
        reflected_phrase = [replacements.get(word.lower(), word) for word in words]
        return ' '.join(reflected_phrase)

    def analyze(self, statement):
        for category in self.categories:
            match = category.match(statement)
            if match:
                if match.groups():
                    reflected = self.reflect(match.group(1))
                    return category.respond(reflected)
                else:
                    return category.respond("...")
        return "Didn't catch that. Speak up, feather."
    


# Define the bot class inheriting from discord.Client
class SimpleBot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.eliza = Eliza()
        self.active_sessions = set()
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
            await message.channel.send("im tryna kiss ethan with my knee\n https://www.youtube.com/watch?v=vZAgr33aBIg")
            await message.delete()

        if message.content.startswith('!xiu'):
            await message.channel.send("xiu lau quay nan chi phai fuck you")
            await message.delete()

        if message.content.startswith('!help'):
            await message.channel.send("xiu lau quay nan chi phai fuck you")

        if message.content.startswith('!laos'):
            await message.channel.send("i want to commit a couple of laus")


        if message.content.startswith('!jmane'):
            await message.channel.send("$quote")
            await message.delete()

        if message.content.startswith('!og'):
            await message.delete()
            await message.channel.send('aryan ima just ignore you from now unless we talking about school cuz on god i will rip you to fucking pieces')
            

        if message.content.startswith('!quote'):
            quote = random.choice(quotes)
            await message.channel.send(quote)
            await message.delete()


        # Check if the user is currently in a session
        if message.author.id in self.active_sessions:
            if message.content.lower() == '!stop':
                self.active_sessions.remove(message.author.id)
                await message.channel.send("Goodbye! If you want to talk again, just say `!talk`.")
                return
            response = self.eliza.analyze(message.content)
            await message.channel.send(response)
            return            

        if message.content.startswith('!talk'):
            self.active_sessions.add(message.author.id)
            await message.channel.send("Hello! I'm here to chat. Type `!stop` to end our conversation.")
            return

# Define intents for the bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Create an instance of your bot
client = SimpleBot(intents=intents)
with open("khotoken.txt", "r") as file:
    token = file.read().strip()
client.run(token)