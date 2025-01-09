import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")

intents = discord.Intents.default()
intents.members = True
intents.messages = True

# client = discord.Client(intents=intents)
# @client.event
# async def on_ready():
#   print("le bot est prêt")

# @client.event
# async def on_member_join(member: discord.Member):
#   general_channel: discord.TextChannel = client.get_channel(1314171884853661801)
#   await general_channel.send(content=f'Bienvenue sur le serveur {member.display_name}')

# @client.event
# async def on_message(message):
#   if message.content.lower() == "ping":
#     await message.channel.send("pong")
#   await client.process_commands(message)

# @client.event
# async def on_message(message):
#   if message.content.startswith("!del"):
#     number = int(message.content.split()[1])
#     messages = await message.channel.history(limit = number+1).flatten()

#     for msg in messages:
#       await msg.delete()
# client.run(os.getenv("TOKEN"))


class DocBot(commands.Bot):
  def __init__(self):
    intents = discord.Intents.default()
    intents.members = True
    super().__init__(command_prefix="/", intents=intents)

  async def on_ready(self):
    print(f"{self.user.display_name} est connecté au serveur")


bot = DocBot()
bot.run(os.getenv("TOKEN"))


