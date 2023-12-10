import asyncio
import random
from config import BOT_USERNAME, OWNER_ID
from pyrogram import Client, filters, enums
from Yumikoo import Yumikoo
from pyrogram.errors import MessageNotModified
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Yumikoo.Helper.yumikoo_text import ACTION_TEXT,AFK_TEXT,WELCOME_TEXT,GAMES_TEXT,IMAGES_TEXT,GROUP_TEXT,STICKER_TEXT,MISC_TEXT,EXTRA_TEXT,CHATGPT_TEXT,MUSIC_TEXT,WAIFU_TEXT       




# ------------------------------------------------------------------------------- #

START_IMG = (
"https://graph.org/file/f035f0e34969c14ae2e8c.jpg",
"https://graph.org/file/68227791cf9273fbede7a.jpg",
"https://graph.org/file/d91ec80b019d43082965d.jpg",
"https://graph.org/file/d6ae49af114fa50d5ba89.jpg",
"https://graph.org/file/30f6cc0b6251afe5c4153.jpg",
"https://telegra.ph/file/0214edaebad6ef6d69c1d.jpg",
"https://telegra.ph/file/f658925a255bea26efaa4.jpg",
"https://telegra.ph/file/235e4c7e9dd0c48bac638.jpg",

)



# ------------------------------------------------------------------------------- #

START_TEXT = """
**ʜᴇʏ ᴛʜᴇʀᴇ [{}](tg://user?id={}) ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !**
━━━━━━━━━━━━━━━━━━━━━━
**`๏ ɪ ᴀᴍ ˹𝗥ᴀsʜᴍɪᴋᴀ 𝗥ᴏʙᴏᴛ˼ ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs
๏ ɪ ᴀᴍ ᴅɪғғᴇʀᴇɴᴛ ғʀᴏᴍ ᴀɴᴏᴛʜᴇʀ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛs
`**
"""


# ------------------------------------------------------------------------------- #

HELP_TEXT = """**"""



# ------------------------------------------------------------------------------- #

Yumikoo_buttons = [              
                [
                    InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴀғᴋ", callback_data="afk_"),
                    InlineKeyboardButton("ᴡᴇʟᴄᴏᴍᴇ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ɢᴀᴍᴇs", callback_data="games_"),   
                    InlineKeyboardButton("ɪᴍᴀɢᴇs", callback_data="images_"),
                    InlineKeyboardButton("ɢʀᴏᴜᴘs", callback_data="groups_")
                ],
                [
                    InlineKeyboardButton("sᴛɪᴄᴋᴇʀ", callback_data="sticker_"),   
                    InlineKeyboardButton("ᴍɪsᴄ", callback_data="misc_"),
                    InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="extra_")
                ],
                [
                    InlineKeyboardButton("ᴄʜᴀᴛɢᴘᴛ", callback_data="chatgpt_"),   
                    InlineKeyboardButton("ᴡᴀɪғᴜ", callback_data="waifu_"),
                    InlineKeyboardButton("ᴍᴜsɪᴄ", callback_data="music_")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]


# ------------------------------------------------------------------------------- #


@Yumikoo.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client: Client, message: Message):
    buttons =  [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/abt_mei"),
                InlineKeyboardButton("ᴍᴀɪɴᴛᴀɪɴᴇʀ", url="https://t.me/i_dxlvir"),
            ],
            [
                InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_")
            ]    
        ]
                                    
    reply_markup = InlineKeyboardMarkup(buttons)
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_photo(
            photo=random.choice(START_IMG),
            caption=START_TEXT.format(message.from_user.first_name, message.from_user.id),
            reply_markup=reply_markup
        )
    else:
        btn = InlineKeyboardMarkup([[
            InlineKeyboardButton("ᴘᴍ ᴍᴇ", url=f"http://t.me/{BOT_USERNAME}?start")]])
        await message.reply(
            f"ʜᴇʏ {message.from_user.mention} ᴘᴍ ᴍᴇ ɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ.",
            reply_markup=btn
        )



# ------------------------------------------------------------------------------- #

@Yumikoo.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="home_":
        buttons =  [
            [
                InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/abt_mei"),
                InlineKeyboardButton("ʙᴏᴛ ᴍᴀᴋᴇʀ", url="https::/t.me/i_dxlvir"),
            ],
            [
                InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_")
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(Yumikoo_buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="action_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                ACTION_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
          
    elif query.data=="afk_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                AFK_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass




    elif query.data=="welcome_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                WELCOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
          
    elif query.data=="games_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                GAMES_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="images_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                IMAGES_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
          
    elif query.data=="groups_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                GROUP_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass




    elif query.data=="sticker_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                STICKER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
          
    elif query.data=="misc_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                MISC_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass




    elif query.data=="extra_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                EXTRA_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
          
    elif query.data=="chatgpt_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                CHATGPT_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


    elif query.data=="music_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                MUSIC_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
          
    elif query.data=="waifu_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                WAIFU_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


  
  
# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":
            await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass
          

