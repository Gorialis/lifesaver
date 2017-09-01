from discord.ext import commands
from discord.ext.commands import command, group
from lifesaver.bot import Cog, command
from lifesaver.bot.storage import AsyncJSONStorage


class Sample(Cog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tags = AsyncJSONStorage('tags.json')

    @command()
    async def sample(self, ctx):
        """ A sample command. """
        await ctx.send('Hello!')

    @group(invoke_without_command=True)
    async def tag(self, ctx, *, key):
        """ Tag management commands. """
        tag = self.tags.get(key)
        if not tag:
            await ctx.send('No such tag.')
        else:
            await ctx.send(tag)

    @tag.command()
    async def list(self, ctx):
        """ Lists all tags. """
        tags = self.tags.all().keys()
        await ctx.send(f'{len(tags)}: {", ".join(tags)}')

    @tag.command(aliases=['create'])
    async def make(self, ctx, key: commands.clean_content, *, value: commands.clean_content):
        """ Creates a tag. """
        if key in self.tags:
            return await ctx.send('Tag already exists.')
        await self.tags.put(key, value)
        await ctx.send('\N{OK HAND SIGN}')


def setup(bot):
    bot.add_cog(Sample(bot))
