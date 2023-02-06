from random import randint, choice
from redbot.core import commands
import asyncio
import random
import discord

# class TestSlots(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
    
#     @commands.command()
#     async def aslot(self, ctx):
#         emojis = ['\N{CHECK MARK}', '\N{X}', '🍇', '🍉', '💰']
#         spinning_emojis = ['⠀', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '⠇']
#         spinning = [f"{emoji} {emoji} {emoji}" for emoji in spinning_emojis]
#         result = [random.choice(emojis) for i in range(3)]
#         for spin in spinning:
#             await ctx.send(spin)
#             await asyncio.sleep(0.5)
#         await ctx.send(' '.join(result))
#         if result[0] == result[1] == result[2]:
#             await ctx.send("Congratulations! You've hit the jackpot!")
#         else:
#             await ctx.send("Better luck next time.")

class TestSlots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aslot(self, ctx):
        emojis = [":cherries:", ":cookie:", ":two:", ":four_leaf_clover:", ":cyclone:", ":sunflower:", ":six:", ":mushroom:", ":heart:", ":snowflake:"]
        spinning_emojis = [":cherries:", ":cookie:", ":two:", ":four_leaf_clover:", ":cyclone:", ":sunflower:", ":six:", ":mushroom:", ":heart:", ":snowflake:"]

        reels = []
        for i in range(0, 3):
            n = randint(3,12)
            reels.append([reel[n - 1], reel[n], reel[n + 1]])
            result = [reels[0][1], reels[1][1], reels[2][1]]

            display_reels = "  " + reels[0][0] + " " + reels[1][0] + " " + reels[2][0] + "\n"
            display_reels += ">" + reels[0][1] + " " + reels[1][1] + " " + reels[2][1] + "\n"
            display_reels += "  " + reels[0][2] + " " + reels[1][2] + " " + reels[2][2] + "\n"

        # result = [random.choice(emojis) for i in range(3)]

        embed = discord.Embed(
            title="Animated Slot Machine",
            description=" ".join(result),
            color=discord.Color.red()
        )
        message = await ctx.send(embed=embed)

        for i in range(8):
            embed.description = " ".join([random.choice(spinning_emojis) for _ in range(3)])
            await message.edit(embed=embed)
            await asyncio.sleep(0.5)

        embed.description = " ".join(result)
        await message.edit(embed=embed)

        if result[0] == result[1] == result[2]:
            await ctx.send("Congratulations! You've hit the jackpot!")
        else:
            await ctx.send("Better luck next time.")

        await message.edit(embed=embed)