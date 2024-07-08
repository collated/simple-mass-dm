import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

# change prefix to your desire, default is $

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True,send_messages=True, read_messages=True)
async def dm_all(ctx, *, message: str):
    print("Executing dm_all command...")   # prints on the terminal when the command commences
    successful = 0
    failed = 0
    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
                successful += 1
                print(f"Sent message to {member.name}")
            except Exception as e:
                failed += 1
                print(f"Could not send message to {member.name}: {e}")
            await asyncio.sleep(0.8)

            # adjust speed of the mass dm to your desire, i usually go either 0.1 or 0.8

    await ctx.send(f"Message sent to {successful} members, failed to send to {failed} members.")

bot.run('BOT TOKEN')  # put ur bot token here
