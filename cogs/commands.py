import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class Command(commands.Cog):
    def __init__(self, client):
        self.client = client

    @slash_command(guild_ids=[1151244211195228232])
    async def hello_slash(self, ctx):
        await ctx.respond('Hello World')

def setup(client):
    client.add_cog(Command(client))
