# Credit @LazyDeveloper.
# Please Don't remove credit.
# Born to make history @LazyDeveloper !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @LazyDeveloperr  🥰
# for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 
# rip paid developers 🤣 - >> No need to buy paid source code while @LazyDeveloperr is here 😍😍
# with Love @LazyDeveloperr 💘
# Subscribe YT @LazyDeveloperr - to learn more about this for free...

import asyncio
import re
import ast
import math
import pytz
import random
from urllib.parse import quote
from datetime import datetime, timedelta, date, time
lock = asyncio.Lock()
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from database.connections_mdb import active_connection, all_connections, delete_connection, if_active, make_active, \
    make_inactive
from info import *
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ForceReply, Message
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results,get_search_results_badAss_LazyDeveloperr
from database.lazy_utils import progress_for_pyrogram, convert, humanbytes
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import os 
from Script import script
import humanize
from PIL import Image
import time
from utils import get_shortlink
from database.filters_mdb import (
    del_all,
    find_filter,
    get_filters,
)
from util.human_readable import humanbytes
from plugins.settings.settings import OpenSettings
from plugins.dl_button import ddl_call_back
from plugins.yt_lazy_dl_btn import youtube_dl_call_back
from urllib.parse import quote_plus
from util.file_properties import get_name, get_hash, get_media_file_size
import logging
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LAZYS_FILE_ID = "CAACAgUAAxkBAAEQ2YpljSvD5sq-Flkm9TV8afTGo7Kr4gACgwMAAjO28FeYSaGKzSOuUTME CAACAgIAAxkBAAEQ2ppljXqrYNVEN_hsFrm72H_tJvwZEQACdgUAAj-VzApFV7w2VozN3TME CAACAgIAAxkBAAEQ2pxljXr88eSrY-fNSv8tWqTsKQXSTwACWgUAAj-VzAobFrmFvSDDnTME CAACAgUAAxkBAAEQ2p5ljXsOArpCEAIuyF_X-cjbcq8y9wACUQMAAn4--FdPtUqUKQy6njME CAACAgUAAxkBAAEQ2qJljXtSW5xxVc0xk6J4dx1TIcReXQACOggAAibGUFalOk-a8Gmc2TME CAACAgIAAxkBAAEQ2qZljXt7emeVhLmGav1fiCUbTVKK6AACyRIAAmA0gEtb-P-xaa3sxjME CAACAgIAAxkBAAEQ2qhljXuRfi61G-Th8T9R7AIO_E-GFQACgBgAAsC2UEmimzNNrlDPPDME CAACAgIAAxkBAAEQ2qpljXuwpjQsCWqkR190gR6vSLrjpgAC7hQAAuNVUEk4S4qtAhNhvDME CAACAgIAAxkBAAEQ2qxljXvF9LzAOBwWqqGxYghZBptPFwACXgUAAj-VzAqq1ncTLO-MOTME CAACAgUAAxkBAAEQ2q5ljXvfjuP7GSEGy5LOIubDdZD24wACdAQAAg0N-VchhV4I8_I1XjME CAACAgUAAxkBAAEQ2rBljXvzM7MpUVZcpRkiYGPiG89UJgACeAMAAqZh-FfxCTpwVzCOEzME CAACAgUAAxkBAAEQ2rJljXwNvgcYFau24iQ57pNx72IbyAACdQQAAmh1-Ffusjt1plc9YzME CAACAgUAAxkBAAEQ2rRljXwhXX-JMs8GFzz2QZRxdUk9lAADBAACXtDwV04PGDy02iQAATME CAACAgUAAxkBAAEQ2rZljXwsAAEr4nU50WP3Hz_0HCxmYSwAAuwDAAISQflXYznjU3iGTvkzBA CAACAgIAAxkBAAEQ2rhljXxPS3Qd-BV9RnA_0OwPiKsSCQACdwUAAj-VzApljNMsSkHZTjME CAACAgIAAxkBAAEQ2rxljXxsaNqc3gMhzW7FovMiXOvYnQAC-hMAAtSF8Etb7jRObi-mqzME CAACAgUAAxkBAAEQ2sBljXzQxfyPIRI4ch3cHPk-rsCzpQACowkAAonICFTwfKVoynUZvzME CAACAgUAAxkBAAEQ2sJljXzqbHl83Fv7n3m0HfNHBrho4QACCwoAAi7EUVfwywxU4Qq7_jME CAACAgUAAxkBAAEQ2sRljXz-3uxQIFRstS3R5W-y0dC5qgAC5QUAAruXSFaWNURJP7tfwjME CAACAgQAAxkBAAEQ2sZljX0jh3vLtJpWZcxxj5bay9t-ZAACKxAAAk1zwFPGlaV1QZjTkTME CAACAgUAAxkBAAEQ23pljX7l5QqJeF5D5N3HZzH11wKW-AAC_QMAAhOM-FfHw6MTc_AX9TME CAACAgUAAxkBAAEQ23hljX7ivAeA9bzizIEtO1zLWdR3cgACQQQAAu-M8FelaJ5dHSa2IjME CAACAgUAAxkBAAEQ23ZljX7g-mO-JJ_zXANWQP_Iu0XSdwADBAACXtDwV04PGDy02iQAATME CAACAgUAAxkBAAEQ23RljX7d5-rssmw93XU3X7DFQ2eQnAACAQQAAjcM8Vc5TYjCrZcv9jME CAACAgIAAxkBAAEQ23BljX7TxvX88ZWgmaCtC69e8oRFtwACyxQAAt2wUUlMYGw0MqQdYTME CAACAgIAAxkBAAEQ225ljX7SHE230w8XkqVhWGnCZCaEywACmxgAApd_GUmWaHhj5QhlhDME CAACAgIAAxkBAAEQ22xljX7NXu_n0gWTgdJbO2WV6LqwCQACFBUAAuCUyEl75qEC_trvQjME CAACAgIAAxkBAAEQ22pljX7LVSnENXQzGww9r62wOqSj8QACYRQAArT6gEs6giPSo52pzjME CAACAgIAAxkBAAEQ22hljX7FZhbAOn2M_Jv_b4_Ekfu4fQACMBMAAuMikUvBPXzxtKbSdTME CAACAgUAAxkBAAEQ22ZljX7BfFC_nYdWmtu05FPnFPnwsAACoQYAAqReUFYvH5-81YCd2TME CAACAgIAAxkBAAEQ22RljX6qPHWpw3uMFsRZThYk7ed1VAACNAADpsrIDFFqS0RzOZ6RMwQ CAACAgIAAxkBAAEQ22JljX6oYwU5DK4iqQOhHKPIJmdItAACNwADpsrIDAe-9Dzoj1lFMwQ CAACAgIAAxkBAAEQ22BljX6mqfCiiq4lkzCy5arscT9chQACMAADpsrIDN5j5wS_ajpFMwQ CAACAgIAAxkBAAEQ215ljX6lCDcQW-CdfWoP82uwvJ-d5gACPQADpsrIDG9X2CRSFUdMMwQ CAACAgIAAxkBAAEQ21xljX6hzov-plccFYwdhZLjCtERtwACYgMAArrAlQUGVK1U7t1DvjME CAACAgIAAxkBAAEQ21pljX6g7JtkVQgJPRZvUuHEeESzFAACYQMAArrAlQWtCQpcpHMj6zME CAACAgIAAxkBAAEQ21hljX6e4T2BXINz9aHC6bbOhN98-AACXwMAArrAlQV3VCzBKTQhzTME CAACAgIAAxkBAAEQ21ZljX6dOiFyPo25z-k3TemJM-AW0AACZAMAArrAlQUCMw3LNvhMBzME CAACAgIAAxkBAAEQ21RljX6aUwXFnLOUckJO6pPsJY7eJQACYwMAArrAlQXFRT6GJ_YYjDME CAACAgIAAxkBAAEQ21JljX6WcSoazCBpf-lSi_JWkRTJcQACXgMAArrAlQVceSrBWv5H7DME CAACAgIAAxkBAAEQ21BljX6TIJxdnk3g2pW4w92UCdGffgACaAMAArrAlQX1qKrummjK4jME CAACAgIAAxkBAAEQ205ljX6Q0uBqgIDVDsUvCNotXNVUxgACVwMAArrAlQVMHrV9flRvYDME CAACAgIAAxkBAAEQ20xljX6PRN-zZQoa_qKWSRtIr-faagACUQMAArrAlQV7yJzLJQ11NTME CAACAgIAAxkBAAEQ20pljX6LO0vO5MGfXTr5raW8awoMCgACZwMAArrAlQUYRInTOvVi5zME CAACAgUAAxkBAAEQ20hljX6CtrJGoRQbkhgunIrnnxmPtgACWAUAAj_q8FQzC8bJrK17oTME CAACAgUAAxkBAAEQ20ZljX56xaIj4yAYphK71XnLiv5piQACMgUAAiH_OFZUebKV2aRk4jME CAACAgUAAxkBAAEQ20JljX5ulp4Hs5GCtcwOoc5tQE5q7AACDgsAAqTleVRk8KSVmKztdTME CAACAgUAAxkBAAEQ20BljX5suhUDAvXCbRW66o_RVL-eLQAC0AUAAmKRSVbH3lZrdPrmzDME CAACAgUAAxkBAAEQ2z5ljX5rZp6rb2npKqJJUZjihq6nfgACEgYAAlHRSVZQOGffLaUQPDME CAACAgUAAxkBAAEQ2zxljX5pCWHmOGS5Kz7xWQFqQHiwIwACfQYAAihQOVXHMR0c722MljME CAACAgUAAxkBAAEQ2zpljX5nMXdpa64FlfpCt55M13RkTQACAgcAAqnwQVUZPTpNSHHYyzME CAACAgUAAxkBAAEQ2zhljX5lvTqj_GdHD0mjE8Gm_yoNuQACkwYAAnSE4FR1rf6moEtC3jME CAACAgQAAxkBAAEQ2zZljX5e9FXfOHq-pfQ--JC1E6f9NAACwgwAApu9YFOto4bf2PBvjjME CAACAgQAAxkBAAEQ2zRljX5c0OUYHcAWTjQsOVviMVVwqAACOxAAArb8IFC1KxiPG8NRXTME CAACAgQAAxkBAAEQ2zJljX5Yvtmjilx1LyeaH_9aFvRabQAClg4AAgpU4FPdiPEnNU-eAzME CAACAgQAAxkBAAEQ2zBljX5VlUhlERMNYflfQ_TFofjlcAAC5gsAAk8cWVNQLKJXQdhgTjME CAACAgUAAxkBAAEQ2y5ljX5HRQ7tY6cNxh1UDp1bek0uSAACRgUAAsVy2VfQ727ilW4Q0TME CAACAgIAAxkBAAEQ2yxljX5BdWIW00GJ7VfNNH84yKol_AACuAwAAu4J0Uju07GbH7xLtjME CAACAgIAAxkBAAEQ2ypljX4_ef4Gvip3zLn9S46-fThs8QACjw8AAnUuOUhbsCYf9OCDLzME CAACAgIAAxkBAAEQ2yhljX4-F93VJ9SI5Nqrw7hkgAuBYAACrA4AApttOUg2JQmaMDgs5DME CAACAgIAAxkBAAEQ2yZljX49k54WbfWZrWrz-XsOn-RLaQACmgsAArKo0EgS53Dn4tBGxjME CAACAgIAAxkBAAEQ2yRljX47vGql9dU1anPD8Gtr21GdDQACxAsAAotw0UgnQqg-jzV7MDME CAACAgIAAxkBAAEQ2yJljX45vhWNHZaM9cz_3A2hTdUcqgACYgwAAoRLUUneeFbkxCAnAzME CAACAgIAAxkBAAEQ2yBljX43ddBRisbLWhf3XCbfq-I6tQACHQ0AAh770Egx8DhQz29keTME CAACAgUAAxkBAAEQ2x5ljX4GJLG--Tdif5GXum4ySAPSUgACPAcAAvRbsVY-RudjcCNnRzME CAACAgUAAxkBAAEQ2xxljX4EJ1zBF-RDDI8Bw9C8TgU-dgACagcAAtOjsVaqe68IYcN1YjME CAACAgUAAxkBAAEQ2xpljX3_JsNCovrCShBKl-XwTMB1WQAC1ggAAtbKwVaoIpJ458lrbzME CAACAgUAAxkBAAEQ2xhljX3-rpUSr-Zysb5jM-UHdtflzwAC8wcAApZv8VZ2tD2uxVCppjME CAACAgUAAxkBAAEQ2xZljX38lCLPiGavo7umPSqqMY37VAACHAgAAsjxwFbq9aiknIndhjME CAACAgUAAxkBAAEQ2xRljX36Xdiuk8Pj_V1alIcWxpstPQAC9gcAAoOYwFbpOHyXHUEwojME CAACAgIAAxkBAAEQ2xJljX3uGw7RTdNeT1kcKleZdN9iWwACAQADwDZPExguczCrPy1RMwQ CAACAgIAAxkBAAEQ2xBljX3teYnVU4XRYcJbFUm29hgmxQACCQADwDZPE-_NG6JK_3GVMwQ CAACAgIAAxkBAAEQ2w5ljX3pISsLZHZG9AGeNJLzMkpgewACBQADwDZPE_lqX5qCa011MwQ CAACAgIAAxkBAAEQ2wxljX3f39-jvHcMId63H9DYQ9mmfwACHgADwDZPE6FgWy2rAAHeBDME CAACAgIAAxkBAAEQ2wpljX3YMNw4lagYeQyyrsm512RZ6gACCgADwDZPE_8Nrj7oDv0IMwQ CAACAgIAAxkBAAEQ2wABZY190jAxdLz3PpozCPddAyED4l4AAhMAA8A2TxOqs4f3fzjKpTME CAACAgIAAxkBAAEQ2v5ljX3RtHBG3Y5NgWNzhP8lCteK1QACAgADwDZPEwj1bkX6hKdZMwQ CAACAgUAAxkBAAEQ2vxljX3G0gxj5pR5rvF17IqbYOce0gACGBsAAhg7sVYEbqcxgVB0BzME CAACAgUAAxkBAAEQ2vpljX3FWN6o0BPvs6t1CsHPSlRY1AACdAoAAj1wsVagMcQaa7DpwDME CAACAgIAAxkBAAEQ2vhljX24IOhI5O_okxvJQLpEQu58DgACchIAAkblqUjyTBtFPtcDUTME CAACAgIAAxkBAAEQ2vZljX2zxFnUYPHtcIoHXkT3ARcV9gACXhIAAuyZKUl879mlR_dkOzME CAACAgIAAxkBAAEQ2vRljX2yJAv_Cu1ILriYIwllOTWzSgACchIAAkblqUjyTBtFPtcDUTME CAACAgIAAxkBAAEQ2vJljX2xNWg1gnxa6xYW4ceNAk7C0AACQhAAAjPFKUmQDtQRpypKgjME CAACAgIAAxkBAAEQ2vBljX2wDLfaSn8v0z5hRi5ygCFQ3gACdhEAAsMAASlJLbkjGWa6DogzBA CAACAgIAAxkBAAEQ2u5ljX2vwTtkxdzk9vx_7sLNQQysxAACvAwAAocoMEntN5GZWCFoBDME CAACAgIAAxkBAAEQ2uxljX2uWkQ0WZuEYqv-ERLKCAgZHgACoxAAAvF3qEh-OxgSw5fVQTME CAACAgIAAxkBAAEQ2upljX2s4GgknJbdiydP1onraOVl0AACaBEAAoWPKEnJ3C01n5I86TME CAACAgIAAxkBAAEQ2uhljX2rpDsEjlPjyvqtgI9HUka2zQACtA4AAnrnsEhInMQI4qVJTzME CAACAgIAAxkBAAEQ2uZljX2qUv5ReJO76qrQs6uuI_w8YAACkBAAAmteqEgcGk7MnoBFmDME CAACAgIAAxkBAAEQ2uRljX2kr05pfviYamDRHv1sV1QBhAACYgwAAoRLUUneeFbkxCAnAzME CAACAgIAAxkBAAEQ2uJljX2hc3ay1OVdOqbAOZSATyPewQACTwsAAiIPqEiffAABWBhYw3gzBA CAACAgIAAxkBAAEQ2uBljX2fD73IIJCnHUhV3C0j3snJ1QACVgwAAtIc2EgGpDcOv3z8XjME CAACAgUAAxkBAAEQ2t5ljX2WDFSnD_cwS5X294G-UrGqUgACxQUAAtKzoFTAWloi3EjAeTME CAACAgUAAxkBAAEQ2txljX2VCFKoA1IkjeNvj3Nq6onA-QACYAQAAioMGFT31AZIdDgfzDME CAACAgUAAxkBAAEQ2tpljX2SoNNnbgE8TH85w2e9wY_aRgACHAsAAjTXKVWSm3iPcbpSVjME CAACAgUAAxkBAAEQ2thljX2RYxSAq_Cayr9ljiDKv6HWZQACHwUAAwYhVsBmt0GBA78hMwQ CAACAgUAAxkBAAEQ2tZljX2OEKazpqSC2yGcvCG9pm882QACzQoAAiDn2VUKLZEKuLBP0DME CAACAgUAAxkBAAEQ2tRljX2L9UzJcL5Ou7F153lNhLaKpgACLwUAAnQ78VeOB3PdfvLh9jME CAACAgUAAxkBAAEQ2tJljX2HCqUHsmfhIrLfI9dc8JwIPQACxQQAAmtnGFRD00nwm6LHDjME CAACAgIAAxkBAAEQ2tBljX1oTRpo7Mu2N_qQSSDUYdHgBwACTwsAAiIPqEiffAABWBhYw3gzBA CAACAgIAAxkBAAEQ2s5ljX1lpq2nIeSMh2ABs7GMWArFvAACagsAArVLqEgy_6fKZOLx5jME CAACAgIAAxkBAAEQ2sxljX1kbYfwmVO0OegtwdAjEN6CGgACrQwAAvGUQUihcDy_-h_T6TME CAACAgIAAxkBAAEQ2spljX1hLlkVpoHdI4SJT7h1_LFTVAACJAwAAviQOEiWAywHzwABlxgzBA CAACAgQAAxkBAAEQ2sZljX0jh3vLtJpWZcxxj5bay9t-ZAACKxAAAk1zwFPGlaV1QZjTkTME CAACAgUAAxkBAAEQ2sRljXz-3uxQIFRstS3R5W-y0dC5qgAC5QUAAruXSFaWNURJP7tfwjME CAACAgUAAxkBAAEQ2sJljXzqbHl83Fv7n3m0HfNHBrho4QACCwoAAi7EUVfwywxU4Qq7_jME CAACAgUAAxkBAAEQ2sBljXzQxfyPIRI4ch3cHPk-rsCzpQACowkAAonICFTwfKVoynUZvzME CAACAgIAAxkBAAEQ2rxljXxsaNqc3gMhzW7FovMiXOvYnQAC-hMAAtSF8Etb7jRObi-mqzME CAACAgUAAxkBAAEQ2sJljXzqbHl83Fv7n3m0HfNHBrho4QACCwoAAi7EUVfwywxU4Qq7_jME CAACAgUAAxkBAAEQ2sBljXzQxfyPIRI4ch3cHPk-rsCzpQACowkAAonICFTwfKVoynUZvzME CAACAgIAAxkBAAEQ2rxljXxsaNqc3gMhzW7FovMiXOvYnQAC-hMAAtSF8Etb7jRObi-mqzME CAACAgIAAxkBAAEQ2rpljXxg0p_h1RoD1tBlVOvwFc-SzwAC_RMAAqrbgEuv3ujuB8gacDME CAACAgIAAxkBAAEQ2rhljXxPS3Qd-BV9RnA_0OwPiKsSCQACdwUAAj-VzApljNMsSkHZTjME CAACAgUAAxkBAAEQ2rZljXwsAAEr4nU50WP3Hz_0HCxmYSwAAuwDAAISQflXYznjU3iGTvkzBA CAACAgUAAxkBAAEQ2rRljXwhXX-JMs8GFzz2QZRxdUk9lAADBAACXtDwV04PGDy02iQAATME CAACAgUAAxkBAAEQ2rJljXwNvgcYFau24iQ57pNx72IbyAACdQQAAmh1-Ffusjt1plc9YzME CAACAgUAAxkBAAEQ2q5ljXvfjuP7GSEGy5LOIubDdZD24wACdAQAAg0N-VchhV4I8_I1XjME CAACAgIAAxkBAAEQ2qxljXvF9LzAOBwWqqGxYghZBptPFwACXgUAAj-VzAqq1ncTLO-MOTME CAACAgIAAxkBAAEQ2qpljXuwpjQsCWqkR190gR6vSLrjpgAC7hQAAuNVUEk4S4qtAhNhvDME CAACAgIAAxkBAAEQ2qhljXuRfi61G-Th8T9R7AIO_E-GFQACgBgAAsC2UEmimzNNrlDPPDME CAACAgIAAxkBAAEQ2qZljXt7emeVhLmGav1fiCUbTVKK6AACyRIAAmA0gEtb-P-xaa3sxjME CAACAgUAAxkBAAEQ2qRljXtnTHB4pmFFoKUQHw7JupE7-wACpwUAAuW4WFaFOaIX4LMhuDME CAACAgUAAxkBAAEQ2p5ljXsOArpCEAIuyF_X-cjbcq8y9wACUQMAAn4--FdPtUqUKQy6njME CAACAgIAAxkBAAEQ2pxljXr88eSrY-fNSv8tWqTsKQXSTwACWgUAAj-VzAobFrmFvSDDnTME CAACAgIAAxkBAAEQ2ppljXqrYNVEN_hsFrm72H_tJvwZEQACdgUAAj-VzApFV7w2VozN3TME CAACAgUAAxkBAAEQ2YpljSvD5sq-Flkm9TV8afTGo7Kr4gACgwMAAjO28FeYSaGKzSOuUTME"
lazystickerset = LAZYS_FILE_ID.split()

