# TSHEGif for R by: @MedThon

from .. import reply_id as rd
from . import *


@bot.on(admin_cmd(outgoing=True, pattern="ش1$"))
@bot.on(sudo_cmd(pattern="ش1$", allow_sudo=True))
async def fygif(Med):
    if Med.fwd_from:
        return
    Ti = await rd(Med)
    if fy_gif:
        Med_caption = f"**{TSHE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الاولى 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, fy_gif, caption=Med_caption, reply_to=Ti
        )

@bot.on(admin_cmd(outgoing=True, pattern="ش2$"))
@bot.on(sudo_cmd(pattern="ش2$", allow_sudo=True))
async def fygif(Med):
    if Med.fwd_from:
        return
    th = await rd(Med)
    if fy_gif2:
        Med_caption = f"**{TSHE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الثانيه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, fy_gif2, caption=Med_caption, reply_to=th
        )

@bot.on(admin_cmd(outgoing=True, pattern="ش3$"))
@bot.on(sudo_cmd(pattern="ش3$", allow_sudo=True))
async def fygif(Med):
    if Med.fwd_from:
        return
    kh = await rd(Med)
    if fy_gif3:
        Med_caption = f"**{TSHE}**\n"
        Med_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        Med_caption += f"**↫ المتـحركه الثالثه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, fy_gif3, caption=Med_caption, reply_to=kh
        )

@bot.on(admin_cmd(outgoing=True, pattern="ش4$"))
@bot.on(sudo_cmd(pattern="ش4$", allow_sudo=True))
async def fygif(Med):
    if Med.fwd_from:
        return
    wh = await rd(Med)
    if fy_gif4:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**↫ المتـحركه الرابعه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, fy_gif4, caption=fyc, reply_to=wh
        )

@bot.on(admin_cmd(outgoing=True, pattern="ش5$"))
@bot.on(sudo_cmd(pattern="ش5$", allow_sudo=True))
async def fygif(Med):
    if Med.fwd_from:
        return
    ih = await rd(Med)
    if fy_gif5:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**↫ المتـحركه الخامسه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, fy_gif5, caption=fyc, reply_to=ih
        )


@bot.on(admin_cmd(outgoing=True, pattern="ش6$"))
@bot.on(sudo_cmd(pattern="ش6$", allow_sudo=True))
async def fygif(Med):
    if Med.fwd_from:
        return
    uh = await rd(Med)
    if fy_gif6:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**↫ المتـحركه السادسه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, fy_gif6, caption=fyc, reply_to=uh
        )


@bot.on(admin_cmd(outgoing=True, pattern="ش7$"))
@bot.on(sudo_cmd(pattern="ش7$", allow_sudo=True))
async def fygif(Med):
    if Med.fwd_from:
        return
    oh = await rd(Med)
    if fy_gif7:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**↫ المتـحركه السابعه 𓆰.**"
        await Med.client.send_file(
            Med.chat_id, fy_gif7, caption=fyc, reply_to=oh
        )

