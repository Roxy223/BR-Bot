# bot.py
import discord
from discord.ext import commands
from keep_alive import keep_alive   # make sure you have a keep_alive.py file

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    keep_alive()  # starts the webserver
    bot.run("MTQwMTg1NjExMTI3MDgyNjA2Ng.GYRmOo.0b7sjqvldH60GxN8YWGilnD9zIEzkXagwRkzE4")