req_channel = REQ_CHANNEL
BUTTONS = {}
SPELL_CHECK = {}
# 
BUTTON = {}
FRESH = {}
BUTTONS0 = {}
BUTTONS1 = {}
BUTTONS2 = {}

# @Client.on_message(filters.group & filters.text & filters.incoming)
# async def give_filter(client, message):
#     try:
#         chatIDx = message.chat.id
#         lazy_chatIDx = await db.get_chat(int(chatIDx))
#         if lazy_chatIDx['is_lazy_verified']:
#             k = await manual_filters(client, message)
#     except Exception as e:
#         logger.error(f"Chat not verifeid : {e}") 

#     if k == False:
#         try:
#             chatID = message.chat.id
#             lazy_chatID = await db.get_chat(int(chatID))
#             if lazy_chatID['is_lazy_verified']:
#                 await auto_filter(client, message)
#         except Exception as e:
#             logger.error(f"Chat Not verified : {e}") 

@Client.on_message(filters.group & filters.text & filters.incoming)
async def give_filter(client, message):
    k = await manual_filters(client, message)
    if k == False:
        await auto_filter(client, message)

@Client.on_callback_query(filters.regex('rename'))
async def rename(bot,update):
	user_id = update.message.chat.id
	date = update.message.date
	await update.message.delete()
	await update.message.reply_text("»»——— 𝙋𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙣𝙚𝙬 𝙛𝙞𝙡𝙚 𝙣𝙖𝙢𝙚...",	
	reply_to_message_id=update.message.reply_to_message.id,  
	reply_markup=ForceReply(True))  
    
