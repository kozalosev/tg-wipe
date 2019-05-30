#!/usr/bin/env python

import asyncio
import time
import os
from telethon import TelegramClient
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.functions.channels import DeleteMessagesRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon.tl.types import Channel

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

client = TelegramClient('login', api_id, api_hash)
client.start()


async def main():
    dialogs = await client.get_dialogs()
    i = 0
    for dialog in dialogs:
        if isinstance(dialog.entity, Channel):
            print('[%s] %s %s' % (i, dialog.entity.id, dialog.entity.title))
        i += 1
    i = int(input('Enter channel index: '))

    chat = dialogs[i].entity
    print(chat)

    while True:
        result = await client(SearchRequest(
            peer=chat,
            q='',
            hash=0,
            filter=InputMessagesFilterEmpty(),
            min_date=None,
            max_date=None,
            offset_id=0,
            add_offset=0,
            from_id=(await client.get_me()).id,
            min_id=0,
            max_id=0,
            limit=100
        ))
        if len(result.messages) == 0:
            break
        ids = []
        for msg in result.messages:
            ids.append(msg.id)
            print('%s %s %s' % (msg.date, msg.id, len(ids)))
        result = await client(DeleteMessagesRequest(chat, ids))
        print(result)
        time.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
