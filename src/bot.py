import os
import discord
from discord.ext import commands

## Constants and ENV stuff
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="%")

bot.run(DISCORD_TOKEN)