# Born to make history @LazyDeveloper !
@Client.on_callback_query(filters.regex("upload"))
async def doc(bot, update):
    try:
        type = update.data.split("_")[1]
        new_name = update.message.text
        new_filename = new_name.split(":-")[1]
        file = update.message.reply_to_message
        file_path = f"downloads/{new_filename}"
        ms = await update.message.edit("\n༻☬ད 𝘽𝙪𝙞𝙡𝙙𝙞𝙣𝙜 𝙇𝙖𝙯𝙮 𝙈𝙚𝙩𝙖𝘿𝙖𝙩𝙖...")
        c_time = time.time()
        try:
            path = await bot.download_media(
                    message=file,
                    progress=progress_for_pyrogram,
                    progress_args=("**\n  ღ♡ ꜰɪʟᴇ ᴜɴᴅᴇʀ ᴄᴏɴꜱᴛʀᴜᴄᴛɪᴏɴ... ♡♪**", ms, c_time))
        except Exception as e:
            await ms.edit(e)
            return 
        splitpath = path.split("/downloads/")
        dow_file_name = splitpath[1]
        old_file_name =f"downloads/{dow_file_name}"
        os.rename(old_file_name, file_path)
        duration = 0
        try:
            metadata = extractMetadata(createParser(file_path))
            if metadata.has("duration"):
               duration = metadata.get('duration').seconds
        except:
            pass
        user_id = int(update.message.chat.id) 
        ph_path = None 
        media = getattr(file, file.media.value)
        filesize = humanize.naturalsize(media.file_size) 
        c_caption = await db.get_caption(update.message.chat.id)
        c_thumb = await db.get_thumbnail(update.message.chat.id)
        if c_caption:
             try:
                 caption = c_caption.format(filename=new_filename, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
             except Exception as e:
                 await ms.edit(text=f"Your caption Error unexpected keyword ●> ({e})")
                 return 
        else:
            caption = f"**{new_filename}** \n\n⚡️Data costs: `{filesize}`"
        if (media.thumbs or c_thumb):
            if c_thumb:
               ph_path = await bot.download_media(c_thumb) 
            else:
               ph_path = await bot.download_media(media.thumbs[0].file_id)
            Image.open(ph_path).convert("RGB").save(ph_path)
            img = Image.open(ph_path)
            img.resize((320, 320))
            img.save(ph_path, "JPEG")
        await ms.edit("三 𝘗𝘳𝘦𝘱𝘢𝘳𝘪𝘯𝘨 𝘵𝘰 𝘳𝘦𝘤𝘦𝘪𝘷𝘦 𝘓𝘢𝘻𝘺 𝘧𝘪𝘭𝘦...︻デ═一")
        c_time = time.time() 
        try:
           if type == "document":
              await bot.send_document(
	            update.message.chat.id,
                       document=file_path,
                       thumb=ph_path, 
                       caption=caption, 
                       progress=progress_for_pyrogram,
                       progress_args=( "**⎝⎝✧ ʀᴇᴄɪᴇᴠɪɴɢ ꜰɪʟᴇ ꜰʀᴏᴍ ʟᴀᴢʏ ꜱᴇʀᴠᴇʀ ✧⎠⎠**",  ms, c_time))
           elif type == "video": 
               await bot.send_video(
	            update.message.chat.id,
	            video=file_path,
	            caption=caption,
	            thumb=ph_path,
	            duration=duration,
	            progress=progress_for_pyrogram,
	            progress_args=( "**⎝⎝✧ ʀᴇᴄɪᴇᴠɪɴɢ ꜰɪʟᴇ ꜰʀᴏᴍ ʟᴀᴢʏ ꜱᴇʀᴠᴇʀ ✧⎠⎠**",  ms, c_time))
           elif type == "audio": 
               await bot.send_audio(
	            update.message.chat.id,
	            audio=file_path,
	            caption=caption,
	            thumb=ph_path,
	            duration=duration,
	            progress=progress_for_pyrogram,
	            progress_args=( "**⎝⎝✧ ʀᴇᴄɪᴇᴠɪɴɢ ꜰɪʟᴇ ꜰʀᴏᴍ ʟᴀᴢʏ ꜱᴇʀᴠᴇʀ ✧⎠⎠**",  ms, c_time   )) 
        except Exception as e: 
            await ms.edit(f" Erro {e}") 
            os.remove(file_path)
            if ph_path:
              os.remove(ph_path)
            return 
        await ms.delete() 
        os.remove(file_path) 
        if ph_path:
           os.remove(ph_path) 
    except Exception as e:
        logger.error(f"error 2 : {e}")

# Born to make history @LazyDeveloper !
@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query):
    ident, req, key, offset = query.data.split("_")
    print(f"REQ => {req}")
    if int(req) not in [query.from_user.id, 0]:
        return await query.answer(
                        f"⚠️ ʜᴇʟʟᴏ{query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,\nʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                        show_alert=True,
                    )
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    chat_id = query.message.chat.id
    if not search:
        await query.answer("You are using one of my old messages, please send the request again.", show_alert=True)
        return

    files, n_offset, total = await get_search_results_badAss_LazyDeveloperr(chat_id, search, offset=offset, filter=True)
    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return
    temp.GETALL[key] = files
    temp.SHORT[query.from_user.id] = query.message.chat.id
    settings = await get_settings(query.message.chat.id)
    pre = 'filep' if settings['file_secure'] else 'file'
    lazyuser_id = query.from_user.id
    try:
        if temp.SHORT.get(lazyuser_id)==None:
            return await query.reply_text(text="<b>Please Search Again in Group</b>")
        else:
            chat_id = temp.SHORT.get(lazyuser_id)
    except Exception as e:
        print(e)
        # if query.from_user.id in download_counts and download_counts[query.from_user.id]['date'] == current_date:
        #     if download_counts[query.from_user.id]['count'] >= DOWNLOAD_LIMIT:
        #         # set URL_MODE to False to disable the URL shortener button
        #         URL_MODE = False
        #     else:
        #         # increment the download count for the user
        #         download_counts[query.from_user.id]['count'] += 1
        # else:
        #     # create a new entry for the user in the download counts dictionary
        #     download_counts[query.from_user.id] = {'date': current_date, 'count': 1}d
    if settings['button']:
            if settings['url_mode']:
                if query.from_user.id in ADMINS or await db.has_prime_status(query.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif query.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif query.from_user.id in LZURL_PRIME_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                        ]
                elif query.message.chat.id is not None and query.message.chat.id in LAZY_GROUPS:
                    btn = [
                    [
                        InlineKeyboardButton(
                            text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                        ),
                    ]
                    for file in files
                    ]
                else:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", 
                                url=f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"
                            ),
                        ]
                        for file in files
                    ]
            else:
                if query.from_user.id in ADMINS or await db.has_prime_status(query.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif query.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                else:    
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]

    else:
        if settings['url_mode']:
            if query.from_user.id in ADMINS or await db.has_prime_status(query.from_user.id):
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                    ]
                    for file in files
                ]
            elif query.from_user.id in MY_USERS:
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                    ]
                    for file in files
                ]
            elif query.from_user.id in LZURL_PRIME_USERS:
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                    ]
                    for file in files
                ]
            elif query.message.chat.id is not None and query.message.chat.id in LAZY_GROUPS:
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                    ]
                    for file in files
                ]
            else:
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",url=f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"),
                        InlineKeyboardButton(text=f"[{get_size(file.file_size)}]", url=f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"),
                    ]
                    for file in files
                ]
        else:
            if query.form_user.id in ADMINS:
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                    ]
                    for file in files
                ]
            elif query.form_user.id in MY_USERS:
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                    ]
                    for file in files
                ]
            else:
                btn = [
                    [
                        InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                        InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                    ]
                    for file in files
                ]
    
    btn.insert(0, 
        [
            InlineKeyboardButton("⇈ ꜱᴇʟᴇᴄᴛ ᴏᴘᴛɪᴏɴꜱ ʜᴇʀᴇ ⇈", 'select_info')
        ]
    )
    btn.insert(0, 
        [
            InlineKeyboardButton(f'ǫᴜᴀʟɪᴛʏ', callback_data=f"qualities#{key}"),
            InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data=f"languages#{key}"),
            InlineKeyboardButton("ꜱᴇᴀsᴏɴ",  callback_data=f"seasons#{key}")
        ]
    )
    btn.insert(0, [
            InlineKeyboardButton("♨️ ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ ♨️", callback_data=f"sendfiles#{key}")
        ])
    btn.insert(0,
        [ 
	    InlineKeyboardButton(text="⚡ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ⚡", url='https://telegram.me/movierequestAK'),
        ] 
    )
    if 0 < offset <= 10:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 10
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton("⋞ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
             InlineKeyboardButton(f"📃 Pages {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}",
                                  callback_data="pages")]
        )
    elif off_set is None:
        btn.append(
            [InlineKeyboardButton(f"🗓 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
             InlineKeyboardButton("ɴᴇxᴛ ⋟", callback_data=f"next_{req}_{key}_{n_offset}")])
    else:
        btn.append(
            [
                InlineKeyboardButton("⋞ ʙᴀᴄᴋ", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"🗓 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
                InlineKeyboardButton("ɴᴇxᴛ ⋟", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )
    try:
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(btn)
        )
    except MessageNotModified:
        pass
    await query.answer()

# Born to make history @LazyDeveloper !
@Client.on_callback_query(filters.regex(r"^spolling"))
async def advantage_spoll_choker(bot, query):
    _, user, movie_ = query.data.split('#')
    if int(user) != 0 and query.from_user.id != int(user):
        return await query.answer("This Message is not for you dear. Don't worry you can send new one !", show_alert=True)
    if movie_ == "close_spellcheck":
        return await query.message.delete()
    movies = SPELL_CHECK.get(query.message.reply_to_message.id)
    if not movies:
        return await query.answer("You are clicking on an old button which is expired.", show_alert=True)
    movie = movies[(int(movie_))]
    chat_id = query.message.chat.id

    await query.answer('Checking for Movie in database...')
    k = await manual_filters(bot, query.message, text=movie)
    if k == False:
        files, offset, total_results = await get_search_results_badAss_LazyDeveloperr(chat_id, movie, offset=0, filter=True)
        if files:
            k = (movie, files, offset, total_results)
            await auto_filter(bot, query, k)
        else:
            k = await query.message.edit('😒 currently unavailable ! we are really sorry for inconvenience !\n Have patience ! our great admins will upload it as soon as possible !')
            await asyncio.sleep(10)
            await k.delete()

# Born to make history @LazyDeveloeprr 🍁
@Client.on_callback_query(filters.regex(r"^qualities#"))
async def qualities_cb_handler(client: Client, query: CallbackQuery):

    try:
        if int(query.from_user.id) not in [query.message.reply_to_message.from_user.id, 0]:
            return await query.answer(
                f"⚠️ ʜᴇʟʟᴏ {query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,\nʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                show_alert=True,
            )
    except:
        pass
    _, key = query.data.split("#")
    # if BUTTONS.get(key+"1")!=None:
    #     search = BUTTONS.get(key+"1")
    # else:
    #     search = BUTTONS.get(key)
    #     BUTTONS[key+"1"] = search
    search = FRESH.get(key)
    search = search.replace(' ', '_')
    btn = []
    for i in range(0, len(QUALITIES)-1, 2):
        btn.append([
            InlineKeyboardButton(
                text=QUALITIES[i].title(),
                callback_data=f"fq#{QUALITIES[i].lower()}#{key}"
            ),
            InlineKeyboardButton(
                text=QUALITIES[i+1].title(),
                callback_data=f"fq#{QUALITIES[i+1].lower()}#{key}"
            ),
        ])

    btn.insert(
        0,
        [
            InlineKeyboardButton(
                text="⇊ sᴇʟᴇᴄᴛ ǫᴜᴀʟɪᴛʏ ⇊", callback_data="select_option"
            )
        ],
    )
    req = query.from_user.id
    offset = 0
    btn.append([InlineKeyboardButton(text="↭ ʙᴀᴄᴋ ᴛᴏ ꜰɪʟᴇs ↭", callback_data=f"fq#homepage#{key}")])

    await query.edit_message_reply_markup(InlineKeyboardMarkup(btn))
 
@Client.on_callback_query(filters.regex(r"^fq#"))
async def filter_qualities_cb_handler(client: Client, query: CallbackQuery):
    try:
        _, qual, key = query.data.split("#")
        curr_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        search = FRESH.get(key)
        search = search.replace("_", " ")
        baal = qual in search
        if baal:
            search = search.replace(qual, "")
        else:
            search = search
        req = query.from_user.id
        chat_id = query.message.chat.id
        message = query.message
        try:
            if int(query.from_user.id) not in [query.message.reply_to_message.from_user.id, 0]:
                return await query.answer(
                    f"⚠️ ʜᴇʟʟᴏ {query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,\nʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                    show_alert=True,
                )
        except:
            pass
        if qual != "homepage":
            search = f"{search} {qual}" 
        BUTTONS[key] = search

        files, offset, total_results = await get_search_results_badAss_LazyDeveloperr(chat_id, search, offset=0, filter=True)
        if not files:
            await query.answer("🚫 ɴᴏ ꜰɪʟᴇꜱ ᴡᴇʀᴇ ꜰᴏᴜɴᴅ 🚫", show_alert=1)
            return
        temp.GETALL[key] = files
        settings = await get_settings(message.chat.id)
        pre = 'filep' if settings['file_secure'] else 'file'
        temp.SHORT[query.from_user.id] = query.message.chat.id
        lazyuser_id = query.from_user.id
        try:
            if temp.SHORT.get(lazyuser_id)==None:
                return await message.reply_text(text="<b>Please Search Again in Group</b>")
            else:
                chat_id = temp.SHORT.get(lazyuser_id)
        except Exception as e:
            print(e)
        if settings["button"]:
            # btn = [
            #     [
            #         InlineKeyboardButton(
            #             text=f"[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}", callback_data=f'{pre}#{file.file_id}'
            #         ),
            #     ]
            #     for file in files
            # ]
            if settings['url_mode']:
                if message.from_user.id in ADMINS or await db.has_prime_status(message.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif message.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif message.from_user.id in LZURL_PRIME_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}'
                            ),
                        ]
                        for file in files
                        ]
                elif message.chat.id is not None and message.chat.id in LAZY_GROUPS:
                    btn = [
                    [
                        InlineKeyboardButton(
                            text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}'
                        ),
                    ]
                    for file in files
                    ]
                else:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", 
                                url=await f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"),
                        ]
                        for file in files
                    ]
            else:
                if message.from_user.id in ADMINS or await db.has_prime_status(message.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif message.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                else:    
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]

        else:
            if settings['url_mode']:
                if query.from_user.id in ADMINS or await db.has_prime_status(query.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.from_user.id in LZURL_PRIME_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.message.chat.id is not None and query.message.chat.id in LAZY_GROUPS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                else:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",url=await f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"),
                            InlineKeyboardButton(text=f"[{get_size(file.file_size)}]", url=await f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"),
                        ]
                        for file in files
                    ]
            else:
                if query.form_user.id in ADMINS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.form_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                else:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]

        btn.insert(0, 
            [
                InlineKeyboardButton("⇈ ꜱᴇʟᴇᴄᴛ ᴏᴘᴛɪᴏɴꜱ ʜᴇʀᴇ ⇈", 'select_info')
            ]
        )
        btn.insert(0, 
            [
                InlineKeyboardButton(f'ǫᴜᴀʟɪᴛʏ', callback_data=f"qualities#{key}"),
                InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data=f"languages#{key}"),
                InlineKeyboardButton("ꜱᴇᴀsᴏɴ",  callback_data=f"seasons#{key}")
            ]
        )
        btn.insert(0, [
            InlineKeyboardButton("♨️ ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ ♨️", callback_data=f"sendfiles#{key}")
        ])
        btn.insert(0,
            [ 
            InlineKeyboardButton(text="⚡ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ⚡", url='https://telegram.me/movierequestAK'),
            ] 
        )

        if offset != "":
            print(f"offset => {offset}")
            btn.append(
                [InlineKeyboardButton(text=f"🗓 1/{math.ceil(int(total_results) / 10)}", callback_data="pages"),
                InlineKeyboardButton(text="ɴᴇxᴛ ⋟", callback_data=f"next_{req}_{key}_{offset}")]
            )
        else:
            btn.append(
                [InlineKeyboardButton(text="🗓 1/1", callback_data="pages")]
            )
        try:
            await query.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(btn)
            )
        except MessageNotModified:
            pass
        await query.answer()   
    except Exception as e:
        logger.error(f"Got an unexpected error : {e}")

