from redbot.core import commands
import discord
from discord.ext import commands
import asyncio
import random

class TestSlots(commands.Cog):
    """My custom animated slots cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='aslots')
    async def aslot(self, ctx):
        """This does stuff!"""
        # Your code will go here
        emojis = ['🍒', '🍊', '🍇', '🍉', '💰']
        spinning_emojis = ['⠀', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '⠇']
        spinning = [f"{emoji} {emoji} {emoji}" for emoji in spinning_emojis]
        result = [random.choice(emojis) for i in range(3)]
        for spin in spinning:
            await ctx.send(spin)
            await asyncio.sleep(0.5)
        await ctx.send(' '.join(result))
        if result[0] == result[1] == result[2]:
            await ctx.send("Congratulations! You've hit the jackpot!")
        else:
            await ctx.send("Better luck next time.")


def setup(bot):
    bot.add_cog(TestSlots(bot))