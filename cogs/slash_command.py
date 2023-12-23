from discord.ext import commands
from discord.commands import Option

class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} ({self.bot.user.id})')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(f'Error: {error}')

    @commands.slash_command(guild_ids=[1151244211195228232])
    async def myinfo(
        self,
        ctx,
        name: Option(str, 'Enter Your name')
    ):
        await ctx.respond(f'Your name is {ctx.get("name")}')

def setup(bot):
    bot.add_cog(SlashCommands(bot))
