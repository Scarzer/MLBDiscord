import os
import discord
from discord.ext import commands
from games import ScoreBoard, generate_active_game_list_embed, generate_game_list_embed, get_games_today

## Constants and ENV stuff
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="%")

@bot.command()
async def list_all(context):
    sbs = get_games_today()
    emb = generate_game_list_embed(sbs)
    await context.send(embed=emb)

@bot.command()
async def list(context):
    sbs = get_games_today()
    emb = generate_active_game_list_embed(sbs)
    await context.send(embed=emb)

@bot.command()
async def track(context, game_index):
    games = {
        "games_not_started" : [],
        "games_in_progress" : [],
        "games_done" : []
    }

    sbs = get_games_today()
    
    for s in sbs:
        if s.game_status == "IN_PROGRESS":
            games["games_in_progress"].append(s)
        elif s.game_status == "FINAL":
            games["games_done"].append(s)
        elif s.game_status == "PRE_GAME":
            games["games_not_started"].append(s)
        else:
            print(f"Unknown game status: {s.game_status}")

    if game_index is None:
        print(games)
        await context.send(f"{len(games['games_in_progress'])}")


bot.run(DISCORD_TOKEN)