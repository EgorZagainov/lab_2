import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import TOKEN
from haendlear import start, inline, help_bot



async def main () -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start.router_start,
        inline.router_inline,
        help_bot.router_help

    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())