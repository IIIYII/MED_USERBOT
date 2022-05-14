# KutGif for R by: @MedThon

from .. import reply_id as rd
from . import *


@bot.on(admin_cmd(outgoing=True, pattern="ك1$"))
@bot.on(sudo_cmd(pattern="ك1$", allow_sudo=True))
async def kutgif(Med):
    if Med.fwd_from:
        return
    Ti = await rd(Med)
    if kut_gif:
        Med_caption = f"**{KUTTE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝙏𝙃𝙊𝙉ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الاولى 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, kut_gif, caption=Med_caption, reply_to=Ti
        )

@bot.on(admin_cmd(outgoing=True, pattern="ك2$"))
@bot.on(sudo_cmd(pattern="ك2$", allow_sudo=True))
async def kutgif(Med):
    if Med.fwd_from:
        return
    th = await rd(Med)
    if kut_gif2:
        Med_caption = f"**{KUTTE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝙏𝙃𝙊𝙉ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الثانيه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, kut_gif2, caption=Med_caption, reply_to=th
        )

@bot.on(admin_cmd(outgoing=True, pattern="ك3$"))
@bot.on(sudo_cmd(pattern="ك3$", allow_sudo=True))
async def kutgif(Med):
    if Med.fwd_from:
        return
    kh = await rd(Med)
    if kut_gif3:
        Med_caption = f"**{KUTTE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝙏𝙃𝙊𝙉ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الثالثه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, kut_gif3, caption=Med_caption, reply_to=kh
        )

@bot.on(admin_cmd(outgoing=True, pattern="ك4$"))
@bot.on(sudo_cmd(pattern="ك4$", allow_sudo=True))
async def kutgif(Med):
    if Med.fwd_from:
        return
    wh = await rd(Med)
    if kut_gif4:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝙏𝙃𝙊𝙉ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه الرابعه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, kut_gif4, caption=kutc, reply_to=wh
        )

@bot.on(admin_cmd(outgoing=True, pattern="ك5$"))
@bot.on(sudo_cmd(pattern="ك5$", allow_sudo=True))
async def kutgif(Med):
    if Med.fwd_from:
        return
    ih = await rd(Med)
    if kut_gif5:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝙏𝙃𝙊𝙉ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه الخامسه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, kut_gif5, caption=kutc, reply_to=ih
        )


@bot.on(admin_cmd(outgoing=True, pattern="ك6$"))
@bot.on(sudo_cmd(pattern="ك6$", allow_sudo=True))
async def kutgif(Med):
    if Med.fwd_from:
        return
    uh = await rd(Med)
    if kut_gif6:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝙏𝙃𝙊𝙉ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه السادسه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, kut_gif6, caption=kutc, reply_to=uh
        )


@bot.on(admin_cmd(outgoing=True, pattern="ك7$"))
@bot.on(sudo_cmd(pattern="ك7$", allow_sudo=True))
async def kutgif(Med):
    if Med.fwd_from:
        return
    oh = await rd(Med)
    if kut_gif7:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝙏𝙃𝙊𝙉ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه السابعه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, kut_gif7, caption=kutc, reply_to=oh
        )

