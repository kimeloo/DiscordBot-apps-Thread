import logging
logger = logging.getLogger(__name__)

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