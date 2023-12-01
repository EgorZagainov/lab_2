from random import randint
from aiogram import Router, F
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command


router_random = Router()


@router_random.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )


@router_random.callback_query(F.data == "random_value")
async def send_random_value(callback_query: types.CallbackQuery):
    await callback_query.message.answer(str(randint(1, 10)))
    await callback_query.answer()
