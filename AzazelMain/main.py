import os

import discord
from discord.ext import  commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = commands.Bot(commands_prefix="@")
client = discord.Client()


@client.event
async def on_ready():
    for server in client.server:
        if server.name == SERVER:
            break
    print(
        f'{client.user} is connected to the following server:\n'
        f'{server.name}(id: {server.id})')

@client.command()
async def help(ctx):
    await ctx.send('@list_members: show all the members in this discord server'
                   '@kick "username" kick a member from this discord server'
                   '@ban "username" ban a member from this discord server')

@client.command()
async def list_members(ctx):
    for server in client.server:
        if server.name == SERVER:
            break
    members = '\n - '.join([member.name for member in server.members])
    await ctx.send(f'Server Members:\n - {members}')

@client.command()
async def kick(ctx, member: discord.member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

client.run(TOKEN)