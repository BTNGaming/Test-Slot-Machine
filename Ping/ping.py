from redbot.core import commands

class Ping(commands.Cog):
    """A simple ping command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping2", aliases=["p"])
    async def _ping(self, ctx):
        """Replies with 'Pong!'"""
        await ctx.send("Pong!")