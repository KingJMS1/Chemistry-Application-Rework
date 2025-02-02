import os
import discord
import re
import typing

from dotenv import load_dotenv

from EquationBalancer import EquationBalancer
from MolarMass import MolarMass
from PercentComposition import PercentComposition

load_dotenv(dotenv_path=".idea/.env")

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.members = True

client = discord.Client(intents=intents)


# notifies if i am connected or not
@client.event
async def on_ready():
    print(f"{client.user} has connected onto discord!")


# the server must be able to say hello to them when they join the server
@client.event
async def on_member_join(member):
    print(f"{member.name} has joined")
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to ChemBot server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-chembot"):
        author = message.author.mention
        command = message.content.replace("-chembot", "").strip()

        print(f"Command: {command}")

        if len(command) == 0:
            await message.channel.send(f"Missing command?")
            return

        # Molar mass
        if command == "molar mass":
            await message.channel.send(f"{author} wants to know molar mass?")
        # Percent Composition
        elif command == "percent comp":
            await message.channel.send(f"{author} wants to know percent composition?")
        # Equation Balancer
        elif command == "bal eq":
            await message.channel.send(f"{author} wants to know a balanced chemical equation?")
        else:
            await message.channel.send(f"{author} no clue what you want.")


client.run(TOKEN)
