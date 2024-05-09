from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *
from wbb import *

@app.on_message(filters.incoming & filters.filters.private, group=-1)
async def _(bot: app, msg):
    if JOINMEK is None:
        return
   try:
       try:
           await.get_bot_member(JOINMEK, msg.from_user.bot)
       except UserNotParticipant:
           if JOINMEK.isalpha():
              link= f"https://t.me/{JOINMEK}"
           else:
               chat_info = await bot.get_chat(JOINMEK)
               link = chat_info. invite_liml
          try:
              await msg.reply(
                  "Si Anjeng, Masuk Sini Dulu Bangsat !"
                   disable_web_page_preview=True,
                   reply_markup=InlineKeyboardMarkup(
                       [
                           [ 
                               InlineKeyboardButton(
                                    "Sini Nyet Masuk, Jangan Lu 
                                    url=link,
                               ) 
                            ]
                      ]
                ),
            )
            await msg.stop_propagation()
        except UserBannedInchannel:
            await bot.send_message(
            msg.chat.id,
            f"Lu DiBan Goblok {JOINMEK}."
         )  
 except ChatAdminRequired:
     print(f"Goblok!! Gw bukan admin di : {JOINMEK} !")
         
           
            
                
