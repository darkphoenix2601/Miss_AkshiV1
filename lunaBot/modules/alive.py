from telethon import events, Button, custom
import re, os
from lunaBot.events import register
from lunaBot import telethn as tbot
from lunaBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/2cc96af4c1a40f44260cd.mp4"
@register(pattern=("/alive"))
async def awake(event):
 Tanjirou_Kamado = event.sender.first_name
 Tanjirou_Kamado = "🌞 I,m Tanjirou Kamado \n\n"
 Tanjirou_Kamado += "🌞 I'm Working with awesome speed**\n\n"
 Tanjirou_Kamado += "🌞 Miss_Akshi : 1.0 LATEST**\n\n"
 Tanjirou_Kamado += "🌞  𝘔𝘺 𝘰𝘸𝘯𝘦𝘳 : [Tanjirou](t.me/Lynncept77)\n\n"
 Tanjirou_Kamado += "🌞 Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("𝘚𝘶𝘱𝘱𝘰𝘳𝘵🔥", "https://t.me/Tanji_kamado_support"), Button.url("𝘜𝘱𝘥𝘢𝘵𝘦𝘴", "https://t.me/Tanji_Updates)]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Miss_Akshi,  buttons=BUTTON)
