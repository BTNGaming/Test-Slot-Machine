import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot is ready. Login as {client.user}")

@client.event
async def on_message(message):
    if message.content.startswith("/mycommand"):
        # Your code here
        await message.channel.send("Your response here")


# from redbot.core import commands

# class Ping(commands.Cog):
#     """A simple ping command."""

#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(name="ping2", aliases=["p"])
#     async def _ping(self, ctx):
#         """Replies with 'Pong!'"""
#         await ctx.send("Pong!")