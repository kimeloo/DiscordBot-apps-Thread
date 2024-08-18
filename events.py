from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os
import logging
logger = logging.getLogger("event")

class Events():
    def __init__(self, bot):
        self.__CHANNEL_ID_discussion = int(os.getenv('CHANNEL_DISCUSSION'))
        self.bot = bot
    
    def add(self):
        return self.__events(self.bot)

    def __events(self, bot):
        @bot.event
        async def on_ready():
            logger.info(f'Logged in as {bot.user.name}')

        @bot.event
        async def on_raw_reaction_add(payload):
            channel = await bot.fetch_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            emoji = payload.emoji
            if (channel.name == 'idea') or (channel.parent.name == 'idea'):
                if emoji.name == "✅":
                    logger.info(f'Reaction {emoji.name} on [{message.content}]')
                    discussion_channel = bot.get_channel(self.__CHANNEL_ID_discussion)
                    new_message = await discussion_channel.send(message.content)
                    thread = await new_message.create_thread(name=message.content, auto_archive_duration=10080)
                    logger.info(f'Created [{message.content}] thread.')

                    seoul_tz = ZoneInfo('Asia/Seoul')
                    creation_time = datetime.now(seoul_tz)
                    archive_time = creation_time + timedelta(days=7)
                    creation_time = creation_time.strftime("%Y-%m-%d %H:%M:%S")
                    archive_time = archive_time.strftime("%Y-%m-%d %H:%M:%S")
                    await thread.send(f"@everyone\n Created : {creation_time} (UTC+9)\nArchived : {archive_time} (UTC+9).")
                    logger.info(f'Thread archive time : {archive_time} (UTC+9)')
        return bot