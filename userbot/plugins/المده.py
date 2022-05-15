"""
©Med : @MedThon
  - Med UpTime
  - Commend: .المده
"""

import time

from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "Medbot"
Med_IMG = "https://telegra.ph/file/57d51af1ca93d8cc8a958.jpg"
Med_TEXT = "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝗠𝗘𝗗𝗧𝙃𝙊𝙉 𓆪"
MedEM = "**⌔∮**"


@bot.on(admin_cmd(outgoing=True, pattern="المده$"))
@bot.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptMed(Med):
    if Med.fwd_from:
        return
    Medid = await reply_id(Med)
    Medupt = await get_readable_time((time.time() - StartTime))
    if Med_IMG:
        Med_c = f"**{Med_TEXT}**\n"
        Med_c += f"**{MedEM} المستخدم :** {mention}\n"
        Med_c += f"**{MedEM} مدة التشغيل :** `{Medupt}`"
        await Med.client.send_file(Med.chat_id, Med_IMG, caption=Med_c, reply_to=Medid)
        await Med.delete()
    else:
        await edit_or_reply(
            Med,
            f"**{Med_TEXT}**\n\n"
            f"**{MedEM} المستخدم :** {mention}\n"
            f"**{MedEM} مدة التشغيل :** `{Medupt}`",
        )
