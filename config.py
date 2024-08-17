import os
from dotenv import load_dotenv, find_dotenv
import logging
logger = logging.getLogger("config")

class Config():
    def __init__(self):
        self.__load_env()
        logger.info(".env loaded.")
    
    def __check_env(self):
        dotenv_file = find_dotenv()
        logger.debug(".env found.")
        return dotenv_file

    def __load_env(self):
        dotenv_file = self.__check_env()
        if dotenv_file:
            load_dotenv(dotenv_file)
            try:
                os.environ['DISCORD_BOT_TOKEN']
                os.environ['CHANNEL_DISCUSSION']
                return
            except KeyError:
                logger.debug(".env - DISCORD_BOT_TOKEN not found.")
        logger.debug("generating .env file.")
        self.__gen_dotenv()
    
    def __gen_dotenv(self):
        logger.warning("Cannot find your token or .env file !")
        logger.info("Making your .env file...")
        TOKEN = input("Paste your Discord Bot Token >> ")
        CHANNEL_DISCUSSION = input("Paste your Discussion Channel ID >> ")
        with open('./.env', 'a') as envFile:
            envFile.write(f'\n# This file contains your secret!!\n# Be careful when you share this project.\n\nDISCORD_BOT_TOKEN = {TOKEN}\nCHANNEL_DISCUSSION = {CHANNEL_DISCUSSION}')
        logger.info("Token saved in .env file !")
        logger.info("Be careful when you share this project.")

if __name__ == '__main__':
    logger.warning("Do not run this file directly.")