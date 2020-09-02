from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Biasakanlah Mengucapkan Salam")
    sleep(1)
    await typew.edit("Assalamualaikum")
# Create by myself @rizkynfs


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Jawab Salam Boss Astaga")
    sleep(1)
    await typew.edit("Waalaikumsalam")
# Create by myself @rizkynfs
