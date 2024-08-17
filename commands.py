import logging
logger = logging.getLogger("commands")

class Commands():
    def __init__(self, bot):
        self.bot = bot
    
    def add(self):
        return self.__commands(self.bot)
    
    def __commands(self, bot):
        @bot.command()
        async def ping(ctx):
            send_message = 'pong'
            logger.info("[{:>8}] : {}".format("Recieved", ctx.message.content))
            await ctx.channel.send(send_message)
            logger.info("[{:>8}] : {}".format("Sent", send_message))
        return bot