# Born to make history @LazyDeveloeprr 🍁
@Client.on_callback_query(filters.regex(r"^seasons#"))
async def seasons_cb_handler(client: Client, query: CallbackQuery):
    try:
        if int(query.from_user.id) not in [query.message.reply_to_message.from_user.id, 0]:
            return await query.answer(
                f"⚠️ ʜᴇʟʟᴏ {query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,\nʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                show_alert=True,
            )
    except:
        pass
    _, key = query.data.split("#")
    # if BUTTONS.get(key+"2")!=None:
    #     search = BUTTONS.get(key+"2")
    # else:
    #     search = BUTTONS.get(key)
    #     BUTTONS[key+"2"] = search
    search = FRESH.get(key)
    BUTTONS[key] = None
    search = search.replace(' ', '_')
    btn = []
    for i in range(0, len(SEASONS)-1, 2):
        btn.append([
            InlineKeyboardButton(
                text=SEASONS[i].title(),
                callback_data=f"fs#{SEASONS[i].lower()}#{key}"
            ),
            InlineKeyboardButton(
                text=SEASONS[i+1].title(),
                callback_data=f"fs#{SEASONS[i+1].lower()}#{key}"
            ),
        ])

    btn.insert(
        0,
        [
            InlineKeyboardButton(
                text="⇊ ꜱᴇʟᴇᴄᴛ ꜱᴇᴀꜱᴏɴ ⇊", callback_data="select_option"
            )
        ],
    )
    req = query.from_user.id
    offset = 0
    btn.append([InlineKeyboardButton(text="↭ ʙᴀᴄᴋ ᴛᴏ ꜰɪʟᴇs ​↭", callback_data=f"fs#homepage#{key}")])

    await query.edit_message_reply_markup(InlineKeyboardMarkup(btn))

