import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import TOKEN
from handlear import start, help_bot, core, my_id, stickers, random_number, inline, echo


async def main () -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start.router_start,
        help_bot.router_help,
        core.router_core,
        my_id.router_my_id,
        stickers.router_stickers,
        random_number.router_random,
        inline.router_inline,
        echo.router_echo

    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())