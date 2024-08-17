import logging
logger = logging.getLogger("thread")

def run():
    # load bot token
    from . import config
    config.Config()

    # run bot
    from . import bot
    bot_ = bot.ThreadBot()
    bot_.run()

if __name__ == '__main__':
    run()