@Client.on_callback_query(filters.regex(r"^fs#"))
async def filter_seasons_cb_handler(client: Client, query: CallbackQuery):
    try:
        _, seas, key = query.data.split("#")
        curr_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        search = FRESH.get(key)
        search = search.replace("_", " ")
        sea = ""
        season_search = ["s01","s02", "s03", "s04", "s05", "s06", "s07", "s08", "s09", "s10", "season 01","season 02","season 03","season 04","season 05","season 06","season 07","season 08","season 09","season 10", "season 1","season 2","season 3","season 4","season 5","season 6","season 7","season 8","season 9"]
        for x in range (len(season_search)):
            if season_search[x] in search:
                sea = season_search[x]
                break
        if sea:
            search = search.replace(sea, "")
        else:
            search = search

        req = query.from_user.id
        chat_id = query.message.chat.id
        message = query.message
        try:
            if int(query.from_user.id) not in [query.message.reply_to_message.from_user.id, 0]:
                return await query.answer(
                    f"⚠️ ʜᴇʟʟᴏ {query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ,\nʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                    show_alert=True,
                )
        except:
            pass
        
        searchagn = search
        search1 = search
        search2 = search
        search = f"{search} {seas}"
        BUTTONS0[key] = search

        files, _, _ = await get_search_results_badAss_LazyDeveloperr(chat_id, search, max_results=10)
        files = [file for file in files if re.search(seas, file.file_name, re.IGNORECASE)]

        seas1 = "s01" if seas == "season 1" else "s02" if seas == "season 2" else "s03" if seas == "season 3" else "s04" if seas == "season 4" else "s05" if seas == "season 5" else "s06" if seas == "season 6" else "s07" if seas == "season 7" else "s08" if seas == "season 8" else "s09" if seas == "season 9" else "s10" if seas == "season 10" else ""
        search1 = f"{search1} {seas1}"
        BUTTONS1[key] = search1
        files1, _, _ = await get_search_results_badAss_LazyDeveloperr(chat_id, search1, max_results=10)
        files1 = [file for file in files1 if re.search(seas1, file.file_name, re.IGNORECASE)]

        if files1:
            files.extend(files1)

        seas2 = "season 01" if seas == "season 1" else "season 02" if seas == "season 2" else "season 03" if seas == "season 3" else "season 04" if seas == "season 4" else "season 05" if seas == "season 5" else "season 06" if seas == "season 6" else "season 07" if seas == "season 7" else "season 08" if seas == "season 8" else "season 09" if seas == "season 9" else "s010"
        search2 = f"{search2} {seas2}"
        BUTTONS2[key] = search2
        files2, _, _ = await get_search_results_badAss_LazyDeveloperr(chat_id, search2, max_results=10)
        files2 = [file for file in files2 if re.search(seas2, file.file_name, re.IGNORECASE)]

        if files2:
            files.extend(files2)

        if not files:
            await query.answer("🚫 ɴᴏ ꜰɪʟᴇꜱ ᴡᴇʀᴇ ꜰᴏᴜɴᴅ 🚫", show_alert=1)
            return
        temp.GETALL[key] = files
        settings = await get_settings(message.chat.id)
        pre = 'filep' if settings['file_secure'] else 'file'
        temp.SHORT[query.from_user.id] = query.message.chat.id
        lazyuser_id = query.from_user.id
        try:
            if temp.SHORT.get(lazyuser_id)==None:
                return await message.reply_text(text="<b>Please Search Again in Group</b>")
            else:
                chat_id = temp.SHORT.get(lazyuser_id)
        except Exception as e:
            print(e)
        if settings["button"]:
            # btn = [
            #     [
            #         InlineKeyboardButton(
            #             text=f"[{get_size(file.file_size)}] {' '.join(filter(lambda x: not x.startswith('[') and not x.startswith('@') and not x.startswith('www.'), file.file_name.split()))}", callback_data=f'{pre}#{file.file_id}'
            #         ),
            #     ]
            #     for file in files
            # ]
            if settings['url_mode']:
                if message.from_user.id in ADMINS or await db.has_prime_status(message.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif message.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif message.from_user.id in LZURL_PRIME_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}'
                            ),
                        ]
                        for file in files
                        ]
                elif message.chat.id is not None and message.chat.id in LAZY_GROUPS:
                    btn = [
                    [
                        InlineKeyboardButton(
                            text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}'
                        ),
                    ]
                    for file in files
                    ]
                else:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", 
                                url=await f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"
                            ),
                        ]
                        for file in files
                    ]
            else:
                if message.from_user.id in ADMINS or await db.has_prime_status(message.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                elif message.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'files#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]
                else:    
                    btn = [
                        [
                            InlineKeyboardButton(
                                text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'{pre}#{file.file_id}'
                            ),
                        ]
                        for file in files
                    ]

        else:
            if settings['url_mode']:
                if query.from_user.id in ADMINS or await db.has_prime_status(query.from_user.id):
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.from_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.from_user.id in LZURL_PRIME_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.message.chat.id is not None and query.message.chat.id in LAZY_GROUPS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                else:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",url=f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"),
                            InlineKeyboardButton(text=f"[{get_size(file.file_size)}]", url=f"https://telegram.me/{temp.U_NAME}?start=files_{file.file_id}"),
                        ]
                        for file in files
                    ]
            else:
                if query.form_user.id in ADMINS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                elif query.form_user.id in MY_USERS:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]
                else:
                    btn = [
                        [
                            InlineKeyboardButton(text=f"{file.file_name}",callback_data=f'files#{file.file_id}',),
                            InlineKeyboardButton(text=f"{get_size(file.file_size)}",callback_data=f'files#{file.file_id}',),
                        ]
                        for file in files
                    ]

        btn.insert(0, 
            [
                InlineKeyboardButton("⇈ ꜱᴇʟᴇᴄᴛ ᴏᴘᴛɪᴏɴꜱ ʜᴇʀᴇ ⇈", 'select_info')
            ]
        )
        btn.insert(0, 
            [
                InlineKeyboardButton(f'ǫᴜᴀʟɪᴛʏ', callback_data=f"qualities#{key}"),
                InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data=f"languages#{key}"),
                InlineKeyboardButton("ꜱᴇᴀsᴏɴ",  callback_data=f"seasons#{key}")
            ]
        )
        btn.insert(0, [
            InlineKeyboardButton("♨️ ꜱᴇɴᴅ ᴀʟʟ ꜰɪʟᴇꜱ ♨️", callback_data=f"sendfiles#{key}")
        ])
        btn.insert(0,
        [ 
	    InlineKeyboardButton(text="⚡ ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ⚡", url='https://telegram.me/movierequestAK'),
        ] 
    )

        offset=0
        total_results = len(files)
        if offset != "":
            print(f"offset => {offset}")
            btn.append(
                [InlineKeyboardButton(text=f"🗓 1/{math.ceil(int(total_results) / 10)}", callback_data="pages"),
                InlineKeyboardButton(text="ɴᴇxᴛ ⋟", callback_data=f"next_{req}_{key}_{offset}")]
            )
        else:
            btn.append(
                [InlineKeyboardButton(text="🗓 1/1", callback_data="pages")]
            )
        try:
            await query.edit_message_reply_markup(
                reply_markup=InlineKeyboardMarkup(btn)
            )
        except MessageNotModified:
            pass
        await query.answer()   
    except Exception as e:
        logger.error(f"Got an unexpected error : {e}")

