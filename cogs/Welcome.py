from modules import db
import time
import random
from modules import permissions

import discord
from discord.ext import commands

class Welcome(commands.Cog, name="Welcome"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="welcome", brief="", description="", pass_context=True)
    async def welcome_message(self, ctx, *, welcome_message):
        if permissions.check(ctx.message.author.id):
            try:
                await ctx.message.delete()
            except Exception as e:
                print(e)
            db.query(["INSERT INTO config VALUES (?,?,?,?)", ["guild_welcome_settings", str(ctx.message.guild.id), str(ctx.message.channel.id), str(welcome_message)]])
            await ctx.send(":ok_hand:", delete_after=3)
        else:
            await ctx.send(embed=permissions.error())

    @commands.command(name="goodbye", brief="", description="", pass_context=True)
    async def goodbye_message(self, ctx, *, goodbye_message):
        if permissions.check(ctx.message.author.id):
            try:
                await ctx.message.delete()
            except Exception as e:
                print(e)
            db.query(["INSERT INTO config VALUES (?,?,?,?)", ["guild_goodbye_settings", str(ctx.message.guild.id), str(ctx.message.channel.id), str(goodbye_message)]])
            await ctx.send(":ok_hand:", delete_after=3)
        else:
            await ctx.send(embed=permissions.error())

    async def make_string(self, template, member):
        return template.replace("(mention)", member.mention).replace("(server)", member.guild.name).replace("(name)", member.name)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        try:
            guildgoodbyesettings = db.query(["SELECT value, flag FROM config WHERE setting = ? AND parent = ?", ["guild_goodbye_settings", str(member.guild.id)]])
            if guildgoodbyesettings:
                right_message = random.choice(guildgoodbyesettings)
                channell = self.bot.get_channel(int(right_message[0]))
                await channell.send(await self.make_string(right_message[1], member))
        except Exception as e:
            print(time.strftime('%X %x %Z'))
            print("in on_member_remove")
            print(e)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            guildwelcomesettings = db.query(["SELECT value, flag FROM config WHERE setting = ? AND parent = ?", ["guild_welcome_settings", str(member.guild.id)]])
            if guildwelcomesettings:
                right_message = random.choice(guildwelcomesettings)
                channell = self.bot.get_channel(int(right_message[0]))
                await channell.send(await self.make_string(right_message[1], member))
        except Exception as e:
            print(time.strftime('%X %x %Z'))
            print("in on_member_join")
            print(e)

def setup(bot):
    bot.add_cog(Welcome(bot))