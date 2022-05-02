from Yashvi import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


@Client.on_message(filters.private & filters.incoming & filters.command("cmda"))
async def _cmda(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.CMDA,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
