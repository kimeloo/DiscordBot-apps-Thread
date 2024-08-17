import discord
from discord.ext import commands as discord_commands
import os
from .commands import Commands as mycommands
from .events import Events as myevents
import logging
logger = logging.getLogger("bot")

class ThreadBot():
    def __init__(self):
        self.__TOKEN = os.getenv('DISCORD_BOT_TOKEN')
        # self.__CHANNEL_ID_discussion = os.getenv('CHANNEL_DISCUSSION')
        self.__create_bot()
    
    def __create_bot(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.reactions = True
        
        bot = discord_commands.Bot(command_prefix='!', intents=intents)
        bot = myevents(bot).add()
        bot = mycommands(bot).add()
        self.bot = bot
    
    def run(self):
        if self.__TOKEN:
            self.bot.run(self.__TOKEN)
        else:
            logger.error("Token not found.")

if __name__ == '__main__':
    logger.warning("Do not run this file directly.")