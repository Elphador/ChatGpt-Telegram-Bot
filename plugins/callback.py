from pyrogram import Client as neural
from helpers.text import *

@neural.on_callback_query() 
async def calls(_,update):
    chat_id = update.message.chat.id; call = update.data
    if call == "help":
        await update.message.reply(HELP)
    else :
        pass