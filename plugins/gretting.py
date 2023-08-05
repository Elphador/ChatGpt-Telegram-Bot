from pyrogram import Client as neural ,filters
from helpers.buttons import *
from pyrogram.types import *
@neural.on_message( filters.command("start"))
async def start(bot, msg):
    markup = InlineKeyboardMarkup([[channel, group], [developer,help]])
    await msg.reply(f"**Hello {msg.from_user.first_name} I'm ChatGPT turbo 3.5 open source Telegram Bot powered by Neurals,you can ask me anything\nclick help for more **",
    reply_markup= markup )
