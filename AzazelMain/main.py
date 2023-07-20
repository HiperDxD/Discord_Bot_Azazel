import os

import discord
from discord.ext import  commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()
client = commands.Bot(commands_prefix="@")

@client.event
async def on_ready():
    for server in client.server:
        if server.name == SERVER:
            break
    print(
        f'{client.user} is connected to the following server:\n'
        f'{server.name}(id: {server.id})')

@client.command()
async def list_members(ctx):
    for server in client.server:
        if server.name == SERVER:
            break
    members = '\n - '.join([member.name for member in server.members])
    await ctx.send(f'Server Members:\n - {members}')

client.run(TOKEN)