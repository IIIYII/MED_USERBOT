#Medthon ®

from userbot.helpers import *
import base64
import io
import os
from pathlib import Path
from . import *
from telethon import types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from youtubesearchpython import Video
import json
import os
import time
import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

try:

    from youtubesearchpython import *

except:
    os.system("pip install pip install youtube-search-python")
    from youtubesearchpython import SearchVideos

from userbot import bot
from ..helpers.utils import reply_id
from userbot.helpers.functions import deEmojify



@bot.on(admin_cmd(pattern="بحث ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="بحث ?(.*)", allow_sudo=True))
async def FindMusicPleaseBot(Med):

    song = Med.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await Med.edit("**❈╎قم باضافـة الاغنيـه للامـر .. بحث + اسـم الاغنيـه**")

    await Med.edit("**╮ جـارِ البحث ؏ـن الاغنيـٓه... 🎧♥️╰**")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await Med.edit("**╮ ❐ جـارِ تحميـل الاغنيـٓه انتظـر قليلاً  ▬▭... 𓅫╰**")

        try:

            await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("عـذراً"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await Med.edit(f"**❈╎عـذراً .. لـم استطـع ايجـاد** {song}")

            await conv.get_response()

            lavde = await conv.get_response()

        except YouBlockedUserError:

            await Med.edit(
                "**❈╎تحـقق من انـك لم تقـم بحظـر البوت @FindMusicPleaseBot .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )

            return

        await Med.edit("**╮ ❐ جـارِ ارسـال الاغنيـٓه انتظـر قليلاً  ▬▭... 𓅫╰**")

        await bot.send_file(Med.chat_id, lavde)

        await bot.send_read_acknowledge(conv.chat_id)

    await Med.delete()
