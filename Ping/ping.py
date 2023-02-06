from redbot.core import commands

class Ping(commands.Cog):
    """A simple ping command."""

    @commands.command(name="ping", aliases=["p"])
    async def _ping(self, ctx):
        """Replies with 'Pong!'"""
        await ctx.send("Pong!")