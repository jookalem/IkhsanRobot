import random
from SiestaRobot.events import register
from SiestaRobot import telethn

APAKAH_STRING = ["iya", 
                 "tidak", 
                 "mungkin", 
                 "mungkin tidak", 
                 "bisa jadi", 
                 "mungkin saja",
                 "tidak mungkin",
                 "YNTKTS",
                 "pala bapak kau pecah",
                 "masa iya?",
                 "tanya aja sama mamak kau pler"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
