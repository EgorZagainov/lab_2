from aiogram import Router, types, Bot
from aiogram.filters import Command

router_stickers = Router()

@router_stickers.message(Command("sticker"))
async def sricker (message: types.Message, bot: Bot):
    await bot.send_sticker(message.from_user.id,
sticker='CAACAgIAAxkBAAEKylVlXGJiYeK0IauZl0oifvrrjsgu3AACZAADWbv8JToS9CchlsxoMwQ')
