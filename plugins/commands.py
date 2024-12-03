import os
import logging
import random
import asyncio
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import *
#5 => verification_steps ! [Youtube@LazyDeveloperr]
from utils import check_verification, get_token, verify_user, check_token, get_settings, get_size, is_subscribed, save_group_settings, temp
from database.connections_mdb import active_connection
import pytz
import datetime
from utils import get_seconds, get_tutorial, get_shortlink
from database.users_chats_db import db 
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
import re
import json
import base64
logger = logging.getLogger(__name__)

BATCH_FILES = {}

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if message.from_user.id in ADMINS:
            buttons = [
                [
                    InlineKeyboardButton('🔍 Group', url=f'https://t.me/{MOVIE_GROUP_USERNAME}')
                ],
                [
                    InlineKeyboardButton('🙆🏻 Hᴇʟᴘ 🦾', url=f"https://t.me/{temp.U_NAME}?start=help"),
                ],[
                InlineKeyboardButton('⪦ 𝕄𝕆𝕍𝕀𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ⪧', url='https://t.me/movierhttps://t.me/MOVIE_MINES_GROUP')
                ],[
                InlineKeyboardButton('💸 E𝐚𝐫𝐧 M𝐨𝐧𝐞𝐲 💸', callback_data="shortlink_info")
                ],
                [
                    InlineKeyboardButton(text=DOWNLOAD_TEXT_NAME,url=DOWNLOAD_TEXT_URL)
                ]
                ]
        else:
            buttons = [
                [
                    InlineKeyboardButton('🔍 Group', url=f'https://t.me/{MOVIE_GROUP_USERNAME}')
                ],
                [
                    InlineKeyboardButton('🙆🏻 Hᴇʟᴘ 🦾', url=f"https://t.me/{temp.U_NAME}?start=help"),
                ],[
                InlineKeyboardButton('⪦ 𝕄𝕆𝕍𝕀𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ⪧', url='https://t.me/MOVIE_MINES_GROUP')
                ],
                [
                    InlineKeyboardButton(text=DOWNLOAD_TEXT_NAME,url=DOWNLOAD_TEXT_URL)
                ]
                ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/LazyDeveloperr/LazyPrincess/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        if message.from_user.id in ADMINS:
            buttons = [[
                InlineKeyboardButton('↖️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs ↗️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                ],[
                InlineKeyboardButton('🧞‍♀️ Sᴇᴀʀᴄʜ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('🔍 Gʀᴏᴜᴘ', url=f'https://t.me/{MOVIE_GROUP_USERNAME}')
                ],[
                InlineKeyboardButton('🙆🏻 Hᴇʟᴘ ', callback_data='help'),
                InlineKeyboardButton('🎁 Hᴇʟᴘ++', callback_data='leech_url_help'),
                ],[
                InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='openSettings'),
                InlineKeyboardButton('♥️ Aʙᴏᴜᴛ', callback_data='about')
                ],[
                InlineKeyboardButton('⪦ 𝕄𝕆𝕍𝕀𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ⪧', url='https://t.me/MOVIE_MINES_GROUP')
                ],[
                InlineKeyboardButton('💸 E𝐚𝐫𝐧 M𝐨𝐧𝐞𝐲 💸', callback_data="shortlink_info")
                ]]
        else:
            buttons = [[
                InlineKeyboardButton('↖️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs ↗️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                ],[
                InlineKeyboardButton('🧞‍♀️ Sᴇᴀʀᴄʜ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('🔍 Gʀᴏᴜᴘ', url=f'https://t.me/{MOVIE_GROUP_USERNAME}')
                ],[
                InlineKeyboardButton('🙆🏻 Hᴇʟᴘ ', callback_data='help'),
                InlineKeyboardButton('🎁 Hᴇʟᴘ++', callback_data='leech_url_help'),
                ],[
                InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='openSettings'),
                InlineKeyboardButton('♥️ Aʙᴏᴜᴛ', callback_data='about')
                ],[
                InlineKeyboardButton('⪦ 𝕄𝕆𝕍𝕀𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ⪧', url='https://t.me/MOVIE_MINES_GROUP')
                ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL), creates_join_request=True)
        except ChatAdminRequired:
            logger.error("Hey Sona, Ek dfa check kr lo ki main Channel mei Add hu ya nhi...!")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "🤖 Join Updates Channel", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            try:
                kk, file_id = message.command[1].split("_", 1)
                pre = 'checksubp' if kk == 'filep' else 'checksub' 
                btn.append([InlineKeyboardButton(" 🔄 Try Again", callback_data=f"{pre}#{file_id}")])
            except (IndexError, ValueError):
                btn.append([InlineKeyboardButton(" 🔄 Try Again", url=f"https://t.me/{temp.U_NAME}?start={message.command[1]}")])
        await client.send_message(
            chat_id=message.from_user.id,
            text="""▲ Join our updated channel below. bot will not give you movie until you join from our update channel...\n

A கீழே உள்ள எங்கள் புதுப்பிக்கப்பட்ட சேனலில் சேரவும். எங்கள் புதுப்பிப்பு சேனலில் நீங்கள் சேரும் வரை போட் உங்களுக்கு திரைப்படத்தை வழங்காது...\n

4 ਹੇਠਾਂ ਸਾਡੇ ਅਪਡੇਟ ਕੀਤੇ ਚੈਨਲ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ। ਬੋਟ ਤੁਹਾਨੂੰ ਉਦੋਂ ਤੱਕ ਮੂਵੀ ਨਹੀਂ ਦੇਵੇਗਾ ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ ਸਾਡੇ ਅਪਡੇਟ ਚੈਨਲ ਤੋਂ ਸ਼ਾਮਲ ਨਹੀਂ ਹੋ तांरे...\n

4 ചുവടെയുള്ള ഞങ്ങളുടെ അപ്ഡേറ്റ് ചെയ്ത ചാനലിൽ ചേരുക. ഞങ്ങളുടെ അപ്ഡേറ്റ് ചാനലിൽ നിന്ന് നിങ്ങൾ ചേരുന്നത് വരെ ബോട്ട് നിങ്ങൾക്ക് സിനിമ നൽകില്ല....\n

▲ हमारे निचे दिए गये update चैनल को join करे जब तक आप हमारे update चैनल को join नहीं करेंगे तब तक bot आपको मूवी नहीं देगा...""",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        if message.from_user.id in ADMINS:
            buttons = [[
                InlineKeyboardButton('↖️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs ↗️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                ],[
                InlineKeyboardButton('🧞‍♀️ Sᴇᴀʀᴄʜ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('🔍 Gʀᴏᴜᴘ', url=f'https://t.me/{MOVIE_GROUP_USERNAME}')
                ],[
                InlineKeyboardButton('🙆🏻 Hᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('🎁 Hᴇʟᴘ++ ', callback_data='leech_url_help'),
            ],[
                InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='openSettings'),
                InlineKeyboardButton('♥️ Aʙᴏᴜᴛ', callback_data='about')
                ],
            [
                InlineKeyboardButton('⪦ 𝕄𝕆𝕍𝕀𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ⪧', url='https://t.me/MOVIE_MINES_GROUP')
            ],
            [
                InlineKeyboardButton('💸 E𝐚𝐫𝐧 M𝐨𝐧𝐞𝐲 💸', callback_data="shortlink_info")
            ]
            ]
        else:
            buttons = [[
            InlineKeyboardButton('↖️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs ↗️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🧞‍♀️ Sᴇᴀʀᴄʜ', switch_inline_query_current_chat=''),
            InlineKeyboardButton('🔍 Gʀᴏᴜᴘ', url=f'https://t.me/{MOVIE_GROUP_USERNAME}')
            ],[
            InlineKeyboardButton('🙆🏻 Hᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('🎁 Hᴇʟᴘ++ ', callback_data='leech_url_help'),
            ],[
                InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='openSettings'),
                InlineKeyboardButton('♥️ Aʙᴏᴜᴛ', callback_data='about')
                ],
            [
                InlineKeyboardButton('⪦ 𝕄𝕆𝕍𝕀𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ⪧', url='https://t.me/MOVIE_MINES_GROUP')
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    data = message.command[1]
    try:
        pre, file_id = data.split('_', 1)
    except:
        file_id = data
        pre = ""
    if data.split("-", 1)[0] == "BATCH":
        sts = await message.reply("Please wait")
        file_id = data.split("-", 1)[1]
        msgs = BATCH_FILES.get(file_id)
        if not msgs:
            file = await client.download_media(file_id)
            try: 
                with open(file) as file_data:
                    msgs=json.loads(file_data.read())
            except:
                await sts.edit("FAILED")
                return await client.send_message(LOG_CHANNEL, "UNABLE TO OPEN FILE.")
            os.remove(file)
            BATCH_FILES[file_id] = msgs
        for msg in msgs:
            title = msg.get("title")
            size=get_size(int(msg.get("size", 0)))
            f_caption=msg.get("caption", "")
            if BATCH_FILE_CAPTION:
                try:
                    f_caption=BATCH_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
                except Exception as e:
                    logger.exception(e)
                    f_caption=f_caption
            if f_caption is None:
                f_caption = f"{title}"
            
            # check verfication start
            # try:
            #     print('A user hit this case....')
            #     zab_user_id = message.from_user.id
            #     if IS_LAZYUSER_VERIFICATION and not await db.has_prime_status(zab_user_id) and not await check_verification(client, zab_user_id):
            #         lazy_url = await get_token(client, zab_user_id, f"https://telegram.me/{temp.U_NAME}?start=")
            #         lazy_verify_btn = [[
            #             InlineKeyboardButton("✅ Verify ✅", url=lazy_url)
            #         ]]
            #         await message.reply_text(
            #             text="You are not verified user ! please verify to get unlimited files or simply you can buy premium",
            #             reply_markup=InlineKeyboardMarkup(lazy_verify_btn)
            #         )
            #         return
            # except Exception as e:
            #     print(f"Exception occured : {str(e)}")
            # ./check verfication end
            # LAZY_DIVERTING_CHANNEL_ID = int(environ.get('LAZY_DIVERTING_CHANNEL_ID', '-1004873483784 -10028934982 -1009389843894 -10048934898934').split())
            select_random_channel = random.choice(LAZY_DIVERTING_CHANNEL_ID)
            SELECTED_CHANNEL = int(select_random_channel)
            
            along_with_lazy_info = "**⚠ DELETING IN 10 minute ⚠**"
            along_with_lazy_footer = f"**Dear {message.from_user.mention}"
            lazy_caption_template =f"{along_with_lazy_info}\n\n{f_caption}\n\n{along_with_lazy_footer}"
            try:
                # print(f'bot is trying to send file to the selected random channel : {SELECTED_CHANNEL}')
                lmsg = await client.send_cached_media(
                    chat_id=SELECTED_CHANNEL,
                    file_id=msg.get("file_id"),
                    caption=lazy_caption_template,
                    protect_content=msg.get('protect', False),
                    )
                # print(f'File sent to : {SELECTED_CHANNEL}')
                invite_link = await client.create_chat_invite_link(int(SELECTED_CHANNEL))
                lazy_invite_url = invite_link.invite_link
                # print(lazy_invite_url)

                message_link = await client.get_messages(int(SELECTED_CHANNEL), lmsg.id)
                file_link = message_link.link
                # print(file_link)
                try:
                    member = await client.get_chat_member(SELECTED_CHANNEL, message.from_user.id)
                    # print(member)
                    if member.status != enums.ChatMemberStatus.MEMBER:
                        fusss = await client.send_message(
                        chat_id=message.from_user.id,
                        text=f"🎉 File Uploaded here ✅\n\nHere is the channel link - Join & Get file 👇\n\n **{lazy_invite_url}**\n\n⚠Note: Dear {message.from_user.mention}, if you stay subscribed to the channel, you will receive direct links next time ❤"
                        )
                        # print(f'User is not subscribed: Got url => {lazy_invite_url}')
                    else:
                        fasss = await client.send_message(
                        chat_id=message.from_user.id,
                        text=f"🎉You're already a channel member🎊\n\nHere is your direct download link 👇\n\n {file_link} \n\n❤Thank you for staying with the channel, {message.from_user.mention}❤"
                        )
                        # print(f'User is subscribed: Got LINK => {file_link}')
                except UserNotParticipant:
                    fasssg = await client.send_message(
                        chat_id=message.from_user.id,
                        text=f"🎉 File Uploaded here ✅\n\nHere is the channel link - Join & Get file 👇\n\n **{lazy_invite_url}**\n\n⚠Note: Dear {message.from_user.mention}, if you stay subscribed to the channel, you will receive direct links next time ❤"
                    )
                    # print(f'User is not subscribed: Got url => {lazy_invite_url}')
                await asyncio.sleep(600)
                await lmsg.delete()
                await fusss.delete()
                await fasss.delete()
                await fasssg.delete()

                # await client.send_cached_media(
                #     chat_id=message.from_user.id,
                #     file_id=msg.get("file_id"),
                #     caption=f_caption,
                #     protect_content=msg.get('protect', False),
                #     )
            except FloodWait as e:
                await asyncio.sleep(e.x)
                logger.warning(f"Floodwait of {e.x} sec.")
                await client.send_cached_media(
                    chat_id=message.from_user.id,
                    file_id=msg.get("file_id"),
                    caption=f_caption,
                    protect_content=msg.get('protect', False),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('▶ Gen Stream / Download Link', callback_data=f'generate_stream_link:{file_id}'),
                            ],
                            [
                                InlineKeyboardButton('📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌', url=f'https://t.me/LazyDeveloperr')
                            ]
                        ]
                    )
                    )
            except Exception as e:
                logger.warning(e, exc_info=True)
                continue
            await asyncio.sleep(1) 
        await sts.delete()
        return
    elif data.split("-", 1)[0] == "DSTORE":
        sts = await message.reply("Please wait")
        b_string = data.split("-", 1)[1]
        decoded = (base64.urlsafe_b64decode(b_string + "=" * (-len(b_string) % 4))).decode("ascii")
        try:
            f_msg_id, l_msg_id, f_chat_id, protect = decoded.split("_", 3)
        except:
            f_msg_id, l_msg_id, f_chat_id = decoded.split("_", 2)
            protect = "/pbatch" if PROTECT_CONTENT else "batch"
        diff = int(l_msg_id) - int(f_msg_id)
        async for msg in client.iter_messages(int(f_chat_id), int(l_msg_id), int(f_msg_id)):
            if msg.media:
                media = getattr(msg, msg.media.value)
                if BATCH_FILE_CAPTION:
                    try:
                        f_caption=BATCH_FILE_CAPTION.format(file_name=getattr(media, 'file_name', ''), file_size=getattr(media, 'file_size', ''), file_caption=getattr(msg, 'caption', ''))
                    except Exception as e:
                        logger.exception(e)
                        f_caption = getattr(msg, 'caption', '')
                else:
                    media = getattr(msg, msg.media.value)
                    file_name = getattr(media, 'file_name', '')
                    f_caption = getattr(msg, 'caption', file_name)
                try:
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, caption=f_caption, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            elif msg.empty:
                continue
            else:
                try:
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await msg.copy(message.chat.id, protect_content=True if protect == "/pbatch" else False)
                except Exception as e:
                    logger.exception(e)
                    continue
            await asyncio.sleep(1) 
        return await sts.delete()
    
    #6 => verification_steps ! [Youtube@LazyDeveloperr]
    elif data.split("-", 1)[0] == "verify":
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        if str(message.from_user.id) != str(userid):
            return await message.reply_text(
                text="<b>Invalid link or Expired link !</b>",
                protect_content=True
            )
        is_valid = await check_token(client, userid, token)
        if is_valid == True:
            await message.reply_text(
                text=f"<b>Hey {message.from_user.mention}, You are successfully verified !\nNow you have unlimited access for all movies till today midnight.</b>",
                protect_content=True
            )
            await verify_user(client, userid, token)
        else:
            return await message.reply_text(
          
