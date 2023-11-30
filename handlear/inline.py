from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, Bot


router_inline = Router()

@router_inline.message(Command("inline"))
async def cmd_inline(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
        )
    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
        )
    await message.answer(
        'Выберите ссылку', reply_markup=builder.as_markup(),
    )