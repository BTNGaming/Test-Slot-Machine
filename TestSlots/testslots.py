from redbot.core import commands
import asyncio
import random
import discord

class TestSlots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aslot(self, ctx):
        emojis = [":cherries:", ":cookie:", ":two:", ":four_leaf_clover:", ":cyclone:", ":sunflower:", ":six:", ":mushroom:", ":heart:", ":snowflake:"]
        spinning_emojis = [":cherries:", ":cookie:", ":two:", ":four_leaf_clover:", ":cyclone:", ":sunflower:", ":six:", ":mushroom:", ":heart:", ":snowflake:"]

        result = [random.choice(emojis) for i in range(3)]
        reel1 = random.choice(spinning_emojis)
        reel2 = random.choice(emojis)
        reel3 = random.choice(spinning_emojis)
        # reel4 = random.choice(spinning_emojis)
        # reel5 = random.choice(spinning_emojis)
        # reel6 = random.choice(spinning_emojis)
        # reel7 = random.choice(spinning_emojis)
        # reel8 = random.choice(spinning_emojis)
        # reel9 = random.choice(spinning_emojis)

        embed = discord.Embed(
            title="Animated Slot Machine",
            description=f'{reel1} | {reel2} | {reel3}',
            color=discord.Color.red()
        )
        message = await ctx.send(embed=embed)

        for i in range(8):
            embed.description = " ".join([reel1 | reel2 | reel3])
            await message.edit(embed=embed)
            await asyncio.sleep(0.5)

        embed.description = " ".join(result)
        await message.edit(embed=embed)

        if result[0] == result[1] == result[2]:
            await ctx.send("Congratulations! You've hit the jackpot!")
        else:
            await ctx.send("Better luck next time.")

        await message.edit(embed=embed)