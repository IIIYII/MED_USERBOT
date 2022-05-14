"""
©Med : @MedThon
  - Commends of All Wallpapers
"""

from . import *

@bot.on(admin_cmd(pattern="م31"))
@bot.on(sudo_cmd(pattern="م31", allow_sudo=True))
async def Med(L_U_2):
    await eor(L_U_2, W)

@bot.on(admin_cmd(pattern="خلفيات1"))
@bot.on(sudo_cmd(pattern="خلفيات1", allow_sudo=True))
async def Med(L_U_2):
    await eor(L_U_2, WL)
    
@bot.on(admin_cmd(pattern="خلفيات2"))
@bot.on(sudo_cmd(pattern="خلفيات2", allow_sudo=True))
async def Med(L_U_2):
    await eor(L_U_2, BN)


