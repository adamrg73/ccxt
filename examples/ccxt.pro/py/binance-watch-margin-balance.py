# -*- coding: utf-8 -*-

import asyncio
import ccxtpro as ccxt
from pprint import pprint


async def main(asyncio_loop):
    exchange = ccxt.binance({
        'asyncio_loop': asyncio_loop,
        'enableRateLimit': True,
        'apiKey': 'YOUR_API_KEY',
        'secret': 'YOUR_SECRET',
        'options': {
            'defaultType': 'margin',
        },
        # comment it out if you don't want debug output
        # this is for the demo purpose only (to show the communication)
        'verbose': True,
    })
    while True:
        try:
            balance = await exchange.watch_balance()
            # it will print the balance update when the balance changes
            # if the balance remains unchanged the exchange will not send it
            pprint(balance)
        except Exception as e:
            print('watch_balance() failed')
            print(e)
            break
    await exchange.close()

if __name__ == '__main__':
    asyncio_loop = asyncio.get_event_loop()
    asyncio_loop.run_until_complete(main(asyncio_loop))
