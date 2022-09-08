import discord
from discord.ext import commands

from functions.swift import swift_api
from functions.pnw import pnw_api
from functions.turncheck import turncheck
from functions.permissioncheck import rolecheck
from functions.sql import database
class vault(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addloan(self, ctx,loanname,loanamt,member:discord.Member = None):
        if rolecheck(ctx):
            discord_id = member.id
            db=database()
            db.addLoan(discord_id,loanname,loanamt)
            db.close(commit=True)
            embed = discord.Embed( description='Added Loan to Database', color=0xe60f0f)
        else:
            embed = discord.Embed( description='You dont have permission to do that, papa Davey will now spank you', color=0xe60f0f)
            await ctx.send(embed=embed)
    @commands.command()
    async def loans(self, ctx,member:discord.Member = None):
        if rolecheck(ctx):
            discord_id = member.id
            db=database()
            data = db.get('SELECT * FROM public."Loans" Where discord_id={discord_id};')
            db.close(commit=False)

            embed = discord.Embed( description= data, color=0xe60f0f)
        else:
            embed = discord.Embed( description='You dont have permission to do that, papa Davey will now spank you', color=0xe60f0f)
            await ctx.send(embed=embed)
    @commands.command()
    async def send(self, ctx, arg1: str='None', arg2: str='None'):
        if rolecheck(ctx):
            if not(arg1 == 'None' or arg2 == 'None'):
                api = swift_api()
                embed = discord.Embed( description=api.send(arg1, arg2), color=0xe60f0f)
                await ctx.send(embed=embed)
                api.logout()
            else:
                embed = discord.Embed( description='Invalid arguments', color=0xe60f0f)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed( description='You dont have permission to do that, papa Davey will now spank you', color=0xe60f0f)
            await ctx.send(embed=embed)
    @commands.command()
    async def code(self, ctx):
        if rolecheck(ctx):
            api = swift_api()
            embed = discord.Embed(title="New Swift Deposit Code:", description=api.depositcode(), color=0xe60f0f)
            await ctx.send(embed=embed)
            api.logout()
        else:
            embed = discord.Embed( description='You dont have permission to do that, papa Davey will now spank you', color=0xe60f0f)
            await ctx.send(embed=embed)
    @commands.command()
    async def depo(self, ctx):
        if rolecheck(ctx):
            api = swift_api()
            embed = discord.Embed(title="Current Balance:", description=api.balance() , color=0xe60f0f)
            await ctx.send(embed=embed)
            api.logout()
        else:
          embed = discord.Embed( description='You dont have permission to do that, papa Davey will now spank you', color=0xe60f0f)
          await ctx.send(embed=embed)
    @commands.command()
    async def tran(self, ctx):
        if rolecheck(ctx):
            api = swift_api()
            embed = discord.Embed(title="Recent Transactions:", description=api.transactions() , color=0xe60f0f)
            await ctx.send(embed=embed)
            api.logout()
        else:
            embed = discord.Embed( description='You dont have permission to do that, papa Davey will now spank you', color=0xe60f0f)
            await ctx.send(embed=embed)
    @commands.command()
    async def offshore(self, ctx, arg1: str='None'):
        if rolecheck(ctx):
            swift = swift_api()
            pnw= pnw_api()
            tc=turncheck()
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
        else:
           embed = discord.Embed( description='You dont have permission to do that, papa Davey will now spank you', color=0xe60f0f)
           await ctx.send(embed=embed)
    @commands.Cog.listener()
    async def on_ready(self):
        pass

def setup(bot):
    bot.add_cog(vault(bot))
