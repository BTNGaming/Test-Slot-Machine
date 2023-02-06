from redbot.core import commands
import asyncio
import random
import discord

class TestSlots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aslot(self, ctx):
        emojis = [":cherries:", ":cookie:", ":two:"]
        spinning_emojis = [":mushroom:", ":heart:", ":snowflake:"]

        result = [[random.choice(emojis) for j in range(3)] for i in range(3)]

        embed = discord.Embed(
            title="Animated Slot Machine",
            description=f'{" | ".join(result[0])}\n{" | >".join(result[1])}\n{"< | ".join(result[2])}',
            color=discord.Color.red()
        )
        message = await ctx.send(embed=embed)

        for i in range(8):
            spinning_results = [[random.choice(spinning_emojis) for j in range(3)] for i in range(3)]
            embed.description = "\n".join([f'>{" | ".join(row)}<' for row in spinning_results])
            await message.edit(embed=embed)
            await asyncio.sleep(0.5)

        embed.description = "\n".join([f'>{" | ".join(row)}<' for row in result])
        await message.edit(embed=embed)

        if all(result[0][i] == result[1][i] == result[2][i] for i in range(3)):
            await ctx.send("Congratulations! You've hit the jackpot!")
        else:
            await ctx.send("Better luck next time.")