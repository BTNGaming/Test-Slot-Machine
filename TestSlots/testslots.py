from redbot.core import commands
import asyncio
import random
import discord

class TestSlots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aslot(self, ctx):
        emojis = [":cherries:", ":cookie:"]
        spinning_emojis = [":cherries:", ":cookie:", ":two:", ":four_leaf_clover:", ":cyclone:", ":sunflower:", ":six:", ":mushroom:", ":heart:", ":snowflake:"]

        result = [    [random.choice(emojis) for i in range(3)],
            [random.choice(emojis) for i in range(3)],
            [random.choice(emojis) for i in range(3)],
        ]

        embed = discord.Embed(
            title="Animated Slot Machine",
            description=f'{" | ".join(result[0])}\n{" | ".join(result[1])}\n{" | ".join(result[2])}',
            color=discord.Color.red()
        )
        message = await ctx.send(embed=embed)

        for i in range(8):
            spinning_results = [[random.choice(spinning_emojis) for j in range(3)] for i in range(3)]
            embed.description = "\n".join([f'{" | ".join(row)}' for row in spinning_results])
            await message.edit(embed=embed)
            await asyncio.sleep(0.5)

        embed.description = f"x{result[0][0]} | {result[0][1]} | {result[0][2]}x\n" \
                    f">{result[1][0]} | {result[1][1]} | {result[1][2]}<\n" \
                    f"x{result[2][0]} | {result[2][1]} | {result[2][2]}x"
        await message.edit(embed=embed)

        if all(result[1][0] == result[1][1] == result[1][2] for i in range(3)):
            await ctx.send("Congratulations! You've hit the jackpot!")
        else:
            await ctx.send("Better luck next time.")