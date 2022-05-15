import asyncio
import time

import aiohttp
from telethon.errors import ChatAdminRequiredError as no_admin
from telethon.tl.functions.messages import ExportChatInviteRequest

from ..helpers import get_user_from_event
from . import *
import os

@Medthon.on(L_U_2 _cmd(pattern="طقس (.*)"))
@Medthon.on(sudo_cmd(pattern="طقس (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    Med = "adf0cf22618186fc11e9f89c090cb356"
    sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str, Med))
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await edit_or_reply(
            event,
            """**🗺┊حالات الطقس لـ مدينـة** {}
**🔅┊الحـرارة :** {}°С
**🏜┊درجة الحرارة الصغرى :** {}°С
**🌋┊درجة الحرارة العظمى :** {}°С
**🏖┊الرطـوبة :** {}%
**🎑┊الـرياح :** {}m/s
**🌁┊السحـاب :** {}hpa
**🌄┊شروق الشمس :** {} {}
**🌅┊غروب الشمس :** {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %I:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %I:%M:%S", time.gmtime(sun_set_time)),
                country_code,
            ),
        )
    else:
        await edit_or_reply(event, response_api["message"])


@Medthon.on(L_U_2 _cmd(pattern="يكتب(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع الكتابه الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)


@Medthon.on(L_U_2 _cmd(pattern="صوتيه(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع ارسال تسجيل الصوت الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@Medthon.on(L_U_2 _cmd(pattern="فيد(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع ارسال الفيديو الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@Medthon.on(L_U_2 _cmd(pattern="لعبه(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**⎆┊عليك كتابة الامر بشكل صحيح**")
    await event.edit(f"**⎆┊تم بدء وضع اللعب الوهمي لـ {t} من الثوانـي ✓**")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)



CMD_HELP.update(
    {
        "وهمي": """**اسـم الاضـافه : **`وهمي`

**الاوامــر : **
  •  `.يكتب`
  •  `.صوتيه`
  •  `.فيد`
  •  `.لعبه`
  
  •  `.طقس + اسم المدينه`
  
**Function : **__Just like art plugin this are some other arts__"""
    }
)