# Born to make history @LazyDeveloeprr 🍁
@Client.on_callback_query(filters.regex(r"^languages#"))
async def languages_cb_handler(client: Client, query: CallbackQuery):
    try:
        if int(query.from_user.id) not in [query.message.reply_to_message.from_user.id, 0]:
            return await query.answer(
                f"⚠️ ʜᴇʟʟᴏ{query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,\nʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                show_alert=True,
            )
    except:
        pass
    _, key = query.data.split("#")
    # if BUTTONS.get(key+"1")!=None:
    #     search = BUTTONS.get(key+"1")
    # else:
    #     search = BUTTONS.get(key)
    #     BUTTONS[key+"1"] = search
    search = FRESH.get(key)
    search = search.replace(' ', '_')
    btn = []
    for i in range(0, len(LANGUAGES)-1, 2):
        btn.append([
            InlineKeyboardButton(
                text=LANGUAGES[i].title(),
                callback_data=f"fl#{LANGUAGES[i].lower()}#{key}"
            ),
            InlineKeyboardButton(
                text=LANGUAGES[i+1].title(),
                callback_data=f"fl#{LANGUAGES[i+1].lower()}#{key}"
            ),
        ])
    btn.insert(
        0,
        [
            InlineKeyboardButton(
                text="⇊ ꜱᴇʟᴇᴄᴛ ʟᴀɴɢᴜᴀɢᴇ ⇊", callback_data="select_option"
            )
        ],
    )
    req = query.from_user.id
    offset = 0
    btn.append([InlineKeyboardButton(text="↭ ʙᴀᴄᴋ ᴛᴏ ꜰɪʟᴇs ​↭", callback_data=f"fl#homepage#{key}")])

    await query.edit_message_reply_markup(InlineKeyboardMarkup(btn))
    
