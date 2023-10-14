from pyrogram import Client as neural ,filters
from helpers.buttons import *
@neural.on_message( filters.command("start"))
async def start(bot, msg):
    markup = InlineKeyboardMarkup([[channel, group], [developer,help]])
    await msg.reply(f"**Hello {msg.from_user.first_name} I'm ChatGPT turbo 3.5 Telegram Bot powered by openai,you can ask me anything **",
    reply_markup= markup )
