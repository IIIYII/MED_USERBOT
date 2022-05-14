# LOVEGif for R by: @MedThon

from .. import reply_id as rd
from . import *


@bot.on(admin_cmd(outgoing=True, pattern="ح1$"))
@bot.on(sudo_cmd(pattern="ح1$", allow_sudo=True))
async def vegif(Med):
    if Med.fwd_from:
        return
    Ti = await rd(Med)
    if ve_gif:
        Med_caption = f"**{LOVE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الاولى 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, ve_gif, caption=Med_caption, reply_to=Ti
        )

@bot.on(admin_cmd(outgoing=True, pattern="ح2$"))
@bot.on(sudo_cmd(pattern="ح2$", allow_sudo=True))
async def vegif(Med):
    if Med.fwd_from:
        return
    th = await rd(Med)
    if ve_gif2:
        Med_caption = f"**{LOVE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الثانيه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, ve_gif2, caption=Med_caption, reply_to=th
        )

@bot.on(admin_cmd(outgoing=True, pattern="ح3$"))
@bot.on(sudo_cmd(pattern="ح3$", allow_sudo=True))
async def vegif(Med):
    if Med.fwd_from:
        return
    kh = await rd(Med)
    if ve_gif3:
        Med_caption = f"**{LOVE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الثالثه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, ve_gif3, caption=Med_caption, reply_to=kh
        )

@bot.on(admin_cmd(outgoing=True, pattern="ح4$"))
@bot.on(sudo_cmd(pattern="ح4$", allow_sudo=True))
async def vegif(Med):
    if Med.fwd_from:
        return
    wh = await rd(Med)
    if ve_gif4:
        vec = f"**{LOVE}**\n"
        vec += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        vec += f"**↫ المتـحركه الرابعه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, ve_gif4, caption=vec, reply_to=wh
        )

@bot.on(admin_cmd(outgoing=True, pattern="ح5$"))
@bot.on(sudo_cmd(pattern="ح5$", allow_sudo=True))
async def vegif(Med):
    if Med.fwd_from:
        return
    ih = await rd(Med)
    if ve_gif5:
        vec = f"**{LOVE}**\n"
        vec += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        vec += f"**↫ المتـحركه الخامسه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, ve_gif5, caption=vec, reply_to=ih
        )


@bot.on(admin_cmd(outgoing=True, pattern="ح6$"))
@bot.on(sudo_cmd(pattern="ح6$", allow_sudo=True))
async def vegif(Med):
    if Med.fwd_from:
        return
    uh = await rd(Med)
    if ve_gif6:
        vec = f"**{LOVE}**\n"
        vec += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        vec += f"**↫ المتـحركه السادسه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, ve_gif6, caption=vec, reply_to=uh
        )


@bot.on(admin_cmd(outgoing=True, pattern="ح7$"))
@bot.on(sudo_cmd(pattern="ح7$", allow_sudo=True))
async def vegif(Med):
    if Med.fwd_from:
        return
    oh = await rd(Med)
    if ve_gif7:
        vec = f"**{LOVE}**\n"
        vec += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        vec += f"**↫ المتـحركه السابعه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, ve_gif7, caption=vec, reply_to=oh
        )

