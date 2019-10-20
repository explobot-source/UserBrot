"""COMMAND : .eye"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "eye":

        await event.edit(input_str)

        animation_chars = [

            "👁👁\n  👄  =====> hey biatch, gimmie a cum",
            "👁👁\n  👅  =====> sup biatch",    
            "👁👁\n  💋  =====> I will hack you, boi",
            "👁👁\n  👄  =====> MAAAAAHNZ!",
            "👁👁\n  👅  =====> mahnz!",    
            "👁👁\n  💋  =====> if i were you...",
            "👁👁\n  👄  =====> actually hope u get cancer ",
            "👁👁\n  👅  =====> cyka blyat!",    
            "👁👁\n  💋  =====> do you like bananas?",
            "👁👁\n  👄  =====> hey, bro"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])
