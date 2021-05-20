import discord
import discord_slash
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
from utils import get_env_vars
from messages import commands

server_ids, role_id, bot_token = get_env_vars() # Get Variables from Environmental Variables

client = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

quest_roles = []

for server in server_ids: 

    quest_roles += [
        create_permission(role_id, SlashCommandPermissionType.ROLE, True), # Lumenaut | Custom Role with Permissions from env var
        create_permission(server, SlashCommandPermissionType.ROLE, False),  # Everyone | everyone role ID = Server ID 
    ]

@client.event
async def on_ready():
    print("Ready!")

for command in commands:
    function_name = f"_{command}"
    @slash.slash(name=command, guild_ids=server_ids,
                description=f"{commands[command][:97]}...")
    async def function_name(ctx):
        await ctx.send(f"{commands[ctx.command.upper()]}")

client.run(bot_token)
