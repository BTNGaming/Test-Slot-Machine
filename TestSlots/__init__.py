from .testslotmachine import TestSlotMachine


def setup(bot):
    bot.add_cog(TestSlotMachine(bot))