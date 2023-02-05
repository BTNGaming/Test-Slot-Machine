from redbot.core import commands

class TestSlots(commands.Cog):
    """My custom animated slots cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aslot(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")