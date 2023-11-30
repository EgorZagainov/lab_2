from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command
from aiogram import types
from aiogram import Router

router_core = Router()


@router_core.message(Command("core"))
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(types.KeyboardButton(text=str(i)))
        builder.adjust(4)
    await message.answer(
        "Выберите сколько ядер у вашего поцесора:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )