from pyrogram import Client as neural ,filters ,enums
from helpers.gpt import gpt
@neural.on_message( filters.private & filters.text)
async def ask_gpt(bot, msg):
    await msg.reply_chat_action(enums.ChatAction.TYPING)
    await msg.reply (gpt(m.text))
     

    

