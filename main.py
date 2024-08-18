import logging
logger = logging.getLogger("thread")

def run(bot):
    from ..config import Config
    Config('CHANNEL_DISCUSSION')

    from .events import Events as myevents
    bot = myevents(bot).add()
    from .commands import Commands as mycommands
    bot = mycommands(bot).add()

    return bot

if __name__ == '__main__':
    print('Do not run this file directly')