@Client.on_callback_query(filters.regex(r"^fl#"))
async def filter_languages_cb_handler(client: Client, query: CallbackQuery):
    try:
        _, lang, key = query.data.split("#")
        curr_time = datetime.now(pytz.timezone('Asia/Kolkata')).time()
        search = FRESH.get(key)
        search = search.replace("_", " ")
        baal = lang in search
        if baal:
            search = search.replace(lang, "")
        else:
            search = search
        req = query.from_user.id
        chat_id = query.message.chat.id
        message = query.message
        try:
            if int(req) not in [query.message.reply_to_message.from_user.id, 0]:
                return await query.answer(
                    f"👊 ʜᴇʟʟᴏ{query.from_user.first_name},\nᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,\nʀᴇQᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...",
                    show_alert=True,
                )
        except:
            pass
        if lang != "homepage":
            search = f"{search} {lang}"
        BUTTONS[key] = search
    
        files, offset, total_results = await get_search_results_badAss_LazyDeveloperr(chat_id, search, offset=0, filter=True)

        if not files:
            await query.answer("🚫 𝗡𝗼 𝗙𝗶𝗹𝗲 𝗪𝗲𝗿𝗲 𝗙𝗼𝘂𝗻𝗱 🚫", show_alert=1)
            return
        temp.GETALL[key] = files 
        settings = await get_settings(message.chat.id)
        pre = 'filep' if settings['file_secure'] else 'file'
        temp.SHORT[query.from_user.id] = query.message.chat.id
        lazyuser_id = query.from_user.id
        try:
