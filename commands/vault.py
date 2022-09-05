import discord
from discord.ext import commands

from functions.swift import swift_api
from functions.pnw import pnw_api
from functions.turncheck import turncheck

class vault(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def send(self, ctx, arg1: str='None', arg2: str='None'):
        if not(arg1 == 'None' or arg2 == 'None'):
            api = swift_api()
            embed = discord.Embed( description=api.send(arg1, arg2), color=0xe60f0f)
            await ctx.send(embed=embed)
            api.logout()
        else:
            embed = discord.Embed( description='Invalid arguments', color=0xe60f0f)
    
    @commands.command()
    async def code(self, ctx):
        api = swift_api()
        embed = discord.Embed(title="New Swift Deposit Code:", description=api.depositcode(), color=0xe60f0f)
        await ctx.send(embed=embed)
        api.logout()
    
    @commands.command()
    async def depo(self, ctx):
        api = swift_api()
        embed = discord.Embed(title="Current Balance:", description=api.balance() , color=0xe60f0f)
        await ctx.send(embed=embed)
        api.logout()
    
    @commands.command()
    async def tran(self, ctx):
        api = swift_api()
        embed = discord.Embed(title="Recent Transactions:", description=api.transactions() , color=0xe60f0f)
        await ctx.send(embed=embed)
        api.logout()
    
    @commands.command()
    async def offshore(self, ctx, arg1: str='None'):
        swift = swift_api()
        pnw= pnw_api()
        tc=checktime()
        if tc=="Success":
            pnwdepo = pnw.pnwdepo(arg1)
            if pnwdepo == "Sucess":
                depositcode = swift.depositcode()
                offshoring = pnw.pnwsendswift(arg1,depositcode)
                if offshoring == "Sucess":
                    embed = discord.Embed(title="Sucess", description=arg1 , color=0xe60f0f)
                    await ctx.send(embed=embed)
                else: 
                    embed = discord.Embed(title=offshoring , color=0xe60f0f)
                    await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=pnwdepo , color=0xe60f0f)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=tc , color=0xe60f0f)
                await ctx.send(embed=embed)
        swift.logout()

    @commands.Cog.listener()
    async def on_ready(self):
        pass

def setup(bot):
    bot.add_cog(vault(bot))
